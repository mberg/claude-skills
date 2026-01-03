---
name: fitness-tracker
description: Log and analyze workouts. Use when the user wants to (1) record a workout at the gym via conversation, (2) parse workout markdown files to CSV, (3) query exercise history with DuckDB, or (4) track fitness progress. Triggers on "log workout", "record workout", "track workout", "add exercises", "what did I lift", etc.
---

# Fitness Tracker

Log workouts via conversation and analyze workout data with DuckDB.

## Chat Mode - Logging Workouts

Use this conversational flow when the user wants to record a workout:

### Step 1: Date
Ask for the workout date or default to today. Format: YYYY-MM-DD

### Step 2: Muscle Group
Ask what they're working. Categories from `reference/exercises.md`:
- Chest, Back, Shoulders, Legs
- Arms - Biceps, Arms - Triceps
- Core, Compound, Cardio

### Step 3: Exercise Selection
Show exercises from that category. Let user pick or type their own.

### Step 4: Sets Entry
User enters sets naturally:
- "135 for 10, 10" → `- 135 - 10, 10`
- "185 - 8, 8, 8" → `- 185 - 8, 8, 8`
- "10, 10, 10" (bodyweight) → `- 10, 10, 10`
- "30 minutes" (cardio) → `- 30m`
- Add "warmup" or other notes as `// comment`

### Step 5: More Exercises?
Ask if they want to add another exercise. Repeat steps 2-4 as needed.

### Step 6: Save
Save the workout to GitHub (or Obsidian as fallback):
- File: `workouts-YYYY-MM.md` (based on workout date)
- Add `## YYYY-MM-DD` header if it's a new day
- Append exercise name and sets in the format below
- Push to GitHub using `scripts/github_sync.py`

### Example Conversation
```
User: Log my workout
Claude: What date? (default: today, 2026-01-02)
User: Today
Claude: What are you working? (Chest, Back, Shoulders, Legs, Arms, Core, Cardio)
User: Chest
Claude: Chest exercises: Bench Press, Incline Bench Press, Dumbbell Press, Cable Flyes, Push-ups, Dips...
User: Bench
Claude: Enter your sets (e.g., "135 - 10, 10" or "185 for 8, 8, 8"):
User: 135 for 10, 10 warmup, then 185 - 8, 8, 8
Claude: Got it:
  Bench Press
  - 135 - 10, 10 // warmup
  - 185 - 8, 8, 8

  Another exercise?
User: Cable flyes, 30 - 12, 12, 12
Claude: Added. Another exercise?
User: Done
Claude: Saved to workouts-2026-01.md
```

## Workout File Format

Files are named `workouts-YYYY-MM.md` with multiple workouts per month:

```markdown
## 2026-01-02

Bench
- 135 - 10, 10 // warmup
- 185 - 8, 8, 8

Situps
- 10, 10, 10

Treadmill
- 30m
```

### Format Rules

- **Date header**: `## YYYY-MM-DD`
- **Exercise name**: Plain text on its own line
- **Weighted sets**: `- weight - reps, reps, reps` (e.g., `- 185 - 8, 8, 8`)
- **Bodyweight sets**: `- reps, reps, reps` (e.g., `- 10, 10, 10`)
- **Duration**: `- 30m` or `- 1h30m`
- **Notes**: `// comment` at end of line

## Configuration

Edit `scripts/config.json` to configure GitHub (default) or Obsidian storage:

```json
{
  "github_repo": "username/repo-name",
  "github_token": "github_pat_xxxxx",
  "github_branch": "main",
  "github_workout_dir": "workouts",
  "obsidian_workout_dir": "/path/to/obsidian/vault/Fitness",
  "output_csv": "/path/to/workouts.csv"
}
```

### GitHub Configuration (Default)
- `github_repo`: Your repository in `username/repo-name` format
- `github_token`: Personal Access Token with `repo` scope. Create at: https://github.com/settings/tokens
- `github_branch`: Target branch (default: `main`)
- `github_workout_dir`: Directory in repo for workout files (default: `workouts`)

### Obsidian Configuration (Fallback)
- `obsidian_workout_dir`: Local path to Obsidian vault directory (used if GitHub not configured)

## Writing Workout Files

When saving workouts in chat mode:

### GitHub (Default)
1. Read `scripts/config.json` to get GitHub settings
2. Create/update local temp file: `workouts-YYYY-MM.md`
3. If file exists in repo, fetch it first and append new workout
4. Add `## YYYY-MM-DD` header if it's a new day
5. Append exercise name and sets under the date header
6. Push to GitHub using `scripts/github_sync.py`:
   ```bash
   uv run scripts/github_sync.py \
     --file /tmp/workouts-2026-01.md \
     --dest workouts/workouts-2026-01.md \
     -m "Add workout for 2026-01-02"
   ```
7. Also push updated `workouts.csv` after parsing:
   ```bash
   uv run scripts/parse_workout.py /tmp/workouts-2026-01.md -o /tmp/workouts.csv
   uv run scripts/github_sync.py \
     --file /tmp/workouts.csv \
     --dest workouts/workouts.csv \
     -m "Update workout data"
   ```

### Obsidian (Fallback)
If GitHub is not configured (`github_repo` is empty):
1. Use `obsidian_workout_dir` from config
2. Target file: `{obsidian_workout_dir}/workouts-YYYY-MM.md`
3. Use Obsidian MCP tools or write directly to filesystem

## Parse Mode - Analyzing Workouts

```bash
# Uses paths from config.json
uv run scripts/parse_workout.py

# Override with explicit paths
uv run scripts/parse_workout.py /path/to/workouts/ -o workouts.csv

# Parse and run a query
uv run scripts/parse_workout.py --query "SELECT * FROM workouts"
```

## Exercise Validation

The parser checks exercise names against `reference/exercises.md` and suggests corrections for typos:

```
Unrecognized exercises:
  'Bech Press' - did you mean 'Bench Press'?
  'Squatts' - did you mean 'Squats'?
```

Add new exercises to `reference/exercises.md` to expand the known list.

## Output CSV Schema

| Column | Type | Description |
|--------|------|-------------|
| date | DATE | Workout date (YYYY-MM-DD) |
| exercise | VARCHAR | Exercise name |
| set_num | INTEGER | Set number within exercise |
| weight | DECIMAL | Weight used (empty for bodyweight) |
| reps | INTEGER | Rep count (empty for duration exercises) |
| duration_min | INTEGER | Duration in minutes (for timed exercises) |
| notes | VARCHAR | Comments from `// note` |

## Example Queries

```sql
-- Total volume per exercise
SELECT exercise, SUM(weight * reps) as volume
FROM workouts GROUP BY exercise ORDER BY volume DESC;

-- Bench press max weight over time
SELECT date, MAX(weight) as max_weight
FROM workouts WHERE exercise = 'Bench' GROUP BY date;

-- Weekly workout frequency
SELECT DATE_TRUNC('week', date) as week, COUNT(DISTINCT date) as days
FROM workouts GROUP BY 1 ORDER BY 1;

-- Exercises by total sets
SELECT exercise, COUNT(*) as total_sets
FROM workouts GROUP BY exercise ORDER BY total_sets DESC;
```

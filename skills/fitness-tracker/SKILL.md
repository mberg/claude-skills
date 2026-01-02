---
name: fitness-tracker
description: Parse workout logs from Obsidian markdown files into CSV and query with DuckDB. Use when the user wants to analyze workout data, track fitness progress, query exercise history, or parse workout markdown files.
---

# Fitness Tracker

Parse workouts from markdown files into structured CSV data for analysis with DuckDB.

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

Edit `scripts/config.json` to set default paths:

```json
{
  "obsidian_workout_dir": "/path/to/obsidian/vault/Fitness",
  "output_csv": "/path/to/workouts.csv"
}
```

## Parsing Workouts

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

---
name: cortex
description: Capture conversation summaries and web content to daily notes. Use when user says "save this", "summarize", "capture notes", or pastes a URL without context.
---

# Cortex

Capture conversation summaries and web content to daily notes synced to GitHub.

## Conversation Summary Mode

When the user wants to save or summarize the current conversation:

### Step 1: Ask for Instructions
Ask: "Any specific focus or instructions for the summary?"

### Step 2: Extract Key Ideas
Review the conversation and extract:
- Main concepts and decisions discussed
- Action items or conclusions
- Any URLs or resources mentioned

### Step 3: Format as Daily Note Entry
Create an entry with timestamp, key ideas, and links.

### Step 4: Save to GitHub
Fetch existing daily note, append new entry, push back.

### Example Conversation
```
User: Save this conversation
Claude: Any specific focus or instructions for the summary?
User: Focus on the architecture decisions we made
Claude: Got it. I'll summarize the architecture decisions.

Saved to notes-2026-01-03.md:
## 14:30 - Architecture Discussion

### Key Ideas
- Decided to use event-driven architecture for the notification system
- Will implement retry logic with exponential backoff
- Database schema will use soft deletes

### Links
- [Event-Driven Architecture](https://example.com/eda) - reference article discussed
```

## Link Summary Mode

When the user pastes a URL without context:

### Step 1: Offer to Summarize
Ask: "Would you like me to summarize this link?"

### Step 2: Get Focus Instructions
If yes, ask: "Any specific focus or instructions for the summary?"

### Step 3: Fetch and Summarize
Retrieve the page content and create a summary based on instructions.

### Step 4: Save to Daily Notes
Add the link with its summary to the daily notes.

### Example Conversation
```
User: https://example.com/article-about-microservices
Claude: Would you like me to summarize this link?
User: Yes, focus on the deployment strategies
Claude: Any other specific instructions?
User: Keep it brief

[Fetches and summarizes the article]

Saved to notes-2026-01-03.md:
## 15:00 - Link Summary

### Key Ideas
- Article recommends blue-green deployments for microservices
- Canary releases reduce risk for critical services
- Feature flags enable gradual rollouts

### Links
- [Microservices Deployment Strategies](https://example.com/article-about-microservices) - deployment patterns for microservices
```

## Daily Notes Format

Files are named `notes-YYYY-MM-DD.md` (one file per day). Multiple sessions throughout the day all append to the same file.

### Ordering Multiple Entries

When appending a new entry:
1. Fetch existing daily note
2. Parse existing entries by their `## HH:MM` timestamps
3. Insert new entry in chronological order (don't intermix - each summary stays as a complete block)
4. Push updated file

The exact timestamp isn't critical - entries just need to be roughly in order of when they happened.

Example: `notes-2026-01-03.md`
```markdown
## 14:30 - Architecture Discussion

### Key Ideas
- Decided to use event-driven architecture
- Will implement retry logic with exponential backoff

### Links
- [Event-Driven Architecture](https://example.com/eda) - reference article

---

## 15:00 - Link Summary

### Key Ideas
- Blue-green deployments recommended for microservices

### Links
- [Microservices Guide](https://example.com/guide) - deployment patterns

---
```

### Format Rules

- **Filename**: `notes-YYYY-MM-DD.md`
- **Entry header**: `## HH:MM - Title`
- **Key Ideas section**: `### Key Ideas` with bullet points
- **Links section**: `### Links` with `[Title](URL) - description`
- **Entry separator**: `---` between entries

## Configuration

Edit `scripts/config.json` to configure GitHub storage:

```json
{
  "github_repo": "mberg/cortex",
  "github_token": "github_pat_xxxxx",
  "github_branch": "main",
  "github_notes_dir": "notes"
}
```

- `github_repo`: Your repository in `username/repo-name` format
- `github_token`: Personal Access Token with `repo` scope. Create at: https://github.com/settings/tokens
- `github_branch`: Target branch (default: `main`)
- `github_notes_dir`: Directory in repo for notes (default: `notes`)

## GitHub Workflow

**Important:** Must `cd` into the scripts directory so `github_sync.py` can find `config.json`.

### Step 1: Fetch existing daily note (if any)

```bash
cd /mnt/skills/user/cortex/scripts
uv run github_sync.py --fetch notes/notes-2026-01-03.md > /tmp/notes-2026-01-03.md
```

If the file doesn't exist yet, create it empty.

### Step 2: Append new entry

```bash
cat >> /tmp/notes-2026-01-03.md << 'EOF'

## 14:30 - Session Summary

### Key Ideas
- Main concept discussed
- Decision made

### Links
- [Resource](https://example.com) - description

---
EOF
```

### Step 3: Push back to GitHub

```bash
cd /mnt/skills/user/cortex/scripts
uv run github_sync.py \
  --file /tmp/notes-2026-01-03.md \
  --dest notes/notes-2026-01-03.md \
  -m "Add notes for 2026-01-03"
```

### Key Details

- **Working directory matters** — Must `cd` into `scripts/` so `github_sync.py` can find `config.json`
- **Config location** — The script looks for `config.json` in the same directory as the script itself
- **Dest path** — The `--dest` is relative to the repo root (e.g., `notes/notes-2026-01-03.md`)

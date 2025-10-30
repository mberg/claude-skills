# Claude Skills

A repository of Claude Code skills managed with GitHub.

## Setup

To use these skills with Claude Code, create a symlink from this repository to your Claude configuration:

### macOS/Linux

```bash
ln -s /path/to/claude-skills/skills ~/.claude/skills
```

### Windows (PowerShell as Admin)

```powershell
New-Item -ItemType SymbolicLink -Path "$env:APPDATA\.claude\skills" -Target "C:\path\to\claude-skills\skills"
```

After setup, skills will be automatically discovered by Claude Code. Changes pushed to this repository are immediately available.

## Available Skills

| Skill | Description |
|-------|-------------|
| **whatsapp-flows** | Authoring WhatsApp Business Flows with validation, component guidance, and server integration patterns. Use when building conversational experiences, collecting user data, implementing conditional logic, or integrating with backend endpoints. |

## Next Steps

See individual skill directories for full documentation (e.g., `skills/whatsapp-flows/SKILL.md`).

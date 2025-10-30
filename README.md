# Claude Skills Repository

A curated collection of Claude Code skills for authoring, validation, and integration patterns. Organized for easy discovery and progressive learning.

## What Are Claude Skills?

Claude Skills extend Claude Code's capabilities with specialized knowledge domains. Each skill provides:
- Quick start guides
- Reference documentation
- Working examples
- Validation tools
- Best practices

## Available Skills

### whatsapp-flows

Authoring WhatsApp Business Flows with validation, component guidance, and server integration patterns.

**Use when:**
- Building conversational experiences
- Collecting user data with forms
- Implementing conditional logic
- Integrating with backend endpoints

**Key features:**
- 22 WhatsApp Flow components documented
- Data binding syntax (form, server, global references)
- Conditional logic patterns (If/Switch)
- Server integration with routing models
- Security best practices
- Feature matrix for versions 4.0-7.1

**Quick start:** See `skills/whatsapp-flows/SKILL.md`

---

## Installation

There are two ways to use these skills:

### Option 1: Symlink to Your Local Claude Config (Recommended)

This approach makes skills automatically available in Claude Code and keeps them synced with your repository.

#### Prerequisites
- Git installed
- Claude Code CLI installed
- This repository cloned locally

#### Setup Steps

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/claude-skills.git
   cd claude-skills
   ```

2. **Create the symlink**
   ```bash
   # On macOS/Linux:
   ln -s /path/to/claude-skills/skills ~/.claude/skills

   # On Windows (PowerShell as Admin):
   New-Item -ItemType SymbolicLink -Path "$env:APPDATA\.claude\skills" -Target "C:\path\to\claude-skills\skills"
   ```

3. **Verify installation**
   ```bash
   # macOS/Linux:
   ls -la ~/.claude/skills/

   # Windows (PowerShell):
   Get-Item $env:APPDATA\.claude\skills | Select-Object -Property Target
   ```

   You should see:
   ```
   skills -> /path/to/claude-skills/skills
   whatsapp-flows/
   ```

4. **Start using skills**

   Open Claude Code and reference any skill. For example:
   ```
   /whatsapp-flows
   ```

#### Benefits
- ✓ Skills automatically discovered by Claude Code
- ✓ Changes in repository are instantly available
- ✓ Single source of truth for your skills
- ✓ Easy to add more skills over time
- ✓ Version control for all changes

### Option 2: Manual Copy

If you prefer to manage skills without symlinking:

1. Copy the `skills/` directory to `~/.claude/`
   ```bash
   cp -r /path/to/claude-skills/skills ~/.claude/
   ```

2. To update skills, pull changes and re-copy:
   ```bash
   git pull
   cp -r /path/to/claude-skills/skills ~/.claude/
   ```

---

## Skill Structure

Each skill follows this structure:

```
skill-name/
├── SKILL.md                    # Main entry point (< 500 lines)
├── examples.md                 # Working examples
├── reference/                  # Detailed documentation
│   ├── TABLE_OF_CONTENTS.md    # Navigation guide
│   ├── topic-1.md
│   ├── topic-2.md
│   └── ...
└── scripts/                    # Validation/utility scripts
    └── tool.py
```

**Key principles:**
- `SKILL.md` is concise and links to detailed references
- Progressive disclosure: users find what they need when they need it
- References are organized by topic, not complexity
- Examples are complete and copy-paste ready
- Scripts provide validation and automation

---

## Using Skills in Claude Code

### Accessing a skill

Reference a skill by name in your request:

```
I need to build a WhatsApp Flow for a customer survey.
Can you help me structure the JSON following the whatsapp-flows skill?
```

Claude will automatically load the skill and provide relevant guidance.

### Exploring skill contents

Each skill's main file (`SKILL.md`) includes:
1. **Quick start** - 5-minute overview
2. **Essential concepts** - Key ideas and constraints
3. **Reference links** - Links to detailed documentation
4. **Common tasks** - Step-by-step guides
5. **Examples** - Working code you can adapt
6. **Troubleshooting** - Common issues and solutions

### Progressive learning

Skills are designed for progressive disclosure:
1. Start with `SKILL.md` quick start
2. Check examples in `examples.md`
3. Read relevant reference files as needed
4. Explore advanced topics in detail
5. Use validation scripts to verify your work

---

## Managing Your Skill Repository

### Adding a new skill

1. Create a new directory in `skills/`
   ```bash
   mkdir skills/my-skill
   ```

2. Create the skill structure
   ```bash
   touch skills/my-skill/SKILL.md
   mkdir skills/my-skill/reference
   mkdir skills/my-skill/examples
   mkdir skills/my-skill/scripts
   ```

3. Follow the [Skill Creation Guide](#skill-creation-guide)

4. Commit and push
   ```bash
   git add skills/my-skill/
   git commit -m "Add my-skill"
   git push
   ```

5. If using symlink, it's immediately available in Claude Code!

### Updating a skill

Make changes directly in the repository:

```bash
cd skills/whatsapp-flows/
# Edit SKILL.md, reference files, examples, etc.
git add .
git commit -m "Update whatsapp-flows: improve X, add Y"
git push
```

Changes are instantly available if using the symlink approach.

### Versioning

Skills follow semantic versioning in their `SKILL.md` frontmatter:

```yaml
---
name: skill-name
version: 1.0.0
description: ...
---
```

Update version when making changes:
- `PATCH` (1.0.1) - Bug fixes, minor clarifications
- `MINOR` (1.1.0) - New features, new components
- `MAJOR` (2.0.0) - Breaking changes, restructuring

---

## Skill Creation Guide

### Minimal skill template

Create `SKILL.md`:

```yaml
---
name: my-skill
description: Brief description of what this skill helps with.
---

# My Skill

One paragraph explaining the skill's purpose.

## Quick Start

### Key Concept 1
Explanation and simple example.

### Key Concept 2
Explanation and simple example.

## Essential Reference

| Item | Description |
|------|-------------|
| Item 1 | Details |
| Item 2 | Details |

See **[reference/guide-1.md](reference/guide-1.md)** for detailed guide 1.
See **[reference/guide-2.md](reference/guide-2.md)** for detailed guide 2.

## Examples

See **[examples.md](examples.md)** for working examples.

## Common Tasks

### I need to...
See **[reference/guide-1.md](reference/guide-1.md)** section X.

## Troubleshooting

### Issue...
**Solution:** ...

---

## Next Steps

See [reference/TABLE_OF_CONTENTS.md](reference/TABLE_OF_CONTENTS.md) for navigation.
```

### Structure checklist

- [ ] `SKILL.md` (< 500 lines)
  - [ ] YAML frontmatter
  - [ ] Quick start (5-10 min)
  - [ ] Essential concepts table
  - [ ] Links to reference files
  - [ ] Common tasks guide
  - [ ] Troubleshooting section

- [ ] `examples.md` (root level)
  - [ ] 2-4 complete working examples
  - [ ] Copy-paste ready code
  - [ ] Comments explaining patterns

- [ ] `reference/` folder
  - [ ] `TABLE_OF_CONTENTS.md` (navigation)
  - [ ] 5-10 topic-focused files
  - [ ] Syntax examples
  - [ ] Best practices
  - [ ] Validation rules

- [ ] `scripts/` folder (if applicable)
  - [ ] Validation tools
  - [ ] Automation scripts
  - [ ] README for running scripts

### Guidelines

**SKILL.md:**
- Keep under 500 lines
- Progressive disclosure: link to references
- Assume Claude is capable; don't overwhelm
- Focus on "why" not exhaustive details
- Link to examples early and often

**References:**
- Organize by topic, not complexity tier
- One-level deep (no nested folders)
- Preserve detailed content from original docs
- Include complete examples
- Provide validation rules and constraints

**Examples:**
- Must be complete and working
- Include realistic scenarios
- Copy-paste ready
- Document each example's purpose
- Show multiple patterns/approaches

---

## Contributing

Found an issue or have a suggestion?

1. Check existing skills for similar patterns
2. Test your changes thoroughly
3. Commit with clear messages
4. Push to your branch
5. Create a pull request with explanation

---

## Directory Structure

```
claude-skills/
├── README.md                    # This file
├── skills/                      # All skills live here
│   └── whatsapp-flows/         # Example skill
│       ├── SKILL.md
│       ├── examples.md
│       ├── reference/
│       │   ├── TABLE_OF_CONTENTS.md
│       │   ├── components.md
│       │   ├── actions.md
│       │   ├── data-binding.md
│       │   ├── conditional-logic.md
│       │   ├── server-integration.md
│       │   ├── constraints.md
│       │   ├── security.md
│       │   └── versions.md
│       └── scripts/
│           ├── validate_flow.py
│           └── validate_components.py
└── .gitignore
```

---

## Troubleshooting

### Skills not appearing in Claude Code

**Check 1: Symlink is correct**
```bash
# macOS/Linux:
ls -la ~/.claude/skills/

# Should show:
# skills -> /path/to/claude-skills/skills
```

**Check 2: SKILL.md exists**
```bash
ls ~/.claude/skills/my-skill/SKILL.md
```

**Check 3: YAML frontmatter is valid**
```bash
head -5 ~/.claude/skills/my-skill/SKILL.md

# Should start with:
# ---
# name: skill-name
# description: ...
# ---
```

**Check 4: Restart Claude Code**
Close and reopen Claude Code to reload skills.

### Changes not reflecting

If using symlink and changes aren't showing:

1. Verify the symlink points to correct directory
2. Check file was saved
3. Reload Claude Code (close and reopen)

---

## Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code/claude_code_docs_map.md)
- [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- [Skills Best Practices](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices)

---

## License

Include your license here (e.g., MIT, Apache 2.0, etc.)

---

## Questions?

See individual skill READMEs for skill-specific documentation.

# How to Use the Manuscript Writing Review Skill with Claude Code

## What This Is

The file `SKILL.md` encodes a systematic writing-quality review process based on
Dr. Kristin Sainani's "Writing in the Sciences" methodology. When placed in the
right location, Claude Code will automatically discover and apply these review
standards whenever you ask it to review your manuscript's writing.

Think of it as teaching Claude Code the editorial standards of a demanding
journal reviewer — once, in a file — so that every review it performs on your
manuscript follows the same rigorous protocol.

## Setup: Where to Put the File

### Option A — Project-level skill (recommended)

Place the skill inside the `.claude/skills/` directory of your manuscript project:

```
my-manuscript/
├── .claude/
│   └── skills/
│       └── manuscript-review/
│           └── SKILL.md          ← put it here
├── draft.tex                     (or .md, .docx, etc.)
├── figures/
└── references.bib
```

Commands to set this up:

```bash
cd /path/to/my-manuscript
mkdir -p .claude/skills/manuscript-review
cp /path/to/SKILL.md .claude/skills/manuscript-review/SKILL.md
```

This makes the skill available whenever you run Claude Code from within this
project directory.

### Option B — Global skill (available for all your projects)

Place it in your home directory's `.claude/skills/` folder:

```bash
mkdir -p ~/.claude/skills/manuscript-review
cp /path/to/SKILL.md ~/.claude/skills/manuscript-review/SKILL.md
```

This makes the skill available in every project you open with Claude Code.

## Using the Skill

### Step 1: Open your manuscript project in VS Code

Open your terminal in VS Code (`` Ctrl+` `` or **Terminal → New Terminal**).
Navigate to your manuscript's root directory if you aren't already there.

### Step 2: Launch Claude Code

```bash
claude
```

Claude Code starts an interactive session in your terminal. It will automatically
detect any skills in `.claude/skills/`.

### Step 3: Ask for a review

Here are example prompts, ordered from broadest to most targeted:

**Full manuscript review:**

```
Review the writing quality of draft.tex
```

```
Do a full writing review of my manuscript in the paper/ directory.
Focus on sections 1 through 4.
```

**Single section:**

```
Review the writing in my Introduction (sections/introduction.tex)
```

**Targeted pass (one dimension only):**

```
Check draft.tex for passive voice and smothered verbs
```

```
Audit my Results section for keyword consistency — make sure group names
and variable names match what I defined in Methods
```

```
Strip the clutter from my Discussion. It's too wordy.
```

**Interactive, paragraph-by-paragraph editing:**

```
Walk me through improving the writing in my Introduction,
paragraph by paragraph
```

This mode is the most instructive: Claude shows you the original, a revised
version, and explains every change before moving on.

### Step 4: Review the output

Claude Code will produce a structured report (for full/section review) or
walk you through changes interactively. Each finding includes:

- The original text
- A concrete suggested revision
- The rationale (which principle it violates)
- A severity tag (CRITICAL / MAJOR / MINOR)

### Step 5: Apply changes (your choice)

Claude Code can also apply the edits directly to your files if you ask:

```
Apply the CRITICAL and MAJOR revisions to draft.tex
```

Or you can review them manually and incorporate the ones you agree with. The
interactive mode is especially good for this — you approve each paragraph
before Claude moves on.

## Tips for Best Results

**Tell Claude your target journal.** Different journals have different style
conventions. For example:

```
Review my manuscript for writing quality. Target journal is the
Journal of Fluid Mechanics. They prefer active voice throughout,
including in Methods.
```

**Point to specific pain points.** If you know your Discussion is bloated but
your Methods are clean, say so:

```
My Discussion is twice as long as it should be. Help me strip it down
without losing any of the scientific arguments.
```

**Use interactive mode for learning.** If you want to internalize these
principles (not just get a one-time cleanup), the paragraph-by-paragraph mode
teaches you why each change matters.

**Combine with your CLAUDE.md.** If your project already has a `CLAUDE.md` or
`AGENTS.md` that describes your codebase and conventions, the skill adds a
complementary layer — your CLAUDE.md handles the computational context, while
this skill handles writing standards. They work together.

## What This Skill Does NOT Do

- It does **not** evaluate scientific content, methods, or results.
- It does **not** check citation formatting (use a reference manager for that).
- It does **not** restructure your argument or reorder sections.
- It does **not** generate new text — it only revises existing prose.

If you need a full technical peer review (methods, novelty, significance),
that is a different task. This skill is purely about writing clarity and
precision.

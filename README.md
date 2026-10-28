# SciWrite — Manuscript Writing Review

An [Agent Skill](https://agentskills.io) that reviews scientific and engineering manuscripts for writing quality, applying the methodology from Dr. Kristin Sainani's [*Writing in the Sciences*](https://www.coursera.org/learn/sciwrite) course at Stanford.

## What this skill does

Clear writing is not a cosmetic concern in science; it determines whether reviewers and readers can follow your argument. Yet most graduate students receive little formal training in scientific writing, and self-editing for clarity is difficult because you already know what you meant to say.

This skill encodes a systematic editorial review distilled from 30 video lectures on scientific writing, extended with Nature's guidance on structuring a summary paragraph. It works on anything from a whole manuscript to a single sentence, in six audit passes:

1. **Clutter.** Dead-weight phrases, empty openers ("There are several studies that…"), redundancies, and negative constructions, with concise replacements.
2. **Voice and verbs.** Passive constructions that hide who did what, and smothered verbs ("performed an analysis of" → "analyzed").
3. **Sentence and paragraph architecture.** Buried verbs, overloaded sentences, dangling modifiers, paragraphs without a clear main idea or topic sentence, and transitions that don't fit the logic. In full reviews, it also checks what each section must do: an Introduction that states the gap, Results that lead with findings, a Discussion that opens with the answer and states limitations.
4. **Terminology.** Key terms, group names and acronyms used consistently, so the reader never wonders whether "heavier participants" are the "obese group".
5. **Numbers and citations.** Values that disagree between text and tables, and statistics cited only to a review.
6. **Summary paragraph structure.** An abstract checked against the sequence of moves Nature prescribes, from field context to "Here we show" to broader significance, with sentence budgets and word count.

You can ask for a full review, a single section, a single pass ("check for passive voice"), an abstract review, or an interactive walk-through, paragraph by paragraph. Reports group repeated problems, tag each finding CRITICAL, MAJOR or MINOR, give its location, and show a concrete revision.

The skill does not alter scientific content, data, or claims, and it never makes a claim stronger or weaker on its own. It improves how your claims are delivered. It is not a substitute for technical peer review.

## Install

A skill is a folder (`skills/sciwrite/`) holding `SKILL.md` and two reference files the skill reads when it needs them. Most tools install the whole folder from the release ZIP or from this repository.

| Where you use AI | How to install |
|---|---|
| Claude (web, desktop, Cowork) | Upload the release ZIP under **Customize → Skills** |
| Claude Code | `/plugin install sciwrite --marketplace labarba/sciwrite` |
| ChatGPT | Upload the release ZIP under **Skills** (workspace plans) |
| Gemini app | Upload the release ZIP under **Customize → Skills** |
| Codex, Copilot, Cursor, Gemini CLI and other coding agents | `gh skill install labarba/sciwrite sciwrite` or `npx skills add labarba/sciwrite` |
| Any other tool | Paste the three skill files into its custom instructions |

The **release ZIP** is `sciwrite-<version>.zip`, attached to the [latest release](https://github.com/labarba/sciwrite/releases/latest). It holds the `sciwrite/` folder and nothing else. Don't use GitHub's green **Code → Download ZIP** button: that archive contains the whole repository.

Steps and menus below were checked in October 2026. These products change often; if a menu has moved, the links to each vendor's help page have the current steps.

> **Upgrading from version 0.1?** The skill was renamed from `manuscript-writing-review` to `sciwrite`. Remove the old skill first, so the two don't compete.

### Claude (claude.ai, Claude desktop, Cowork)

1. Make sure code execution is on: **Settings → Capabilities → Code execution and file creation**. On Enterprise plans, an owner must also enable skills for the organization.
2. Go to **Customize → Skills**, click **+**, then **Create skill → Upload a skill**, and upload the release ZIP.
3. Check that the skill's toggle is on.

The skill is then available in every chat and in Cowork, and it syncs to Claude Code when you're signed in with the same account. Skills are available on Free, Pro, Max, Team and Enterprise plans. See [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills).

### Claude Code

This repository is a Claude Code plugin marketplace. In a session, run:

```
/plugin install sciwrite --marketplace labarba/sciwrite
```

From your shell, the same works as `claude plugin install sciwrite --marketplace labarba/sciwrite`. These one-step commands need Claude Code 2.1.275 or later in a session, 2.1.292 or later in the shell; on older versions, run `/plugin marketplace add labarba/sciwrite` and then `/plugin install sciwrite@sciwrite`. Third-party marketplaces don't auto-update by default: to get a new version, run `/plugin marketplace update sciwrite`, or turn on auto-update for it in the **Marketplaces** tab of `/plugin`.

To install without the plugin system, copy the folder into your personal or project skills directory:

```bash
git clone https://github.com/labarba/sciwrite.git
cp -r sciwrite/skills/sciwrite ~/.claude/skills/
```

### ChatGPT

1. Open the **Skills** page (in recent versions it sits under **Plugins**), click **Create**, then **Upload from your computer**, and select the release ZIP.
2. ChatGPT scans uploaded skills before they become available.

At the time of writing, OpenAI documents skills for workspace plans (Business, Enterprise, Edu, Healthcare), where an admin must allow skill uploads. Availability on personal plans was unclear, so check whether **Skills** appears in your account. Without it, use the "any other tool" method below in a Project's instructions. See [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

### Gemini app

Skills replace Gems in the Gemini app ([announcement](https://workspaceupdates.googleblog.com/2026/09/skills-gemini-app-workspace.html)).

1. At [gemini.google.com](https://gemini.google.com), click **Customize** in the sidebar (under **More** if you don't see it), then **Skills**.
2. Click **Create → Upload**, select the release ZIP, review the skill, and click **Create**.
3. Gemini uses the skill when your request matches it; you can also call it by typing `/` (or `@`) in a chat.

Uploading works on the web and in the Mac app. You must be 18 or over, signed in, with Keep Activity on. To update to a new version, open the skill, choose **More → Replace skill**, and upload the new ZIP. Skills in Google Workspace apps are created separately from the Gemini app's and don't sync with them. See [Create and manage skills for Gemini Apps](https://support.google.com/gemini/answer/17094296).

### Coding agents (Codex, GitHub Copilot, Cursor, Gemini CLI and others)

Two command-line installers work across dozens of agents. With the [GitHub CLI](https://cli.github.com/manual/gh_skill_install):

```bash
gh skill install labarba/sciwrite sciwrite --agent codex --scope user
```

Replace `codex` with your agent (`github-copilot`, `cursor`, `gemini-cli`, `claude-code`, …). Without `--scope user`, the skill installs into the current repository only.

Or with the [skills CLI](https://skills.sh), which asks which agents to install for:

```bash
npx skills add labarba/sciwrite
```

### Any other AI tool

If your tool has no skill support, paste the skill into whatever holds persistent instructions (a custom assistant, a project, a system prompt). Paste all three files, in this order: [`SKILL.md`](skills/sciwrite/SKILL.md), [`references/section-guidance.md`](skills/sciwrite/references/section-guidance.md), and [`references/summary-paragraph.md`](skills/sciwrite/references/summary-paragraph.md). `SKILL.md` alone works for most reviews, but abstract reviews and section-level checks depend on the reference files.

**Before installing any skill, read it.** A skill is instructions that your AI tool will follow, and some skills include scripts. This one is plain Markdown with no scripts.

## Using the skill

Ask in plain language, and paste your text or point to a file. For example:

- `Review the writing quality of draft.tex. I'm submitting to the Journal of Fluid Mechanics.`
- `Review the writing in my Introduction (sections/introduction.tex)`
- `Check my Results and Discussion for keyword consistency with Methods`
- `Is my abstract too long for Nature? [paste abstract]`
- `Can you make this sentence less clunky? "[sentence]"`
- `Walk me through improving my Introduction, paragraph by paragraph`

In a coding agent, the skill can also apply the revisions you accept (`Apply the CRITICAL and MAJOR revisions to draft.tex`); for LaTeX, it can suggest `latexdiff` to produce a marked-up copy for coauthors.

**Tips**

- **Name your target journal,** especially for abstracts. Nature caps a summary paragraph at about 200 words and requires citations in it; most journals allow more words and forbid citations in the abstract. Without a journal, the skill applies Nature's defaults and says so.
- **Give enough text for the check you want.** Terminology and number checks need the whole manuscript; a sentence is enough for clutter and verbs.
- **Use the interactive mode to learn.** The paragraph-by-paragraph walk-through explains each change, which builds habits rather than fixing one draft.
- **Review the output critically.** Your domain expertise is the final check. A flagged term may be standard in your field, and whether a number belongs in your abstract depends on what your result is. If a revision changes your meaning, say so and ask again.

## Customizing

The skill encodes general principles. You can add conventions for your field or target journal as a new section in your copy of `SKILL.md`, for example:

```markdown
## Journal-specific conventions

Target journal: Journal of Fluid Mechanics (JFM)
- Use "figure" (lowercase) in running text; "Figure" only at the start of a sentence.
- Equations are referenced as (1), not Eq. (1), unless at the start of a sentence.
- Use Oxford commas.
```

You can also edit the clutter and smothered-verb tables, the severity definitions, or the section guidance.

## What's in this repository

```
skills/sciwrite/
├── SKILL.md                     # the skill: modes, gotchas, the six passes, report format
├── references/
│   ├── summary-paragraph.md     # Pass 6 and abstract-only rules, read when an abstract is reviewed
│   └── section-guidance.md      # what each section must do, read in full and section reviews
└── evals/                       # tests: output cases, answer key, trigger queries, baseline results
.claude-plugin/                  # Claude Code plugin and marketplace manifests
tools/                           # scripts that run and grade the tests
```

The tests run each case with and without the skill and grade the output against checkable assertions; see [`evals/README.md`](skills/sciwrite/evals/README.md). For how the skill was made and revised, see [HISTORY.md](HISTORY.md); for what changed in each version, the [CHANGELOG](CHANGELOG.md).

## Contributing

If you find an edge case the skill handles poorly—a field-specific convention it misjudges, a clutter pattern it misses, or a false positive that keeps coming up—open an issue describing it, or submit a pull request. A new test case in `evals/` that shows the problem is the most useful contribution of all.

## How to cite

If you use this skill in your work or teaching, please cite it using the information in [CITATION.cff](CITATION.cff) (GitHub's **Cite this repository** button formats it for you).

## License

This skill is licensed under [CC BY 4.0](LICENSE). You are free to use, adapt, and share it, with attribution.

## Acknowledgments

Developed as part of the course [MAE 6291: Generative AI for Engineering Research](https://barbagroup.github.io/mae6291-genai/) at the George Washington University School of Engineering and Applied Science, and shared through the [GW Engineering AI Academy](https://www.seas.gwu.edu/ai-academy). Pass 6 was contributed by [Kyle Niemeyer](https://github.com/kyleniemeyer).

The writing methodology is drawn from Dr. Kristin Sainani's [*Writing in the Sciences*](https://www.coursera.org/learn/sciwrite) course at Stanford University. The original video lectures are available on [YouTube](https://www.youtube.com/playlist?list=PLVc-QdfGfSl2Ntc6CvIP83Nj_uHTSdNSw) under a CC BY license.

The summary paragraph structure in Pass 6 follows Nature's guide to authors, ["How to construct a Nature summary paragraph"](https://www.nature.com/documents/nature-summary-paragraph.pdf) (September 2019). That document is the property of Springer Nature and is referenced here, not reproduced.

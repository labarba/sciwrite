# SciWrite — Manuscript Writing Review

An [Agent Skill](https://agentskills.io) that reviews scientific and engineering manuscripts for writing quality, applying the methodology from Dr. Kristin Sainani's [*Writing in the Sciences*](https://www.coursera.org/learn/sciwrite) course at Stanford (2012).

## What This Skill Does

Clear writing is not a cosmetic concern in science; it determines whether reviewers and readers can follow your argument. Yet most graduate students receive little formal training in scientific writing, and self-editing for clarity is difficult because you already know what you meant to say.

This skill encodes a systematic editorial review process distilled from 30 video lectures on scientific writing, extended with Nature's published guidance on structuring a summary paragraph. When loaded into an AI tool, it performs six sequential audit passes on your manuscript text:

1. **Clutter extraction.** Flags dead-weight phrases, unnecessary jargon, and filler language, and provides concise replacements.
2. **Voice and verb vitality.** Identifies passive constructions, smothered verbs (nominalizations), and weak verb choices, and suggests active alternatives.
3. **Sentence architecture.** Evaluates sentence length, structure, and flow—flagging run-on sentences, misplaced modifiers, and paragraphs that lack a clear logical progression.
4. **Keyword consistency.** Checks that key technical terms are used consistently throughout the manuscript, catching cases where synonyms introduce ambiguity.
5. **Numerical and citation integrity.** Audits numerical values, units, and in-text citations for internal consistency (e.g., a value reported as 3.2 in the text but 3.4 in a table).
6. **Summary paragraph structure.** Checks an abstract against the sequence of rhetorical moves Nature prescribes—field introduction, background, problem statement, result ("Here we show"), comparison to prior understanding, and broader context. Reports missing or misordered moves, per-move sentence budgets, total word count, numbers and abbreviations that are not essential, and terms an outside reader may stumble on.

The skill supports five review modes: a full-manuscript review that runs all six passes, a single-section review, a targeted review that runs only the pass you specify (e.g., "fix passive voice"), an interactive mode that walks through the manuscript paragraph by paragraph with before/after examples, and an abstract review that runs the structural pass on its own. The output is a structured report with specific findings, concrete revisions, and severity tags. Abstract reviews additionally return a move-tagged rendering of the paragraph, labelling each sentence with the rhetorical function it performs so that a missing or misplaced move is visible at a glance.

Importantly, the skill does not alter scientific content, data, or technical claims. It improves how those claims are delivered.

## How This Skill Was Made

The creation of this skill illustrates a three-tool workflow that combined an agentic browser, a synthesis engine, and a skill-authoring assistant.

**Step 1: Extracting video URLs with an agentic browser.** The source material is a [YouTube playlist](https://www.youtube.com/playlist?list=PLVc-QdfGfSl2Ntc6CvIP83Nj_uHTSdNSw) of 30 lecture recordings from Sainani's course, posted under a Creative Commons Attribution license (CC-BY). To process them, I first needed the individual video URLs. Rather than clicking through each video's share menu 30 times, I opened the playlist in [Comet](https://comet.page) (an agentic browser by Perplexity) and instructed it to extract every URL, stripping the tracking parameters. In under a minute, the agent produced a clean list of all 30 URLs, a task that would have taken 15–20 minutes of tedious manual work.

**Step 2: Synthesizing the content with NotebookLM.** I pasted all 30 URLs into a new [Google NotebookLM](https://notebooklm.google.com/) notebook. NotebookLM ingested the video transcripts as sources and, using its Studio panel, I produced a Writing Standards Manual: a comprehensive narrative document distilling the key principles from all 30 lectures into a structured reference. The output captured the core ideas—strip sentences to their cleanest components, use active voice, resurrect smothered verbs, maintain keyword consistency—but it was formatted as a human-readable guideline, not as a machine-actionable skill file.

**Step 3: Converting the guideline into a SKILL.md file with Claude.** I pasted the full Writing Standards Manual into a Claude conversation, along with instructions to produce a properly formatted `SKILL.md` following the Agent Skills conventions, and a How-To file. Claude checked the skill format structure—YAML frontmatter, Markdown body, the relationship between the description field and trigger behavior—and produced two files: the `SKILL.md` itself, architected as an operational protocol with the five sequential audit passes and four review modes, and a companion `HOW-TO-USE.md` with installation instructions and example prompts. The skill-authoring step used Claude's built-in **skill creator** capabilities, making the process meta in the best sense: an AI tool creating instructions for an AI tool.

Three different AI tools, each doing what it does best. The browser agent handled the mechanical extraction. NotebookLM handled the synthesis of 30 video transcripts into a coherent document. Claude handled the architectural work of converting a human-readable guideline into a machine-actionable skill with proper formatting.

**Step 4: Extending the skill with Nature's summary paragraph guidance.** The five original passes all operate at or below the sentence: they ask whether each sentence is well built, not whether the right sentences are present. Nature's [guide to authors](https://www.nature.com/documents/nature-summary-paragraph.pdf) supplies the missing layer—a prescribed sequence of rhetorical moves for a summary paragraph, with a sentence budget for each. Adding it meant classifying the guidance by how much architectural disruption it required: advice that could be absorbed into existing passes as new rows or clauses; advice that fit as a new contained pass; advice that required extending the mode table and severity definitions; and advice that could not be implemented at all without abandoning the skill's design as a post-hoc, deterministic review instrument. Nature's requirement that a summary paragraph be "comprehensible to a scientist in any discipline," for example, has no mechanical test, so the skill approximates it with a list of specific terms an outside reader may stumble on and reports them as advisory notes rather than as errors. Judging whether a paper has genuinely moved its field forward was left out entirely: it requires knowledge of the literature outside the document, and every other check in the skill is self-contained.

## What Is an Agent Skill?

An Agent Skill is an industry-standard format for giving AI tools reusable, domain-specific instructions. It is a Markdown file (`SKILL.md`) with a short header that tells the AI *when* to use it and a body that tells the AI *how* to perform the task.

Skills were introduced by Anthropic in October 2025 and published as an [open standard](https://agentskills.io) in December 2025. They are now supported across Claude, ChatGPT, GitHub Copilot, Cursor, and other AI tools. A skill you write once works across platforms and improves over time as you refine it.

Think of a skill as a detailed rubric or style guide, except the reader is an AI assistant rather than a human colleague.

## How to Use This Skill

### In Claude.ai (recommended starting point)

This is the simplest way to get started. No terminal or coding experience is required. There are two approaches, depending on whether you want the skill available everywhere or only within a specific project.

**Option A: Install account-wide via Customize (recommended)**

This makes the skill available in all your conversations and in Cowork.

1. Download this repository as a ZIP file (on the repository's main page, click the green **Code** button, then **Download ZIP**).
2. Open [claude.ai](https://claude.ai). In the left sidebar, click **Customize** (the toolbox icon), then go to **Skills**.
3. Click the **+** button, then **+ Create skill**, and upload the ZIP file.
4. The skill will appear in your Skills list. Make sure its toggle is turned on.
5. Start any conversation and ask Claude to review your writing. For example:

   > Review the writing quality of my manuscript. Here is the Introduction section:
   >
   > [paste your text]

Claude will recognize that the request matches the skill, load it, and produce a structured review report with specific findings and suggested revisions. You can also upload your manuscript as a PDF or paste individual sections.

> **Note:** The ZIP file must contain the skill folder at the root level. If your ZIP contains `sciwrite/SKILL.md` (not just a loose `SKILL.md`), you're set.

**Option B: Add to a specific Project's knowledge base**

If you prefer to limit the skill to a particular project (for example, a project dedicated to a specific manuscript):

1. Download the `SKILL.md` file from this repository.
2. Open or create a **Project** in Claude.ai.
3. In the Project's knowledge base, click **Add content** and upload the `SKILL.md` file.
4. Start a conversation inside that Project and ask Claude to review your writing.

This approach keeps the skill scoped to one project, which is useful if you are working on multiple manuscripts with different conventions.

### In Claude Code (terminal agent)

Place `SKILL.md` in `.claude/skills/manuscript-review/` inside your manuscript project directory, then launch Claude Code and ask for a review. See [`HOW-TO-USE.md`](HOW-TO-USE.md) for full setup instructions, example prompts, and tips for each review mode.

### In Claude's Cowork (desktop agent)

If you installed the skill account-wide via Customize (Option A above), it is already available in Cowork—no additional setup needed.

If you prefer to work with the file directly, you can also place the `SKILL.md` file in the folder you point Cowork at (or in a subfolder). Then ask Cowork to review a manuscript file in that same folder:

   > Review the writing quality of the manuscript draft in this folder.

### In ChatGPT

Because OpenAI has adopted the Agent Skills standard, you can use this skill in ChatGPT through a Custom GPT:

1. Open the `SKILL.md` file and copy its full contents (everything below the closing `---` of the header).
2. Go to [chat.openai.com](https://chat.openai.com), click your profile icon, then **My GPTs** → **Create a GPT**.
3. In the **Configure** tab, paste the contents of the skill into the **Instructions** field. You may also want to add the YAML header's description text at the top so the GPT knows when to apply these instructions.
4. Name the GPT something like "SciWrite Reviewer" and save it.
5. Open the GPT and paste your manuscript text.

The output format and reasoning will follow the same structure as in Claude.

### In Google Gemini

Gemini does not yet natively support the SKILL.md format, but you can achieve a similar result using a **Gem** (Gemini's equivalent of a custom assistant):

1. Open [gemini.google.com](https://gemini.google.com) and navigate to **Gems** (in the left sidebar, or via the Gem manager).
2. Create a new Gem. In the instructions field, paste the full body of the `SKILL.md` file (everything after the YAML header).
3. Save the Gem and open a conversation with it.
4. Paste your manuscript text and ask for a writing review.

### General approach for any AI tool

If your preferred AI tool is not listed above, the pattern is the same:

1. Find the tool's mechanism for persistent instructions (custom assistants, system prompts, project instructions, or similar).
2. Paste the contents of `SKILL.md` into that mechanism.
3. Provide your manuscript text and ask for a review.

The skill is plain Markdown with no dependencies on any specific platform. It works wherever you can give an AI tool a block of instructions to follow.

## Tips for Getting Good Results

**Provide enough text for context.** A single isolated sentence is hard to review for keyword consistency or logical flow. A full section or chapter gives the skill enough material to identify patterns—repeated nominalizations, inconsistent terminology, or structural problems that span multiple paragraphs.

**Specify the review mode if you have a specific need.** If you already know your weakness is passive voice, ask for a targeted review rather than a full pass. This produces faster, more focused feedback.

**Use the interactive mode for learning.** The paragraph-by-paragraph mode shows before/after revisions with explanations — useful for building long-term writing habits, not just fixing a single draft.

**Name your target journal when reviewing an abstract.** The structural pass is venue-dependent in ways that matter. Nature caps a summary paragraph at roughly 200 words and requires it to be fully referenced; most other journals allow more words and forbid citations in the abstract outright. If you do not say where you are submitting, the skill applies Nature's defaults and tells you it has done so — so a 250-word abstract bound for a journal that permits 250 will be flagged for length until you say otherwise.

**Review the output critically.** The skill produces well-structured editorial feedback, but your domain expertise is the final quality check. Occasionally a "smothered verb" that the skill flags is actually the standard term in your field (e.g., "polymerization" is not a nominalization that needs fixing). Use your judgment. The same applies to the structural pass: whether a measurement is essential enough to keep in an abstract is a judgment call about what your result actually is, and the skill's suggestion is a prompt, not a verdict.

**Iterate.** If a suggested revision changes your intended meaning, tell the AI why and ask it to try again. The skill's structured reasoning means the AI can explain *why* it flagged a particular sentence, which makes it easy to have a productive back-and-forth.

## Customizing the Skill

The skill encodes general principles of scientific writing clarity. You can extend it with discipline-specific or journal-specific conventions. For example, if your target journal has specific style requirements, you could add a section like:

```markdown
## Journal-Specific Conventions

Target journal: Journal of Fluid Mechanics (JFM)
- Use "figure" (lowercase) in running text; "Figure" only at the start of a sentence.
- Equations are referenced as (1), not Eq. (1), unless at the start of a sentence.
- Use Oxford commas.
- Abbreviations must be defined at first use in the abstract AND again at first use in the body text.
```

You can also adjust the severity thresholds, add or remove entries from the clutter-phrase lookup table, or modify the review modes to match your workflow.

## Contributing

If you use this skill and find an edge case it doesn't handle well—a field-specific writing convention it misjudges, a common clutter pattern it misses, or a false positive that comes up repeatedly—contributions are welcome. Open an issue describing the case, or submit a pull request with your proposed change.

## License

This skill is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You are free to use, adapt, and share it, with attribution.

The source material—Dr. Kristin Sainani's *Writing in the Sciences* video lectures—is published under a [Creative Commons Attribution (CC-BY)](https://creativecommons.org/licenses/by/4.0/) license.

## Acknowledgments

Developed as part of the course [MAE 6291: Generative AI for Engineering Research](https://barbagroup.github.io/mae6291-genai/) at the George Washington University School of Engineering and Applied Science, and shared through the [GW Engineering AI Academy](https://www.seas.gwu.edu/ai-academy).

The writing methodology encoded in this skill is drawn from Dr. Kristin Sainani's [*Writing in the Sciences*](https://www.coursera.org/learn/sciwrite) course at Stanford University. The original video lectures are available on [YouTube](https://www.youtube.com/playlist?list=PLVc-QdfGfSl2Ntc6CvIP83Nj_uHTSdNSw) under a CC-BY license.

The summary paragraph structure encoded in the sixth pass follows Nature's guide to authors, ["How to construct a Nature summary paragraph"](https://www.nature.com/documents/nature-summary-paragraph.pdf) (September 2019), together with Nature's published formatting guidance for Articles. That document is the property of Springer Nature and is referenced here, not reproduced.

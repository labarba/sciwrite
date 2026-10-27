---
name: sciwrite
description: >
  Use this skill when asked to review, edit, or improve the writing quality of a
  scientific or engineering manuscript. Triggers include: "review my writing,"
  "check my manuscript," "improve clarity," "clean up the prose," "edit for
  journal submission," "writing review," or any request to evaluate sentence-level
  quality, eliminate clutter, fix passive voice, or enforce keyword consistency in
  a research paper draft. Also triggers on "review my abstract," "check my summary
  paragraph," "does my abstract follow Nature's structure," "is my abstract too
  long," or any request to evaluate whether an abstract states its result clearly,
  is structured correctly, or is readable outside the specialty. Also triggers when
  asked to prepare a manuscript for submission to a specific journal. Do NOT use for
  content/technical review of methods or results, statistical analysis, or citation
  formatting.
license: CC-BY-4.0
metadata:
  author: Lorena A. Barba
  version: "0.2.0-dev"
  source: Kristin Sainani, Writing in the Sciences (Stanford, CC-BY lectures)
  repository: https://github.com/labarba/sciwrite
---

# Manuscript Writing Review — Scientific Clarity and Precision

## Purpose

You are an expert scientific writing reviewer. Your goal is to transform cluttered
academic prose into clean, precise, powerful scientific communication. You apply
the principles of Dr. Kristin Sainani's "Writing in the Sciences" methodology:
every word must earn its place; every sentence must be stripped to its cleanest
components. For abstracts and summary paragraphs you also check structure, against
the sequence of rhetorical moves Nature prescribes for its summary paragraphs.

You do NOT alter scientific content, data, or technical claims. You improve how
those claims are delivered. This holds for structural review too: you verify that a
result statement exists, is marked, and sits in the right position — you do not
judge whether the result is the paper's most important finding, or whether the
comparison to prior work is fair. Those are content questions and belong to peer
review.

## Review Modes

When the user asks for a writing review, determine which mode to use:

| Mode | Trigger | What you do |
|------|---------|-------------|
| **full-review** | "review my manuscript," "full writing review" | Run all six audit passes on the entire document, produce a structured report |
| **section-review** | "review the Introduction," "check the Discussion" | Run Passes 1–5 on a single section; add Pass 6 if the section is the abstract |
| **targeted** | "fix passive voice," "clean up clutter" | Run only the relevant audit pass(es) |
| **interactive** | "walk me through improving this" | Go paragraph by paragraph, showing before/after with explanations |
| **abstract-review** | "review my abstract," "check my summary paragraph" | Run Pass 6, plus Passes 1, 2, and 4 scoped to the abstract |

Default to **full-review** if ambiguous.

## The Six Audit Passes

Apply these sequentially. Each pass focuses on one dimension of writing quality.

Passes 1–5 are independent dimensions — order among them does not change the
findings. Pass 6 is different: it evaluates the abstract as a whole against a
required rhetorical structure, and it runs **last**, after the sentence-level
passes have cleaned up the prose it is judging. Run Pass 6 whenever the document
includes an abstract or summary paragraph. In **abstract-review** mode, run it
together with Passes 1, 2, and 4, all scoped to the abstract.

**Abstracts need a reference file.** Whenever the text under review includes an
abstract or summary paragraph, and always in **abstract-review** mode, read
[references/summary-paragraph.md](references/summary-paragraph.md) before
starting the passes. It holds the Pass 6 procedure, adjustments to Passes 1–4
that apply only to abstracts (for example, which passive constructions to leave
alone), and the output format for abstracts.

### Pass 1: Clutter Extraction

Strip every sentence to its cleanest components. Flag and replace:

**Dead-weight phrases → concise replacements:**

| Cluttered phrase | Replace with |
|------------------|--------------|
| Due to the fact that | Because |
| A majority of | Most |
| Are of the same opinion | Agree |
| Give rise to | Cause |
| Have an effect on | Affect |
| In the event that | If |
| At the present time | Now / Currently |
| In order to | To |
| A number of | Several / Many |
| On the basis of | Based on |
| In light of the fact that | Because / Since |
| It is worth noting that | (delete — just state the point) |
| It is important to note that | (delete) |
| It is interesting to note that | (delete) |
| In terms of | (rewrite to be specific) |

**Dead-weight introductory phrases — flag for deletion:**

- "As it is well known..." → replace with a direct citation
- "It should be emphasized that..."
- "It can be regarded that..."
- "As it has been shown..."
- "It is noteworthy that..."

**Redundancy extraction:** remove adjectives or adverbs that repeat information
already carried by the noun or verb. Examples:

- "successful solutions" → "solutions" (success is inherent)
- "completely eliminate" → "eliminate"
- "future plans" → "plans"
- "unexpected surprise" → "surprise"
- "currently underway" → "underway"

### Pass 2: Active Voice and Verb Vitality

Scientific transparency requires accountability. Identify who did what.

**Passive → Active conversion protocol:**

1. Spot the pattern: "to-be" verb + past participle ("was observed," "were analyzed")
2. Identify the actor: Who performed the action? Default to "We" if the authors did it.
3. Reconstruct as Subject–Verb–Object.

Example:
- Passive: "The activation of channels is induced by the depletion of stores."
- Active: "Depleting stores activates channels."

**Nominalization ("smothered verbs") — resurrect the verb:**

| Smothered form | Resurrected verb |
|----------------|-----------------|
| Provides a review of | Reviews |
| Offers a confirmation of | Confirms |
| Shows a peak | Peaks |
| Obtains an estimate of | Estimates |
| Conducts an assessment of | Assesses |
| Provides a description of | Describes |
| Makes an adjustment to | Adjusts |
| Performs an analysis of | Analyzes |
| Achieves a reduction in | Reduces |

Flag every "noun + of" construction and check whether a direct verb exists.

**When passive voice is acceptable:**
- The actor is genuinely unknown or irrelevant ("The sample was collected in 2019")
- Standard methodological phrasing in Methods sections where journal style requires it
- Deliberate emphasis on the object over the actor

Do NOT mechanically convert every passive sentence. Flag the ones where the
passive obscures accountability or the actor.

### Pass 3: Sentence Architecture

**Buried predicate audit:** Count words between subject and main verb. If more
than ~12 words intervene, the predicate is buried. Recommend restructuring.

- Buried: "One study of 930 adults with MS receiving care in one of two
  managed care settings found that..."
- Fixed: "One study found that, among 930 adults with MS in managed care
  settings, ..."

**Punctuation for efficiency:**
- Use a **colon** to set up a list or specific explanation, replacing wordy openings
- Use a **dash (—)** for emphatic parentheticals or to merge sentences where a
  transition feels forced
- Use **semicolons** to link closely related independent clauses, reducing the
  need for transition words

**Sentence length variation:** Flag paragraphs where all sentences are roughly
the same length (±5 words). Recommend varying rhythm: short declarative sentences
for emphasis, longer ones for explanation.

### Pass 4: Keyword Consistency and Terminology

In scientific writing, terminological consistency is a virtue, not a defect.

**The Banana Rule:** Do not call a "banana" an "elongated yellow fruit" to avoid
repetition. If the Methods say "obese group," the Results must not switch to
"heavier group." Synonym variation for technical terms forces the reader to wonder
whether a new category has been introduced.

**Keyword consistency audit:**
1. Extract all key terms from the Methods (group names, variable names, technique
   names, abbreviations).
2. Verify that the exact same terms appear in the Abstract, Results, Discussion,
   Tables, and Figure captions.
3. Flag every instance where a synonym was substituted for a defined term.

The abstract is the highest-value target for this check. A term introduced in the
summary paragraph and then renamed in the body forces the reader to decide whether
two things are being described or one.

**Acronym austerity:**
- Flag non-standard acronyms created only for author convenience.
- Permit only universally recognized acronyms (DNA, RNA, CFD, FEM, PIV, etc.).
- Verify that every acronym is defined at first use in the Abstract AND in the
  main text AND in each Table/Figure legend (readers do not read linearly).

### Pass 5: Numerical Consistency and Citation Integrity

This pass checks whether numbers that appear are *correct and consistent*. Whether a
number *belongs* in the abstract at all is a separate question, handled by the
essentiality test in Pass 6. The two are complementary: a value can be perfectly
consistent with Table 1 and still be spending words the summary paragraph cannot
afford.

**Numerical consistency checklist:**
- Does the sample size (N) in the Abstract match Table 1?
- Do percentages in Results match the raw numbers in Tables?
- Are significant figures consistent and appropriate for the measurement precision?
- Do Figure graphics match the corresponding Table values? Run this check only
  when you can see the figures (as images or their underlying data). If you have
  only the text, say that you skipped it; do not guess what a figure shows.

**Citation integrity — the "Telephone Game" audit:**
Flag any statistic presented as established fact but cited only through secondary
sources (reviews, textbooks). Recommend the author verify the primary source.
Common pattern: "According to [Review, 2020], the prevalence is 15–62%..." — but
the original studies behind those numbers may have very different scopes.

### Pass 6: Summary Paragraph Structure

Run this pass last, after Passes 1–5 have cleaned up the prose. Passes 1–5 ask
whether each sentence is well built. This pass asks a prior question: whether the
right sentences are present, in the right order, doing the right work. A summary
paragraph in which every sentence is clear but the result is never stated is a
worse abstract than a cluttered one that says what the authors found.

Follow the six-step procedure in
[references/summary-paragraph.md](references/summary-paragraph.md).

## Output Format

### For full-review and section-review modes

Produce a structured report with this skeleton:

```
## Writing Quality Review: [Document/Section Title]

### Summary
[2–3 sentence overall assessment: dominant issues, overall clarity level]

### Pass 1: Clutter — [N issues found]
[List each instance with line/paragraph reference, original text, suggested revision,
and brief rationale]

### Pass 2: Voice and Verbs — [N issues found]
[Same format]

### Pass 3: Sentence Architecture — [N issues found]
[Same format]

### Pass 4: Terminology — [N issues found]
[Same format]

### Pass 5: Numbers and Citations — [N issues found]
[Same format]

### Pass 6: Summary Paragraph Structure — [N issues found]
[Active parameters: venue, word target, ceiling, citation policy]
[Move-tagged rendering — see references/summary-paragraph.md]
[Missing moves, out-of-order moves, budget overruns, non-essential numbers and
abbreviations, each with original text, suggested revision, rationale, severity]
[Accessibility notes — advisory, untagged]

### Top 5 Priority Revisions
[The five changes that would most improve the manuscript, ranked by impact]
```

### For interactive mode

Go paragraph by paragraph. For each:
1. Show the original paragraph
2. Show a revised version with the sentence-level passes (1–5) applied
3. Explain the key changes made and why

Wait for the user to confirm or adjust before proceeding to the next paragraph.

### For targeted mode

Run only the requested pass(es) and report in the same format as above, limited
to the relevant section(s).

### For abstract-review mode

Follow the output order in
[references/summary-paragraph.md](references/summary-paragraph.md).

## Severity Levels

Tag each finding with a severity:

- **CRITICAL** — Actively misleads the reader (wrong number, term inconsistency
  that implies a different variable, passive voice that hides important
  accountability), **or, in Pass 6, a required move that is missing entirely.**
  A missing move is CRITICAL even when every sentence present is clear, because the
  paragraph omits information the reader needs and no edit to the surviving text
  supplies it. The commonest instance is an abstract with no result statement: it
  describes what was studied and never says what was found, and it fails in front
  of an editor before it reaches a reviewer.
- **MAJOR** — Significantly impairs clarity (buried predicates, heavy nominalization,
  dense clutter). In Pass 6: moves present but out of sequence, word count over the
  active ceiling, a sentence budget missed by more than one, or a non-essential
  number or acronym in moves 1–3. These are ordering and proportion problems — the
  information is all there, and the fix is rearrangement or compression rather than
  new material.
- **MINOR** — Worth fixing but does not impede understanding (slight wordiness,
  optional style improvements). In Pass 6: a sentence budget missed by one.

Accessibility notes from Pass 6 Step 6 carry no severity tag. They are advisory and
are reported in their own subsection.

## Constraints

- **Never alter scientific content.** You improve delivery, not substance. If a
  claim seems wrong, flag it as a content note but do not change it.
- **Respect disciplinary conventions.** Some fields expect passive voice in Methods
  sections; some journals have specific style requirements. If the target journal
  is not specified, do not stop to ask: review against general conventions, say
  that you have done so, and invite the author to name the journal. This matters
  most in Pass 6, where the rules are venue-
  dependent in both directions: Nature requires the summary paragraph to be fully
  referenced, while most journals forbid citations in abstracts outright, and word
  limits vary widely. Applying one venue's rules to another produces confident,
  wrong advice. When the venue is unknown, use the defaults, state that you have
  done so, and flag venue-dependent items as conditional rather than as errors.
- **Preserve the author's voice.** The goal is clarity, not homogeneity. If a
  sentence is clear and effective despite breaking a "rule," leave it alone.
- **Be specific.** Every suggestion must include the original text and a concrete
  revision. Never say "consider improving clarity" without showing how.

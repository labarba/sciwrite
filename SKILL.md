---
name: manuscript-writing-review
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
includes an abstract or summary paragraph, and run it alone in **abstract-review**
mode.

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

**Abstract throat-clearing — flag for deletion.** A summary paragraph is under a
hard word budget and the reader already knows they are reading a paper. Openers
that announce the act of writing spend words that the result statement needs:

- "In this paper we present..." → state what you found
- "This study investigates..." → state what you found
- "The purpose of this work is to..." → state what you found
- "This paper is organized as follows..." → does not belong in an abstract

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

**The canonical form: "Here we show."** Nature requires that the main conclusion of
a summary paragraph be introduced by "Here we show" or its equivalent, and this is
the clearest available instance of what this pass is trying to produce: the authors
named as the actor, the finding stated as a direct object. The supporting forms in
the same register are "We found," "Our results demonstrate," and "We anticipate."
When reviewing an abstract, treat these as the target constructions rather than as
options.

**When passive voice is acceptable:**
- The actor is genuinely unknown or irrelevant ("The sample was collected in 2019")
- Standard methodological phrasing in Methods sections where journal style requires it
- Deliberate emphasis on the object over the actor
- **Field-level background statements**, where the actor is the discipline rather
  than the authors. The opening moves of a summary paragraph are legitimately
  passive: "mitotic spindles are assembled by motor proteins" describes settled
  knowledge, not something the authors did. Do not flag passive constructions in
  the introduction and background moves of an abstract; the voice should shift to
  first-person active at the result statement and stay there.

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

Do **not** apply this check to a summary paragraph. A well-formed abstract is a
compressed sequence of declaratives under a hard word budget; uniformity there is
the correct form, not a defect, and flagging it manufactures findings the author
should ignore.

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
- **In a summary paragraph, apply a stricter threshold.** Nature instructs authors
  to avoid abbreviations and acronyms unless essential, because the paragraph is
  written for readers outside the discipline. An acronym earns its place in an
  abstract only if spelling the term out would cost more words than the acronym
  saves, or if the acronym is more widely recognized than the expansion. Otherwise
  spell it out or cut the term. See Pass 6 for the essentiality test.

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
- Do Figure graphics match the corresponding Table values?

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

The reference structure is Nature's, which is prescriptive about both the sequence
of rhetorical moves and how many sentences each is allowed. Other venues differ in
budget but rarely in sequence — the funnel from general field to specific result and
back out to general significance is close to universal.

**Step 1 — Establish the active parameters.**

Ask the user for the target venue if it is not stated, and record the parameters at
the top of the report so the author can see what the findings are being measured
against. Defaults, if no venue is given:

| Parameter | Default | Notes |
|-----------|---------|-------|
| Word target | 200 | Nature's stated target for a summary paragraph |
| Word ceiling | 300 | Applies only when the broader-perspective move is present |
| Citations in summary | Permitted | Nature requires the summary be fully referenced; most other journals forbid citations in abstracts entirely — confirm before flagging either way |
| Numbers and units | Essential only | See Step 5 |
| Abbreviations | Essential only | See Pass 4 |

If the user names a different venue or a different limit, use theirs and say so in
the report header. Do not apply Nature's 200-word target to a journal that allows
250, and do not flag citations as an error in a venue that requires them.

**Step 2 — Segment the paragraph into moves.**

Assign every sentence to exactly one move. Sentences that fit no move are tagged
unassigned, which is itself a finding.

| # | Move | Budget | Required | Test |
|---|------|--------|----------|------|
| 1 | Field introduction | 1–2 sentences | Yes | Comprehensible to a scientist in any discipline |
| 2 | Detailed background | 2–3 sentences | Yes | Comprehensible to scientists in related disciplines |
| 3 | Problem statement | 1 sentence | Yes | States the general problem this study addresses |
| 4 | Main result | 1 sentence | Yes | Introduced by "Here we show" or equivalent |
| 5 | Result against prior belief | 2–3 sentences | Yes | Says what the result reveals relative to what was thought before |
| 6 | General context | 1–2 sentences | Yes | Places the result in a wider frame |
| 7 | Broader perspective | 2–3 sentences | Optional | Accessible to any scientist; presence raises the word ceiling |

**Step 3 — Check inventory and order.**

Report each required move that is absent, and each move that appears out of
sequence. These are the two failure modes that structural review exists to catch,
and they are distinct in both kind and severity: a missing move means the paragraph
does not contain a piece of information the reader needs, and is CRITICAL; a move
present but out of sequence means the information is all there in an order that
makes it harder to follow, and is MAJOR. An abstract can fail either way — all
seven moves scrambled, or five moves in perfect order — and the second is the more
serious problem, because no amount of reordering fixes a result that was never
stated.

Move 4 gets its own check because it is the one authors most often omit. Verify that
an explicit result-claim marker is present — "Here we show," "We found," "We
demonstrate," "We report." An abstract that describes what was studied but never
states what was found has no move 4, however many sentences sit in that position.

**Step 4 — Check budgets.**

Report per-move sentence counts against the budget table, and the total word count
against the active target. Over-budget moves usually indicate the background has
crowded out the result; under-budget moves usually indicate a move is nominally
present but doing no work.

**Step 5 — Apply the essentiality test to numbers, units, and abbreviations.**

Nature instructs authors to avoid numbers, abbreviations, acronyms, and measurements
unless essential. This is not a prohibition but a relevance filter, and the test is
whether the quantity *is itself the finding*.

- Passes: a measured rate that constitutes the result being reported, where the
  magnitude is the point and paraphrase would lose it.
- Fails: sample sizes, dimensionless-group values, tolerances, grid counts, p-values,
  and any number belonging to moves 1–3, where the reader outside the field cannot
  yet interpret it.

Flag every failing instance with a concrete revision that either cuts the number or
converts it to a qualitative statement.

**Step 6 — Accessibility approximation (advisory).**

Nature's requirement that moves 1–2 be comprehensible to a scientist in any
discipline cannot be verified mechanically, and this pass does not pretend to. What
it can do is surface the specific terms most likely to cost an outside reader:

- Technical nouns appearing in moves 1–2 that are not defined in the paragraph and
  are not general-science vocabulary.
- Terms whose first appearance anywhere in the paper is in the summary paragraph.
- Named methods, instruments, model systems, or governing equations used without
  a gloss.

Report these as **advisory notes**, not as severity-tagged findings. They are
prompts for the author's judgment — a term that reads as impenetrable jargon to one
reader is the standard name of the object under study to another, and the author is
better placed to decide. Say what an outside reader would likely stumble on and
why; do not assert that the paragraph fails.

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
[Move-tagged rendering — see below]
[Missing moves, out-of-order moves, budget overruns, non-essential numbers and
abbreviations, each with original text, suggested revision, rationale, severity]
[Accessibility notes — advisory, untagged]

### Top 5 Priority Revisions
[The five changes that would most improve the manuscript, ranked by impact]
```

### Move-tagged rendering (Pass 6 artifact)

Before listing Pass 6 findings, reproduce the summary paragraph with every sentence
prefixed by its assigned move. This makes the structure visible at a glance and lets
the author see a missing or misplaced move rather than only reading about it:

```
[1 Field intro]        During cell division, mitotic spindles are assembled by
                       microtubule-based motor proteins.
[2 Background]         The bipolar organization of spindles is essential for proper
                       segregation of chromosomes, and requires ...
[3 Problem]            However, the precise roles of kinesin-5 during this process
                       are unknown.
[4 Result ✓]           Here we show that the vertebrate kinesin-5 Eg5 drives the
                       sliding of microtubules ...
[5 vs prior belief]    We found in controlled in vitro assays that ...
[6 General context]    Our results demonstrate how members of the kinesin-5 family
                       are likely to function in mitosis ...
[7 Broader]            We anticipate our assay to be a starting point for ...
[— unassigned]         [any sentence that fits no move]

Moves present: 1 2 3 4 5 6 7 — in order
Sentence budget: 1/2 ✓  3/3 ✓  1/1 ✓  1/1 ✓  3/3 ✓  1/2 ✓  3/3 ✓
Word count: 250 (target 200; ceiling 300, move 7 present)
```

Mark move 4 with a check only when an explicit result-claim marker is present.

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

Lead with the active parameters and the move-tagged rendering, then report Pass 6
findings, then the abstract-scoped findings from Passes 1, 2, and 4. Structure comes
first because a missing move usually makes sentence-level edits to the surrounding
text moot — there is no point polishing a background move that needs to be cut to
make room for a result statement. Close with the accessibility notes.

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
  sections; some journals have specific style requirements. Ask about the target
  journal if not specified. This matters most in Pass 6, where the rules are venue-
  dependent in both directions: Nature requires the summary paragraph to be fully
  referenced, while most journals forbid citations in abstracts outright, and word
  limits vary widely. Applying one venue's rules to another produces confident,
  wrong advice. When the venue is unknown, use the defaults, state that you have
  done so, and flag venue-dependent items as conditional rather than as errors.
- **Preserve the author's voice.** The goal is clarity, not homogeneity. If a
  sentence is clear and effective despite breaking a "rule," leave it alone.
- **Be specific.** Every suggestion must include the original text and a concrete
  revision. Never say "consider improving clarity" without showing how.

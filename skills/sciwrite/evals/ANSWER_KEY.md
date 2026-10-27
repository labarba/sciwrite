# Answer key for the test passages

Every planted problem in the invented passages, with where it is, which pass
should catch it, and the severity the skill's rules assign. The assertions in
`evals.json` are written from this list. Tests 1–2 come from Sainani's lecture
1.4; their answer key is Sainani's own edits, recorded in `evals.json`.

The passages are invented. Their technical claims and reference [12] are
fictitious and are not meant to be checked.

## Test 3: `files/cavity.tex` (full review, LaTeX)

| # | Location | Planted problem | Pass | Expected severity |
|---|----------|-----------------|------|-------------------|
| 1 | Methods ¶1 | "In order to solve" → "To solve" | 1 Clutter | MINOR |
| 2 | Methods ¶1 | "Due to the fact that" → "Because" | 1 Clutter | MINOR |
| 3 | Methods ¶2 | Buried predicate: about 30 words between "A grid convergence study" and "was performed" | 3 Architecture | MAJOR |
| 4 | Results ¶1 | "It is worth noting that" → delete | 1 Clutter | MINOR |
| 5 | Results ¶1 | "high-resolution grid" renames the defined term "fine mesh" | 4 Terminology | MAJOR or CRITICAL |
| 6 | Results ¶1 | "We performed an analysis of" → "We analyzed" | 2 Verbs | MINOR |
| 7 | Results ¶1 | Text gives max deviation 2.1%; table shows 2.4% (u, 256 × 256) | 5 Numbers | CRITICAL |
| 8 | Results ¶1 | Fine mesh is 512 × 512 here, 256 × 256 in Methods and the table | 5 Numbers | CRITICAL |
| 9 | Results ¶1 | "SGS" is never defined (and is out of place in a laminar simulation; a content note at most) | 4 Terminology | MAJOR |

Also tested: the review must not change anything inside math, and must keep
`\cite`, `\citet`, `\ref`, `\eqref` and `\label` intact.

Not planted: "Re" is defined at first use; the passive "was compared" inside
the buried-predicate sentence goes away with the restructuring.

## Test 4: `files/arterial-stiffness.md` (full review)

| # | Location | Planted problem | Pass | Expected severity |
|---|----------|-----------------|------|-------------------|
| 1 | Abstract vs Methods | 96 adults in the Abstract; 92 (48 + 44) in Methods | 5 Numbers | CRITICAL |
| 2 | Abstract | "PWV" used without definition (defined only in Methods) | 4 Terminology | MAJOR |
| 3 | Methods | 15–62% prevalence cited only to a review [12] | 5 Citations | MAJOR |
| 4 | Results | 45 of 48 reported as 92%; correct value is 94% | 5 Numbers | CRITICAL |
| 5 | Results | "heavier participants" renames the defined "obese group" | 4 Terminology | CRITICAL (implies a different category) |

Decoys that should not be flagged as errors: 39 of 44 = 89% is correct; the
table agrees with the text; "Blood samples were collected after an overnight
fast" is an acceptable Methods passive (the actor doesn't matter).

## Test 5: abstract without a result (abstract review)

| # | Sentence | Planted problem | Pass | Expected severity |
|---|----------|-----------------|------|-------------------|
| 1 | — | No main-result statement ("Here we show" move missing) | 6 Structure | CRITICAL |
| 2 | — | No comparison with prior understanding | 6 Structure | CRITICAL (missing required move) |
| 3 | 2 | "In this paper we present" announces the paper | 1 Clutter (abstract) | MINOR or MAJOR |
| 4 | 4 | "This study investigates" announces the paper | 1 Clutter (abstract) | MINOR or MAJOR |
| 5 | 4 | Mass-flux range, mesh size (4.2 million cells) are not essential | 6 Essentiality | MAJOR |
| 6 | 5 | Number of configurations (36) is not essential | 6 Essentiality | MAJOR |
| 7 | 4 | "VOF" acronym not essential in an abstract | 4 / 6 | MAJOR |
| 8 | 6 | "The results are discussed in terms of their implications" says nothing | 6 Structure | (covered by #1) |

No venue is named, so the skill should state that it is applying its default
parameters. Any revision must not invent a result.

## Test 6: Discussion paragraph (targeted: passive voice and smothered verbs only)

| # | Phrase | Planted problem | Expected handling |
|---|--------|-----------------|-------------------|
| 1 | "It was found that" | Passive hides the authors | → "We found that" |
| 2 | "A comparison … was made" | Nominalization + passive | → "We compared …" |
| 3 | "it was concluded that" | Passive hides the authors | → "we concluded that" |
| 4 | "Performing a quantification of" | Nominalization | → "Quantifying" |

Decoys: "recrystallization" is a field term, not a smothered verb; "The
specimens were annealed in flowing argon" is an acceptable passive; "in order
to" is clutter but outside the requested pass, so a targeted review should not
report it.

## Test 7: clean control

Nothing is planted. The numbers are consistent: a performance factor of
(Nu/Nu₀)/(f/f₀)^(1/3) = 2.3 / 4.1^(1/3) = 1.44, reported as 1.4. "Re" is
defined at first use, the terms "ribbed channel", "smooth channel", "rib
pitch" and "Nusselt number" are used consistently, and every sentence has its
subject next to its verb. A good review reports no CRITICAL or MAJOR
findings and at most a few optional MINOR suggestions.

Revised in PR 4. The first version had three real problems that both baseline
reviews caught: "as the flow visualizations in Figure 6 show" credited a
visualization with showing a drop in heat transfer; "closest pitch" misused
"close" for a distance and never gave the value; and "the highest of the three
pitches" read as if 1.4 were a pitch. The revision names all three pitches,
cites Figure 6 only for the recirculation, and states the drop as a number.

## Test 8: `files/wind-farm-intro.md` (section review, two Introduction paragraphs)

| # | Location | Planted problem | Pass | Expected severity |
|---|----------|-----------------|------|-------------------|
| 1 | ¶1, sentence 1 | Opens with rows and land use; the paragraph is about wake costs, so there is no real topic sentence | 3 Paragraph | MAJOR |
| 2 | ¶1, sentence 2 | "There are several studies that have shown that" → "Several studies have shown that" | 1 Clutter | MINOR |
| 3 | ¶1, sentence 3 | "However" introduces a second cost of wakes, not a contrast | 3 Paragraph | MINOR or MAJOR |
| 4 | ¶1, sentence 4 | Offshore winds and installation costs are off-topic | 3 Paragraph | MAJOR |
| 5 | ¶1, sentence 5 | "was not considered important" → "was overlooked" | 1 Clutter | MINOR |
| 6 | ¶2, sentence 1 | Dangling modifier: "Using large-eddy simulation, the wake … was resolved" | 3 Sentence | MAJOR |
| 7 | ¶2, sentence 1 | Overloaded sentence: about 70 words and five ideas joined by "and", "but", "whereas", "which" | 3 Sentence | MAJOR |
| 8 | ¶2, sentence 2 | Vague "This motivates" | 3 Sentence | MINOR |

Decoys: "large-eddy simulation" and "velocity deficit" are field vocabulary;
"Here we simulate…" is a good closing sentence; the citations must stay intact.
The passive "was resolved" disappears when the dangling modifier is fixed.

## Test 9: `files/micromixer.md` (section review, Results and Discussion)

| # | Location | Planted problem | Pass | Expected severity |
|---|----------|-----------------|------|-------------------|
| 1 | Results, sentence 1 | Leads with "Figure 3 shows…" instead of the finding | 3 Section | MINOR or MAJOR |
| 2 | Results, sentence 3 | "This is because…" explains the mechanism: interpretation in Results | 3 Section | MINOR |
| 3 | Results, sentence 3 | Vague "This" | 3 Sentence | MINOR |
| 4 | Discussion, sentence 1 | Opens with methods, not the main finding | 3 Section | MAJOR |
| 5 | Discussion, sentence 2 | Repeats all six numbers from the Results | 3 Section | MAJOR or MINOR |
| 6 | Discussion, last sentence | "prove … optimal … all applications" claims more than the results show | Content note | (untagged or flagged; not rewritten silently) |
| 7 | Discussion | No limitations (e.g., the Reynolds-number range, the trade-off with pressure drop) | 3 Section | MAJOR |

Decoys: past tense in Results is correct; the comparison with Stroock et al.
is present and should stay; the pressure-drop ordering in the Results matches
the numbers.

# Baseline results (iteration 0)

Skill version 0.2.0-dev, as merged in PR #4 (commit 63a9740). Run on
2026-10-27 with Claude Code 2.1.296 and its default model, using
`tools/run_evals.py` and `tools/grade_evals.py`. Each output test ran once
per configuration; each trigger query ran three times. Grading was done by a
blind LLM judge and spot-checked by hand.

## Output tests

| Test | Skill loaded? | With skill | Without skill |
|------|---------------|------------|---------------|
| 1 Sainani: cancer biology | No | 3/9 | 3/9 |
| 2 Sainani: athletic activity | No | 5/7 | 5/7 |
| 3 Cavity flow, LaTeX | Yes | 8/10 | 8/10 |
| 4 Arterial stiffness | Yes | 7/7 | 4/7 |
| 5 Abstract with no result | Yes | 7/7 | 2/7 |
| 6 Passive voice only | No | 6/7 | 5/7 |
| 7 Clean control | Yes | 2/4 | 2/4 |

| | With skill | Without skill | Difference |
|---|---|---|---|
| Mean pass rate | 0.74 | 0.56 | +0.18 |
| Mean time | 69 s | 49 s | +20 s |
| Mean tokens | 74,000 | 42,000 | +33,000 |
| Mean cost | $0.20 | $0.14 | +$0.06 |

In tests 1, 2 and 6 the skill was available but not loaded, so those
with-skill runs are effectively baseline runs. Where it loaded, it made a clear
difference in tests 4 and 5.

## Trigger queries

| Set | Should trigger | Should not trigger | Total |
|-----|----------------|--------------------|-------|
| Train | 5/6 | 6/6 | 11/12 |
| Validation | 2/4 | 4/4 | 6/8 |

No false triggers. The misses are short or targeted requests and queries that
promise text or files the run did not have.

## Known flaws in the tests (follow-ups)

These are flaws in the tests, not in the skill. Fix them before relying on
comparisons with later iterations. Items 1–3 were fixed in PR 4, and test 3
gained two assertions on locations and content notes. Items 5 and 6 were
resolved in PR 8: with the new description, the skill loads in every test.

1. **Test 7 is not a clean control.** Both reviews rightly flagged "as the flow
   visualizations in Figure 6 show" (a visualization cannot show a drop in heat
   transfer), "closest pitch" (a pitch is a distance; and its value is never
   given), and "the highest of the three pitches" (reads as if 1.4 were a
   pitch). Rewrite the paragraph.
2. **Test 3, math assertion is wrong.** "Does not propose any change inside the
   equation environment or inline math" fails when the review correctly fixes
   `$512 \times 512$`. It should allow changes that correct a flagged number
   and forbid changes to the equation itself.
3. **Test 6, "We found" assertion is too narrow.** Both reviews deleted "It was
   found that" and started with the finding, which is arguably better. Accept
   either.
4. **Label-only assertions.** Assertions that require the word CRITICAL reward
   the skill's report format. Without the skill, test 4 caught both number
   errors under "fix first" but failed these assertions. Keep them, but mark
   them as format checks.
5. **Tests 1, 2 and 6 never measured the skill.** Add runs whose prompt asks
   for the skill explicitly, so its output quality can be measured separately
   from triggering.
6. **Three trigger queries are incomplete.** "is my abstract too long…
   pasting it below" and "Here's the discussion…" contain no text, and the
   wind-tunnel query names a file the run cannot read. Add the text.
7. **Test 8, two assertions are too narrow** (found in PR 6). The citation
   assertion fails when the review rightly cuts the off-topic sentence along
   with its citation [6]; it should require citations to stay intact in
   sentences that are kept or moved. The vague-"this" assertion fails when the
   review folds "This motivates the present study" into the next sentence,
   which is a valid fix; accept either.
8. **Test 7 control still has one real flaw** (found in PR 4): sentences 4
   and 5 don't say which Reynolds number "the highest value" and "15% lower"
   refer to. Reviews flag it as MAJOR in most runs.

## Observations for later work

- The skill is not loaded for sentence-level or single-pass requests with
  pasted text (tests 1, 2, 6). Address in the description work (PR 8).
- With the skill, the test 3 review changed the author's "center" to
  "centre". US vs UK spelling belongs in the gotchas (PR 5).
- The test 3 review reported 14 findings on two paragraphs, several of them
  content suggestions. Evidence for grouping and noise control (PR 4).
9. **Test 9 does not discriminate** (found in PR 7). It scores 9/9 with and
   without the skill: the model already knows the basic conventions for
   Results and Discussion sections. Make its planted problems subtler, or
   replace assertions that pass in both configurations.
10. **Test 8, positive-construction assertion conflicts with the skill.** The
    Pass 1 rule offers "not important" → "unimportant", but the assertion's
    examples ("overlooked", "ignored") led the grader to fail "unimportant".
    Align the two.

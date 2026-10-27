# SciWrite tests

These files test the skill. They are left out of the release zip.

| File | What it holds |
|------|---------------|
| `evals.json` | Output tests: a prompt, the expected result, and checkable assertions for each case |
| `ANSWER_KEY.md` | Every planted problem in the invented passages, with location, pass, and expected severity |
| `files/` | Input files for tests 3, 4, 8 and 9 |
| `trigger_train.json` | 12 queries (6 should trigger, 6 should not) used to improve the description |
| `trigger_validation.json` | 8 queries (4 and 4) held out to check that a new description generalizes |

## Output tests

- **Tests 1–2 (source fidelity):** two sentences from lecture 1.4 of Kristin
  Sainani's *Writing in the Sciences* (CC BY), scored against her own edits. The
  skill was built from this course, so these measure fidelity to the method, not
  performance on new text.
- **Tests 3–6, 8 and 9 (planted errors):** invented passages with known problems; see
  `ANSWER_KEY.md`. They also contain decoys that should not be flagged.
- **Test 7 (control):** a clean paragraph that measures false alarms.

Run each test twice, with and without the skill (or against the previous
version), and grade every assertion as pass or fail with quoted evidence. The
method follows the Agent Skills guide,
[Evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills).

## Trigger tests

Run each query three times and count how often the skill is loaded. A query
passes when the rate is above 0.5 for should-trigger queries and below 0.5 for
the others. Change the description only in response to failures in the train
set; use the validation set to check the result. See
[Optimizing skill descriptions](https://agentskills.io/skill-creation/optimizing-descriptions).
The "near miss" queries share vocabulary with the skill but need something else.

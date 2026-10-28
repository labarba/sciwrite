# Changelog

All notable changes to the SciWrite skill are recorded here.
Versions follow [Semantic Versioning](https://semver.org/). While the version
is 0.x, any release may include breaking changes.

## [Unreleased] — 0.2.0

### Changed
- README rewritten with install steps checked in October 2026 for Claude
  (web, desktop, Cowork), Claude Code (one-step plugin install), ChatGPT and
  the Gemini app (native skill upload, replacing the Custom GPT and Gem
  workarounds), and coding agents through `gh skill install` and
  `npx skills add`. Tools without skill support get instructions to paste
  all three skill files. The description of the passes matches the current
  skill.
- Moved "How This Skill Was Made" from the README to `HISTORY.md`, with a new
  section on the version 0.2 revision. Fixed the broken Comet link.
- Rewrote the description around what users ask for rather than a list of
  trigger phrases: it now covers requests of any length, down to a single
  pasted sentence, and names abstracts explicitly. On the trigger queries,
  the skill now loads for 16/16 training and 10/10 validation queries
  (before: 14/16 and 8/10), with no false triggers in either set.
- Trimmed `SKILL.md` from 500 to 477 lines by moving the Pass 6 severity
  rules, the Pass 6 report contents, and abstract-only caveats into
  `references/summary-paragraph.md`.
- Trigger queries: completed three that promised text the run never had, and
  added short pasted excerpts (and near misses) to both sets.
- Section-specific guidance in `references/section-guidance.md`, read in full
  and section reviews: what the Introduction, Methods, Results and Discussion
  must each do (the Introduction's funnel to a stated gap; Results that lead
  with findings and leave interpretation out; a Discussion that opens with the
  main finding, compares with previous work, states limitations, and treats
  overreach as a content note). Findings are reported under Pass 3. New test
  9 covers Results and Discussion.
- Paragraph-level checks. Pass 3 is now "Sentence and Paragraph
  Architecture": it adds overloaded sentences, dangling and misplaced
  modifiers, vague "this", and paragraph structure (one main idea, topic
  sentence, logical flow, transitions that fit the logic). Pass 1 adds empty
  "There is/are … that" openers and negative constructions. The paragraph
  checks are skipped for abstracts, where Pass 6 judges structure. New test 8
  covers these checks.
- New "Gotchas" section: leave math, citation and reference commands, and
  markup intact in source files; never change the strength of a claim or
  invent results, numbers or citations; keep the author's spelling variety;
  treat field vocabulary as vocabulary, not jargon; do not edit the manuscript
  unless asked; run the terminology and numbers passes across the whole
  document. Test 3 gains an assertion on US spelling.
- Less noisy reports. Repeated problems are grouped into one finding with a
  count; MINOR findings collapse into a one-line "Minor edits" list; every
  finding gives a location; suggestions about content go under "Content notes"
  instead of the severity scale; passes with nothing to report are left out.
  Added an example of a full finding and a grouped one.
- Field-dependent rules softened: "noun + of" constructions are flagged only
  when the verb is shorter and clearer, and established technical terms are
  left alone; acceptable acronyms depend on the readership; undefined
  acronyms in legends are MINOR; the sentence-length check needs four or more
  similar sentences.
- Fixed three test flaws found in the baseline: rewrote the control
  paragraph (test 7) and loosened two over-narrow assertions (tests 3 and 6).
- Moved everything specific to abstracts into
  `references/summary-paragraph.md`: the Pass 6 procedure, the
  abstract-only adjustments to Passes 1–4, the move-tagged example, and the
  abstract-review output order. `SKILL.md` tells the agent to read it whenever
  an abstract is under review. The wording is unchanged; `SKILL.md` drops from
  484 to 332 lines.
- Resolved three contradictions in the instructions. `abstract-review` runs
  Pass 6 together with Passes 1, 2, and 4 (it no longer also says "alone").
  When no journal is named, the skill reviews against default conventions and
  says so instead of stopping to ask. The figure-versus-table check runs only
  when the figures are visible.
- Renamed the skill from `manuscript-writing-review` to `sciwrite`, so the
  `name` field matches its folder as the Agent Skills spec requires.
  Existing installs under the old name must be removed and reinstalled.
- Moved `SKILL.md` to `skills/sciwrite/SKILL.md`.
- Merged `HOW-TO-USE.md` into the README.

### Added
- Test set in `skills/sciwrite/evals/`: seven output tests (two from
  Sainani's lecture 1.4, four invented passages with planted errors and an
  answer key, one control), 20 trigger queries split into train and
  validation sets, and the baseline results in `BASELINE.md`.
- `tools/run_evals.py` and `tools/grade_evals.py` to run the tests through
  `claude -p` and grade them with a blind LLM judge.
- Pass 6, Summary Paragraph Structure, and a new `abstract-review` mode.
  Pass 6 checks an abstract against the sequence of rhetorical moves in
  Nature's summary-paragraph guide, with sentence budgets, an essentiality
  test for numbers and acronyms, and advisory accessibility notes.
  Contributed by [Kyle Niemeyer](https://github.com/kyleniemeyer) in
  [#3](https://github.com/labarba/sciwrite/pull/3).
- `license` and `metadata` (author, version, source, repository) in the
  SKILL.md frontmatter.
- Claude Code plugin and marketplace manifests in `.claude-plugin/`.
- GitHub Actions workflow that validates the skill with `skills-ref` and
  attaches a ready-to-upload zip to each tagged release.
- `CITATION.cff`.

## 0.1.0 — 2026-08-03

- First tagged release, an early draft: five audit passes, four review modes.

# Changelog

All notable changes to the SciWrite skill are recorded here.
Versions follow [Semantic Versioning](https://semver.org/). While the version
is 0.x, any release may include breaking changes.

## [Unreleased] — 0.2.0

### Changed
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

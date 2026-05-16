# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v1.1.0] - 2026-05-16

### Features

- feat(ci): add automated release pipeline and mypy enforcement (3029eed)
- feat: .python-version file added (0b4dfd0)
- feat: better readme (5f25b81)
- feat: added new section to readme: production (2f89811)
- feat: added new dev dependency ruff (5309de6)

### Bug fixes

- fix: redirect egg-info to project root to prevent it from being generated inside src/ (bc1b512)
- fix: better tests (b1e13a8)
- fix: title app (af99d9d)
- fix: better name boilerplate (8e24b43)
- fix: env name prev name project to new (f3e36a5)
- fix: better repository name/description and better system test (735742d)
- fix: correct minor code quality issues across codebase                                                                                                                                                                                                                                                                     - Fix mock_keys fixture return type hint to type[MockKeys]                                                                                                                                                                                                        - Fix _gravity type annotation from int to float in PlayerModel   - Guard player property against empty sprite group (returns None)                                                                                                                                                                                                 - Rename default logger name from "tkinter-app" to "pygame-app"                                                                                                                                                                                                   - Narrow exception catch from Exception to AttributeError in resource_path                                                                                                                                                                                        - Remove irrelevant migrations exclude from pre-commit ruff hooks (046cabc)

### Refactors

- refactor: replace pip install -r with pip install -e for build, dev and test deps (0f3619c)
- refactor: migrate to feature-based architecture and apply audit fixes (8a3d43a)

### Uncategorized

- patch: pyproject.toml update description (c8f59ad)
- patch: readme updated (d72ee0e)
- initial commit (cb57a27)
- Initial commit (e921e2d)


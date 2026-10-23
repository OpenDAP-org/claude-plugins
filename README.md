# Claude Plugins

Claude Code plugin marketplace for OpenDAP repositories.

Every OpenDAP repository enables the `opendap` plugin in its `.claude/settings.json`. Claude Code offers to install it the first time you trust the repository folder.

## Plugins

- `opendap`: project conventions.
  - `/opendap:requirement` records a requirement in `docs/requirements/`.
  - `/opendap:adr` records a decision in `docs/adr/`.
  - `/opendap:license-check` checks REUSE licensing.
  - `/opendap:fab-package` builds a KiCad project's fab and assembly package locally.
  - `/opendap:release` tags a revision and publishes a GitHub Release (manual only).
  - `/opendap:drc-rules` creates fab design rules with a test board.
  - `/opendap:export` generates a component's `export/` folder.
  - `/opendap:security-check` runs the weekly Blackbird OS security check.
  - A `SessionStart` hook reminds when the weekly security check is due.
  - A `PreToolUse` hook blocks `git commit --no-verify` and commits in clones without `pre-commit install`.

## Install manually

```sh
claude plugin marketplace add opendap-project/claude-plugins
claude plugin install opendap@opendap
```

## License

This repository follows the [REUSE](https://reuse.software) layout: license texts live in `LICENSES/` and `REUSE.toml` maps each path to its license.

- Default: **GNU GPL v3.0 or later** (`GPL-3.0-or-later`)
- Markdown files (including skills): **Creative Commons Attribution-ShareAlike 4.0** (`CC-BY-SA-4.0`)

Copyright © 2026 The OpenDAP Project.

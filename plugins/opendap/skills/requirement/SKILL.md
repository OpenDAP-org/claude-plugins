---
name: requirement
description: Add or update a requirement in an OpenDAP repository's docs/requirements/README.md. Use when the maintainers states something the project must or should achieve.
---

# Record a requirement

Requirements live in `docs/requirements/README.md` of the repository they belong to, as one table:

| ID | Requirement | Priority | Status |
|---|---|---|---|

1. **Pick the repository.** A requirement goes where it is implemented: product-level requirements and interfaces between components in `t1`, the physical case in `case`, electronics in `board`, the HAT interface in `hat-standard`, and so on. If it spans repositories, record it in each one, scoped to that repository.
2. **Only confirmed content.** Record what the maintainers stated. Do not add inferred details, numbers or wording. If something is needed but not stated, add it under `## Open questions` instead.
3. **ID.** Use the repository prefix already in the file (for example `BRD`, `CASE`, `HCS`) and the next free number, zero-padded to three digits. Never reuse or renumber an ID; mark a dropped requirement `Withdrawn` instead of deleting it, and one that belongs elsewhere `Moved` (with its new ID).
4. **Wording.** One testable statement. Use "shall" for **must** and "should" for **should**.
5. **Status.** `Confirmed` when agreed; `Draft` when the intent is agreed but the detail is still open.
6. If the file or the `docs/requirements/` folder does not exist, create it with the heading `# <Project> requirements`, a one-line intro and the table above, and link it from `docs/README.md`.
7. Context that is not a requirement (ideas, open options, background) goes under `## Context` in the same file.
8. Write in English.

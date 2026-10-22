---
name: drc-rules
description: Create or update a KiCad design-rule set (.kicad_dru) for a fab and process in kicad-lib/design-rules/, with a test board that triggers every rule. Use when a board needs rules no existing set covers, such as HDI with microvias or flex.
---

# Create fab design rules

Rule sets live in the `kicad-lib` repository under `design-rules/<fab>-<process>/`. Vendored upstream sets under `design-rules/vendor/` are never edited.

1. Get the fab's published capability page for the process (for example PCBWay HDI or flex). Record its URL and the date read. Every number in the rules must come from it; if a value is missing, list it as an open question instead of guessing.
2. Write the capabilities as a TOML file in the same shape as `design-rules/vendor/kicad-druid/capabilities/*.toml`, and generate the `.kicad_dru` with the vendored `tools/generate_dru.py` where it supports the rules; write the rest by hand in KiCad 10 custom-rule syntax.
3. Build a test board (`<fab>-<process>.kicad_pro/.kicad_pcb/.kicad_sch`) with one passing and one failing case per rule.
4. Verify with KiCad 10: `kicad-cli pcb drc --format json --severity-all` on the test board must report every rule by name, and only on the failing cases.
5. Add a `README.md` in the rule folder: source URL, date read, process, layer count, and what the rules do not cover.

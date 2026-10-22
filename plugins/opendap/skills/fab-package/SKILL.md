---
name: fab-package
description: Build the fab and assembly package (Gerbers, drill, pick-and-place, PCBWay-style BOM, Interactive HTML BOM, schematic and assembly PDFs, STEP, IPC-2581) for a KiCad project, locally. Use before ordering boards or attaching a release.
---

# Build a fab package

Everything runs on the local machine. There is no CI.

1. Find the KiCad project (`*.kicad_pro`) the user means. If there are several, ask.
2. Find the toolkit: `public/toolkit` in the OpenDAP workspace, or `$OPENDAP_TOOLKIT`. Its version must be the one pinned in the repository's `.pre-commit-config.yaml`.
3. Make sure the project uses the right fab rules: a `<project>.kicad_dru` copied from `kicad-lib/design-rules/` for the target fab and process. If none is present, stop and ask which fab and process.
4. Run:

   ```sh
   <toolkit>/tools/fab-package.sh <project>.kicad_pro
   ```

   The script runs ERC and DRC first and stops on errors. Never pass `--skip-checks` unless the user explicitly asks; a skipped package is marked `UNCHECKED`.
5. Report the package folder (`<project>/fab/<name>-<revision>/`), its `MANIFEST.txt`, and every warning. Missing Manufacturer or MPN fields block PCBWay turn-key assembly; list the affected designators.
6. Never commit `fab/`. Packages are attached to releases with `/opendap:release`.

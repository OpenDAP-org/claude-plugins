---
name: release
description: Tag a hardware revision and publish a GitHub Release with its fab packages and exports, from the local machine. Use when the user wants to release, order or freeze a board or component revision.
disable-model-invocation: true
---

# Release a revision

A release is outward-facing: confirm the tag name, the repository and the attached files with the user before creating or pushing anything.

1. The working tree must be clean and on the commit to release; local checks must pass (`pre-commit run --all-files`).
2. Ask the user for the tag. Do not invent a versioning scheme.
3. For each KiCad project in the repository, build its package with `/opendap:fab-package` at that commit, then zip each package folder.
4. If the repository has an `export/` folder, regenerate it with `/opendap:export` and commit it before tagging.
5. After the user confirms: create an annotated tag, push it, and create the release:

   ```sh
   git tag -a <tag> -m "<summary>"
   git push origin <tag>
   gh release create <tag> <package zips…> --title "<tag>" --notes "<what changed>"
   ```

6. Report the release URL.

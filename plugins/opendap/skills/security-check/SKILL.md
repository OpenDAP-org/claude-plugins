---
name: security-check
description: Run the weekly OpenDAP OS security check, comparing the last built image's packages with Debian's security, updates and backports archives. Use when the SessionStart reminder says it is due, or before a release.
---

# Weekly security check

There is no CI, so this check runs by hand, at least weekly.

1. From the OpenDAP workspace, run `public/opendap-os/build/security-check.py`. It reads the last image manifest and records the run in `.state/security-check`.
   - No manifest yet: build an image first with `public/opendap-os/build/dap-image.sh`.
2. Report the result to the user: up to date, or the list of packages with newer versions and the archive they come from (security, updates, backports).
3. If there are security updates, offer to rebuild the image (`dap-image.sh`) and, when a release is affected, to prepare a new one with `/opendap:release`. Do not rebuild or release without the user's confirmation.

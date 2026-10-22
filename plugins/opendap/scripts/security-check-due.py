#!/usr/bin/env python3
"""SessionStart hook: remind Claude when the weekly DAP OS security check is due.

Looks for the OpenDAP workspace above the session directory (the folder holding repos.tsv)
and its state file .state/security-check, written by dap-os/build/security-check.py.
"""
import json, os, sys, time

INTERVAL_DAYS = 7
data = json.load(sys.stdin) if not sys.stdin.isatty() else {}
d = os.path.abspath(data.get("cwd") or os.getcwd())
while d != os.path.dirname(d) and not os.path.exists(os.path.join(d, "repos.tsv")):
    d = os.path.dirname(d)
if not os.path.exists(os.path.join(d, "repos.tsv")) or not os.path.isdir(os.path.join(d, "public", "dap-os")):
    sys.exit(0)  # not inside the OpenDAP workspace
state = os.path.join(d, ".state", "security-check")
try:
    last = int(open(state).readline())
except (OSError, ValueError):
    last = 0
age_days = (time.time() - last) / 86400
if age_days >= INTERVAL_DAYS:
    when = "never" if not last else f"{int(age_days)} days ago"
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext":
        f"OpenDAP: the weekly DAP OS security check is due (last run: {when}). "
        "Tell the user and offer to run /opendap:security-check."}}))

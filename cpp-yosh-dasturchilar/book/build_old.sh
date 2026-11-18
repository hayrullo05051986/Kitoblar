#!/bin/bash
cd /home/claude/book
S=$(ls /root/.claude/skills/synced/*/docx/scripts/office/soffice.py|head -1)
mkdir -p oldout
for i in 1 2 3 4 5; do
  [ -f tocpages.json ] && cp tocpages.json prev.json
  node build.js oldout/old.docx >/dev/null
  (cd oldout && timeout 400 python3 $S --headless --convert-to pdf old.docx >/dev/null 2>&1)
  python3 findpages.py oldout/old.pdf | tail -1
  cmp -s prev.json tocpages.json && { echo STABLE; break; }
done

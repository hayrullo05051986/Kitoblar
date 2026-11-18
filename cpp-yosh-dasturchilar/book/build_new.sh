#!/bin/bash
cd /home/claude/book
export ALIFBO=new SRC=merged_new
S=$(ls /root/.claude/skills/synced/*/docx/scripts/office/soffice.py|head -1)

mkdir -p newout
for i in 1 2 3 4 5; do
  [ -f tocpages_new.json ] && cp tocpages_new.json prev_new.json
  node build.js newout/new.docx >/dev/null
  (cd newout && timeout 400 python3 $S --headless --convert-to pdf new.docx >/dev/null 2>&1)
  python3 findpages.py newout/new.pdf _new | tail -1
  [ -f prev_new.json ] && cmp -s prev_new.json tocpages_new.json && { echo STABLE; break; }
done

#!/bin/bash
cd /home/claude/book
export ALIFBO=new IMG_OUT=/home/claude/book/img_new
for f in banners.py img_cover.py img_m1_5.py img_m6_9.py img_m10_11.py img_algo.py comics_m1_5.py comics_m6_7.py comics_m8_9.py img_m12_13.py; do python3 $f >/dev/null 2>&1 || echo FAIL $f; done

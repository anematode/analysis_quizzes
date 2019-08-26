#!/bin/bash

command -v pdfunite >/dev/null 2>&1 || { echo >&2 "pdfunite is required to run this program; you can install it using poppler. Aborting."; exit 1; }

python assemble.py blanked blanked_assembled

(cd blanked_assembled; exec ../organize_quizzes.sh)

# Takes in a folder of individual quiz PDFs and assembles them into a single pdf

# Given a folder and destination folder (as arguments), it does the following:
# 1. Find all quizzes that are in there.
# 2. Assemble the quizzes into PDFs, then put the resulting PDFs in the destination folder.

import sys
import os
import re

quiz_regex = re.compile("^([a-zA-Z0-9_]+)_[0-9]+\.pdf$")

quiz_folder = sys.argv[1]
dest_folder = sys.argv[2]

for folder in [quiz_folder, dest_folder]: # Ensure they're folders
    if not os.path.isdir(folder):
        raise ValueError("%s doesn't exist or isn't a folder." % folder)

quiz_names = set()  # keeps track of quizzes seen

for filename in os.listdir(quiz_folder):
    regex_result = quiz_regex.match(filename)

    if regex_result:
        quiz_name = regex_result.group(1)  # the quiz name
        quiz_names.add(quiz_name)
    else:
        continue

qf_path = os.path.abspath(quiz_folder)
df_path = os.path.abspath(dest_folder)

for quiz_name in quiz_names:  # for every quiz
    print("Assembling quiz/test %s...." % quiz_name)

    os.system("pdfunite %s_?.pdf %s.pdf" % (qf_path + '/' + quiz_name, df_path + '/' + quiz_name))  # unites the PDFs

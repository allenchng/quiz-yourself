# Copyright 2018 Allen Chang

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ==============================================================================

"""Presents data science interview questions"""

import pandas as pd
import os
import random
import itertools
import argparse
import sys

from random import shuffle

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--num_questions", help="number of questions per category")
    args = parser.parse_args()

    if args.num_questions:
        num_questions = args.num_questions

    path = sys.path[0]  # detects path based on where script was launched
    questions_dir = path + '/questions'

    filelist = []
    for file in os.listdir(str(questions_dir)):
        if file.endswith(".csv"):
            filelist.append(os.path.join(str(questions_dir), file))

    random.shuffle(filelist)

    questions = []

    for i in filelist:
        file = pd.read_csv(i, header=None, usecols=[0], sep=';')
        file_list = file[0].tolist()

        question_indices = random.sample(range(0, len(file_list)), int(num_questions))
        question_list = [file_list[i] for i in question_indices]
        questions.append(question_list)

    flattened_list  = list(itertools.chain(*questions))

    question_iterator = iter(flattened_list)
    for i in question_iterator:
        print(i)
        input("Press Enter to continue...")

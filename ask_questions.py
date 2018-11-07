import pandas as pd
import os
import random
import itertools
import argparse

from random import shuffle

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", help="directory where script is stored")
    args = parser.parse_args()

    if args.dir:
        path = args.dir

    filelist = []
    for file in os.listdir(str(path)):
        if file.endswith(".csv"):
            filelist.append(os.path.join(str(path), file))

    random.shuffle(filelist)

    questions = []

    for i in filelist:
        file = pd.read_csv(i, header=None, usecols=[0], sep=';')
        file_list = file[0].tolist()

        question_indices = random.sample(range(0, len(file_list)), 5)
        question_list = [file_list[i] for i in question_indices]
        questions.append(question_list)

    flattened_list  = list(itertools.chain(*questions))

    question_iterator = iter(flattened_list)
    for i in question_iterator:
        print(i)
        input("Press Enter to continue...")

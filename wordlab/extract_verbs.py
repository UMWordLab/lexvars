"""
Loads verbs in a file and search for corresponding
probabilities in lexvars
Created by Yizhi Tang
"""

import pandas as pd
import numpy as np



def load_data(fname):
    """
    Reads in a csv file and return one column of a dataframe.
    A dataframe df is similar to dictionary.
    You can access the label by calling dataframe['Verb Token']
    """
    return pd.read_csv(fname)


def main():
    """
    Read from Summary_Stats_Decl.csv a list of verbs.
    Extract probabilities of each word from resources in lexvars repo
    """

    # Load all verbs and remove duplicates
    verb_file = "Summary_Stats_Decl.csv"
    all_verbs = load_data(verb_file)['Verb Token'].drop_duplicates()
    # Load all probabilities
    probability_file = "lex-lrec3.csv"
    all_prob = load_data(probability_file)

    # Loop through and extract probabilities
    verb_frames = []
    verb_keys = []
    for verb in all_verbs:
        # Use pandas library "smart indexing"
        verb_frames.append(all_prob[all_prob['verb'] == verb])
        # Use keys for quick access in the future
        verb_keys.append(verb)
    # ignore_index=True set up an ordered index
    # and ignore the index of probabilties in original
    result = pd.concat(verb_frames, keys=verb_keys, ignore_index=True)
    #print(result)
    result.to_csv("result.csv")



if __name__ == '__main__':
    main()

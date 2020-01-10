from typing import List, Any

import numpy as np

s = "I wrote some text about it"

def reshuffle(s):
    """
    Making letters in words shuffled
    :param s: a sentence
    :return: sentence with letters in words in other order
    """
    l = s.split(" ")
    out_string = []

    for i in l:
        if len(i) < 4:  # short words
            out_string.append(i)
        else:           # long words
            li = list(i)
            li_toreshuffle = li[1:-1]
            np.random.shuffle(li_toreshuffle)
            li_output = li[0]
            li_output = li_output + "".join(li_toreshuffle)
            li_output = li_output + li[-1]
            out_string.append("".join(li_output))
    return " ".join(out_string)

print(reshuffle(s))
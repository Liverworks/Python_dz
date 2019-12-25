import numpy as np

s = "I wrote some text about it"

l = s.split(" ")
ol = []

for i in l:
    if len(i) < 4:  # short words
        ol.append(i)
    else:           # long words
        li = list(i)
        lir = li[1:-1]
        np.random.shuffle(lir)
        lio = li[0]
        lio = lio + "".join(lir)
        lio = lio + li[-1]
        ol.append("".join(lio))

print(" ".join(ol))
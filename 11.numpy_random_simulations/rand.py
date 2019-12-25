import random
import numpy as np
import time
import seaborn as sns
import matplotlib.pyplot as plt

ln = []
lr = []
for i in range(1, 200):
    start = time.time()     # numpy random
    np.random.random(i)
    stop = time.time()
    ln.append(stop - start)

    start = time.time()     # random
    for a in range(1, i):
        random.random()
    stop = time.time()
    lr.append(stop - start)

gr = sns.lineplot(x=range(1, 200), y=lr)
sns.lineplot(x=range(1, 200), y=ln)
gr.set(xlabel = "number", ylabel = "time")
plt.title("Blue - random, orange - np")
plt.show()


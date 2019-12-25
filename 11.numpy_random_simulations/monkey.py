import time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def issort(l) -> object:
    """
    Checking if the list of numbers is sorted
    :param l: a list of numbers
    :return: bool
    """
    for i in range(1, len(l)):
        if l[i - 1] > l[i]:
            return False
    return True


times = []

for i in range(1, 10):  # list length
    for a in range(5):  # repeats
        l = np.random.randint(0, 50, i)
        start = time.time()
        while issort(l) == False:
            np.random.shuffle(l)
        stop = time.time()
        times.append((stop - start, i))


times = np.array(times, dtype=[("time", "float"), ("len", "float")])
gr = sns.lineplot(x=times["len"], y=times["time"])
gr.set(xlabel="len", ylabel="time")
plt.title("Monkey sort time")
plt.show()

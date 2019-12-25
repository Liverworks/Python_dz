import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x = y = 0
xy = [(0, 0)]

for i in range(30): # 30 steps
    l = np.random.randint(0, 4, 1)  # direction
    if l == 0:
        x += 1
    elif l == 1:
        y += 1
    elif l == 2:
        x -= 1
    else:
        y -= 1
    xy.append((x, y))

xy = np.array(xy, dtype=[("x", "int"), ("y", "int")])

gr = sns.scatterplot(x=xy['x'], y=xy['y'])
plt.title("random walk")
plt.show()
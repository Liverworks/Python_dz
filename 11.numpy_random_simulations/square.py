import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x1 = 0      # coordinates of vertexes and side middles of the square
y1 = 0
x2 = 1
y2 = 0
x3 = 1
y3 = 1
x4 = 0
y4 = 1
x5 = 0.5
y5 = 0
x6 = 1
y6 = 0.5
x7 = 0.5
y7 = 1
x8 = 0
y8 = 0.5
xy = []

x, y = np.random.random(2)
x0, y0 = np.random.random(2)

for i in range(10000):

    choise = np.random.randint(0, 8, 1)
    if choise == 0:
        xc = (x + 2 * x1) / 3
        yc = (y + 2 * y1) / 3
    elif choise == 1:
        xc = (x + 2 * x2) / 3
        yc = (y + 2 * y2) / 3
    elif choise == 2:
        xc = (x + 2 * x3) / 3
        yc = (y + 2 * y3) / 3
    elif choise == 3:
        xc = (x + 2 * x4) / 3
        yc = (y + 2 * y4) / 3
    elif choise == 4:
        xc = (x + 2 * x5) / 3
        yc = (y + 2 * y5) / 3
    elif choise == 5:
        xc = (x + 2 * x6) / 3
        yc = (y + 2 * y6) / 3
    elif choise == 6:
        xc = (x + 2 * x7) / 3
        yc = (y + 2 * y7) / 3
    else:
        xc = (x + 2 * x8) / 3
        yc = (y + 2 * y8) / 3

    x, y = x0, y0
    x0, y0 = xc, yc
    xy.append((xc, yc))

xy = np.array(xy, dtype=[("x", "float"), ("y", "float")])


gr = sns.scatterplot(x=xy['x'], y=xy['y'], s = 10)
plt.title("Sierpinski carpet")
plt.show()

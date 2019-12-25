import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x1 = 0
y1 = 0
x2 = 1
y2 = 0
x3 = 0.5
y3 = 0.866025404
xy = []

def rand_coord(x1=0, y1=0, x2=1, y2=0, x3=0.5, y3=0.866025404):
    """
    Making a random point inside a triangle
    :param x1 -- y3: triangle vertex coordinates
    :return: two coordinates of a point inside
    """
    x0 = np.random.random(1)
    y0 = np.random.uniform(0, y3, 1)
    if ((abs((x1 - x0)*(y2 - y1) - (x2 - x1)*(y1 - y0)) +
        abs((x2 - x0)*(y3 - y2) - (x3 - x2)*(y2 - y0)) +
        abs((x3 - x0)*(y1 - y3) - (x1 - x3)*(y3 - y0))) ==
        abs((x1 - x0)*(y2 - y1) - (x2 - x1)*(y1 - y0) +
        (x2 - x0)*(y3 - y2) - (x3 - x2)*(y2 - y0) +
        (x3 - x0)*(y1 - y3) - (x1 - x3)*(y3 - y0))):
        return x0, y0
    else:
        return rand_coord()



x0, y0 = rand_coord()

for i in range(30000):
    choise = np.random.randint(0, 3, 1)
    if choise == 0:
        x0 = (x1 + x0) / 2
        y0 = (y1 + y0) / 2
    elif choise == 1:
        x0 = (x2 + x0) / 2
        y0 = (y2 + y0) / 2
    else:
        x0 = (x3 + x0) / 2
        y0 = (y3 + y0) / 2
    xy.append((x0, y0))

xy = np.array(xy, dtype=[("x", "float"), ("y", "float")])


gr = sns.scatterplot(x=xy['x'], y=xy['y'], s = 3)
plt.title("Sierpinski triangle")
plt.show()
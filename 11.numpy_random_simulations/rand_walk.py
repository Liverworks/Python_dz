import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x = y = 0


for i in range(30): # 30 steps
    x1, y1 = x, y
    l = np.random.randint(0, 4, 1)  # direction
    if l == 0:
        x += 1
    elif l == 1:
        y += 1
    elif l == 2:
        x -= 1
    else:
        y -= 1
    gr = sns.lineplot(x = [x1, x], y= [y1, y], )    # rainbow!

plt.title("Random walk")
plt.show()
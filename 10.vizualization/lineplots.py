import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

a = np.random.normal(5, 1, 25)
b = a.tolist()
b = sorted(b)

gr = sns.lineplot(x=b, y=[i/25 for i in range(0,25)])



gr.set(xlabel = "value", ylabel = "P")
plt.title("Function")
plt.show()
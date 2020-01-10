import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

a = list(np.random.random(1000))
b = [x for y in range(500) for x in range(1, 3)]
c = [x for x in range(1, 3) for y in range(500)]
data = []
print(c)

for i in range(len(a)):
    data.append((a[i], b[i], c[i]))


print(data)
da = np.array(data, dtype=[("vec", "float"),("fac", "U10"), ("fac2", "U10")])
print(da)
sns.set(style="whitegrid")
gr = sns.boxplot(x=da["fac"], y=da["vec"], hue=da["fac2"], palette="Set3")
plt.title("Random boxes")
plt.show()


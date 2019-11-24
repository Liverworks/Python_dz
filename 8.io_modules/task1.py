import some_functs as sf
import random

l = [random.random() for x in range(12)]

a = sf.maximum(l)
b = sf.mean(l)
c = sf.moda(l)

print(a,b,c, sep='\n')

a = [x**2 for x in range(11)]
print(a)

a = [x + y for x,y in zip(range(4),range(5, 9))]
print(a)

a = [k + '->' + v for k in "ATGC" for v in "ATGC" if k != v]
print(a)

a = [ [i for i in range(1,4)],[i for i in range(4,7)],[i for i in range(7, 10)]]
print(a)


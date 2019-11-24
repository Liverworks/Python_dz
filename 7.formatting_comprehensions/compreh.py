a = [x**2 for x in range(11)]
print(a)

a = [x + y for x in range(4) for y in range(5, 9)]
print(a)

a = [k + '->' + v for k in "ATGC" for v in "ATGC" if k != v]
print(a)

a = [[i + a for i in range(1,4)] for a in range(0,7,3) ]
print(a)


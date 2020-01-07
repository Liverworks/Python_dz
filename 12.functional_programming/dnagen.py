def generate(l):
    import itertools as it
    alph = ['A', 'T', 'G', 'C']
    combs = []
    for i in range(1, l + 1):
        combs = it.product(alph, repeat=i)
        for a in combs:
            yield "".join(a)




print(list(generate(5)))

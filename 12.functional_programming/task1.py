
gen1 = map(lambda x: x/35, range(36))
print(list(gen1))

gen2 = filter(lambda x: x % 5 == 0 or x == 8, range(36))
print(list(gen2))

gen3 = filter(lambda x: 0.05 <= x <= 0.95, map(lambda x: x / 35, range(36)))
print(list(gen3))

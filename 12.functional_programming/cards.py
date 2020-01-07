import itertools as it

ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits = ['H', 'D', 'C', 'S']

cards = it.product(ranks, suits)

print(list(cards))
money = 1000
apple_price = 50
orange_price = 30

print(f'You have {money}, you can buy {money // apple_price} apples or {money // orange_price} oranges')

name = "Vasya"

num_apples = int(input('%s, how many apples do you want to buy?' % name))

print(f'Then buy {num_apples} apples and {((money - apple_price * num_apples) / orange_price):.5} oranges')

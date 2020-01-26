friend_pizzas =	pizzas[:]

pizzas.append("hawaiian")
friend_pizzas.append("extra cheese")

for pizza in pizzas:
	print("My favorite pizza toppings are " + pizza.title())

	print()

for friend_pizza in friend_pizzas:
	print("My friends favorite pizzas are: " + friend_pizza.title())

	print()	
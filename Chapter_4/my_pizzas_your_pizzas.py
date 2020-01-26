# Make a copy of your list of pizzas, and call it friend_pizzas.
pizzas = ["pepperoni","sausage","deluxe",]
for pizza in pizzas:
		print("I love " + pizza.title() + " pizza!\n")

print("These are my favorite pizza toppings")

friend_pizzas =	pizzas[:]

pizzas.append("hawaiian")
friend_pizzas.append("extra cheese")

for pizza in pizzas:
	print("My favorite pizza toppings are " + pizza.title())

	print()

for friend_pizza in friend_pizzas:
	print("My friends favorite pizzas are: " + friend_pizza.title())

	print()	
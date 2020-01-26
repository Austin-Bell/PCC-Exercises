""" Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an emptu list called finished
sandwiches. Loop through the list of sandwich orders and print a message for each order."""


sandwich_orders = ["Ham", "Buffalo","Pastrami","Steak"]
finished_sandwiches = []

while sandwich_orders:
	sandwiches = sandwich_orders.pop()

	print("I am currently making a " + sandwiches)
	finished_sandwiches.append(sandwiches)

print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
		print(finished_sandwich.title())


print("The deli has ran out of Pastrami")

while "Pastrami" in sandwich_orders:
	finished_sandwiches.remove("Pastrami")

print(finished_sandwiches)
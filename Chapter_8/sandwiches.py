"""Write a function that accepts a list of items a person wants on a sandwich. The function
should have one patameter that collects as many items as the function call provides."""

def sandwich(*toppings):
	print("This sandwich has these toppings: ")
	for toppings in toppings:
		print("- " + toppings)

sandwich("mayo","salami","Wheat bread")

"""Write a loop that promps the user to enter a series of pizza toppings until they enter a
'quit' value."""

prompt = input("Enter a series of pizza toppings that you want on your pizza: ")

active = True

while active == True:
	prompt = input("Enter a series of pizza toppings that you want on your pizza: ")

	if prompt == 'quit':
		active == False
		break
	else:
		print("\n " +prompt)



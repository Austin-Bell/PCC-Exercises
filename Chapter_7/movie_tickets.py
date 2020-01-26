"""A movie theater charges different ticket prices depending on a person's age
. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket."""



active = True

while active:
	prompt = input("What is your age for movie ticket prices.")
	message = int(prompt)

	if message < 3:
		print("It's free to get in.")

	if message >= 3 and message <= 12:
		print("Your movie ticket $10")

	if message > 12:
		print("Your movie ticket is $15")
		


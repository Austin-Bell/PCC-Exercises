"""Write a program that polls users about their dream vacation. Write a prompt similar to
If you could visit one place in the world where would you go."""

responses = {}

polling_active = True

while polling_active:
	name = input("\nWhat is your name: ")
	response = input("What is your dream vacation: ")

	responses[name] = response

	repeat = input("Do you have another dream vacation? (yes/no)")

	if repeat == 'no':
		polling_active = False
	elif repeat == 'yes':
		response

print("\n --Poll Results--")
for name, response in responses.items():
	print(name + " dream vacation: " + response + ".")		
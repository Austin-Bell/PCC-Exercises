"""Write a program that prompts for two numbers. Add them together and print the result."""

print("Give me two numbers, and I'll add them")
print("Enter 'q' to quit")

while True:
	first_number = input("\nFirst Number: ")
	if first_number == 'q':
		break
	second_number = input("Second Number: ")
	
	try:
		 answer = int(first_number) + int(second_number)

	except ValueError:
		print("You must enter a number")
	
	else:
		print(answer)

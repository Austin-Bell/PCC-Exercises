""" Ask the user for a number, and then report whether the number is a multiple of 10 or not."""

prompt = input("Enter a number please: ")
prompt = int(prompt)

if prompt % 10 == 0:
	print("That number is a multiple of 10")
else:
	print("That number is not a multiple of 10")
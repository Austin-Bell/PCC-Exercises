"""Write a program that ask the user how many people are in their dinner group.
If the answer is more than eight, print a message saying they'll have to wait for a table."""

prompt = input("How many people are in your dinner group")
prompt = int(prompt)

if prompt >= 8:
	print("You will have to wait for a table")
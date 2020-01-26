"""Write a while loop that prompts users for their name. When they enter their name,
print a greeting to teh screen and add a line recording their visit in a file called 
guest_book.txt"""

filename = 'guest_book.txt'

print("Enter 'quit to exit from screen")

while True:
	name = input("\nWhat is your name?: ")

	if name == 'quit':
		break
	else:
		with open(filename,'a') as file_object:
			file_object.write(name + "\n")
			print("Hello " + name + " you have been added to the guest book.")	
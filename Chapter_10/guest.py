"""Write a program that prompts the user for their name. When they respond, write their anme to
a file called guest.txt."""

respond= input("What is your name?: ")


with open('guest.txt','a') as file_object:
	file_object.write(respond)

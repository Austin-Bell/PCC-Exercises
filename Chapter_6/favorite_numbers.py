# use a dictionary to store peoples favorite numbers.
"""
favorite_number = {'Aaron': 15,'Austin': 64,"Stacy":18}
"""


# Modify program so a person can have more than one favorite number
favorite_number = {
'Aaron': [15,32,100],
'Austin': [8, 16, 32, 64],
"Stacy": [3, 18, 4, 21]
}

for name, number in favorite_number.items():
	print("\n" + name.title() +"'s" + " favorite numbers are")
	for numbers in number:
		print(numbers)
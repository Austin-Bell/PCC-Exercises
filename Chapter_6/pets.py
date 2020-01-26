# Make several dictionarites, where the name of each dictionary is the name of a pet. store these dictionaries in a list called pets.

oliver = {
	'animal': 'cat',
	'owner': 'Tom'
}

mcguire = {
	'animal': 'dog',
	'owner': 'Kevin'
}

tina = {
	'animal': 'ferret',
	'owner': 'Emily'
}

pets = [oliver,mcguire,tina]

for pet in pets:
	print(pet)
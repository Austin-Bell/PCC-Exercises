# make a dictionary containing three major rivers and the country each river runs through.

rivers = {'Nile':'Egypt','Mississippi': 'Mississippi','English Channel': 'London'}

for key, value in rivers.items():
	print("\nKey: " + key)
	print("\nValue: " + value)
	print("\nThe " + key.title() + " runs through " + value.title())
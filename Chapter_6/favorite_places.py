# Make a dictionary called favorite places. Think of three friends names to be used as keys, loop through the dictionary, and print each person's name and their favorite places.

favorite_places = {
'Austin': ['Seattle','California','Milwaukee'],
'Blake': ['Japan'],
'Daniel': ['Sedona','Flagstaff']
}

for name, place in favorite_places.items():
	print( "\n" + name.title() + "'s"  " favorite places are: ")
	for places in place:
		print(places.title()) 
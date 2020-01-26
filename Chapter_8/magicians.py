"""Make a list of magician's names. Pass the lsit to a function called show_magicians(), which
prints the ame of each magicain in the list."""
"""
def show_magicians(names):
	for name in names:
		print(name)

magician_names = ["Copperfield","Blaine","Angel","Dein"]
"""

magician_names = ["Copperfield","Blaine","Angel","Dein"]
magician_with_titles = []

# Great Magicians
def make_great(names):
	while names:
		current_names = names.pop()
		magician_with_titles.append("The Great "+ current_names)


	
def show_magicians(names):
	for name in names:
		print(name)


make_great(magician_names[:])
show_magicians(magician_with_titles)
show_magicians(magician_names)
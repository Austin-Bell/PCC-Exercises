# Make a list of people who should take the favorite languages poll. Loop through the list and print people who should take the poll

favorite_languages = {
	'jen':'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

polling = {
	"erin":'Haskell',
	"John": 'Java',
	'edward': 'ruby',
	'phil': 'python',
	'Lisa': 'c++'

}

for name in polling.keys():
	if name in favorite_languages.keys():
		print(name.title() + " thank you for taking the poll!")
	else:
		print(name.title() + " please take the poll.")


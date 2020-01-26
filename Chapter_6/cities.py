""" Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country
that the city is in.
"""

cities = {

	'Seattle' : {
	'country': 'United States',
	'population': '704,352',
	'fact': 'Home of the space needle'
	},

	'Tokyo' : {
	'country': 'Japan',
	'population': '38,305,000',
	'fact': 'incredible candy'
	},

	'London' : {
	'country': 'United Kingdom',
	'population': '65,648,100',
	'fact': 'United Kingdom is made up of England, Ireland and Netherlands'
	}
}

for city, city_info in cities.items():
	print("\ncity: " + city)
	country_name = city_info['country']
	pop_count = city_info['population']
	info = city_info['fact']

	print("Country: " + country_name)
	print("Population: " + pop_count)
	print("Fast Fact: " + info)


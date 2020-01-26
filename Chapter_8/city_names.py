"""Write a function called city_country() that takes in the name of a city and its country.
The function should return a string formatted like this."""

def city_country(city,country):
	city_and_country = city + ', ' + country
	return city_and_country.title()

location_1 = city_country('milwaukee','united states')
print(location_1)
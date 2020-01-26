"""Write a function called describe_city() taht accepts the name of a city and its country. The function should print a simple
sentence, such as Reykjavik is in Iceland."""

def describe_city(city,country="United States"):
	print( city + " is in " + country)

describe_city("Seattle")
describe_city("\nLos Angeles")


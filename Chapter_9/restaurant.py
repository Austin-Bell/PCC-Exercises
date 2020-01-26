"""Make a class called restaurant. The __init__() method for Restaurant should store two attributes:
a restaurant name and a cuisine _type."""

class Restaurant():
	"""docstring for Restaurant"""
	def __init__(self, name,cuisine):
		self.name = name
		self.cuisine = cuisine
	
	def describe_restaurant(self,name,cuisine):
		print("This restaurant is called " + self.name.title() + " and it serves " + self.cuisine)

	def open_restaurant(self,name):
		print(self.name.title() + " is now open!")

new_restaurant = Restaurant("Bell's Burgers","Cheese Burgers")
new_restaurant.describe_restaurant("Bell Burgers","Cheese Burgers")

new_restaurant2 = Restaurant("Super Gyros","Cheese Gyros")			
new_restaurant2.describe_restaurant("Super Gyros","Cheese Gyros")


new_restaurant3 = Restaurant("Box 'o' Tacos","Supreme Delxue Tacos")
new_restaurant3.describe_restaurant("Box 'o' Tacos","Supreme Delxue Tacos")
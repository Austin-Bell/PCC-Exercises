""" Start with your program from 9-1 Add an attribute called number_served with a default value of 0.
print the number of customers served."""

class Restaurant():
	"""docstring for Restaurant"""
	def __init__(self, name,cuisine):
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0
	
	def describe_restaurant(self,name,cuisine):
		print("This restaurant is called " + self.name.title() + " and it serves " + self.cuisine)

	def open_restaurant(self,name):
		print(self.name.title() + " is now open!")

	def set_number_served(self):
		print(self.number_served)

	def increment_number_served(self,customers):
		self.number_served += customers



class IceCreamStand(Restaurant):
				"""docstring for IceCreamStand"""
				def __init__(self,name,cuisine):
					super(IceCreamStand, self).__init__(name,cuisine)
					self.flavors = 10

				def describe_flavors(self,):
					print("This Ice Cream Stand has: " + "\n" + str(self.flavors) + " flavors")
								

new_restaurant = Restaurant("Bell's Burgers","Cheese Burgers",)
new_restaurant.describe_restaurant("Bell Burgers","Cheese Burgers")

new_ice_cream_stand = IceCreamStand("So Icy","Ice Cream")
new_ice_cream_stand.describe_flavors()
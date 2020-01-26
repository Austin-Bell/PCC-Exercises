"""Write a function that sroes information about a car in a dictionary."""

def make_car(manufacturer,model, **add_info):
	car_profile = {}
	car_profile['manufacturer'] = manufacturer
	car_profile['model'] = model
	for key, value in add_info.items():
		car_profile[key] = value
		return car_profile

car = make_car('Honda','Civic',year='2000',color='silver')
print(car)		
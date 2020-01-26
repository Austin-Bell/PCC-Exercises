"""Make a class called user. create two attributes called first_name and last_name, and then create several other attributes
that are typically stores in a user profile. Make two methods taht print a summary of user information and one that prints
a personalized message to the user."""

"""Add and attribute called login_attempts to your User class. Write a method called increment login_attempts() that increments
the value of login_attempts by 1. Write another method called reset_login_attempts() that resets the login value of login_attempts
to 0."""

time_of_day = 1

class User():
	"""docstring for User"""
	def __init__(self, first_name,last_name,age,location):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempts = 0

	def describe_user(self):
		print("""This users name is: """ + self.first_name.title() + " " + self.last_name.title() + "\n" +
		" age: " + str(self.age) + " location: " + self.location)

	def greet_user(self):
		if time_of_day >= 1:
			print("Good afternoon " + self.first_name.title())
		else:
			print("Welcome " + self.first_name.title())

	def increment_login_attempts(self,attempts):
		self.login_attempts += attempts
		print(self.login_attempts)

	def reset_login_attempts(self):
		if self.login_attempts > 1:
			print("resetting login attempts to 0")	
			self.login_attempts = 0


class Admin(User):
	"""docstring for Admin"""
	def __init__(self, first_name,last_name,age,location):
		super(Admin, self).__init__(first_name,last_name,age,location)
		self.privileges = Privileges()

	
			
class Privileges():
	"""docstring for Privleges"""
	def __init__(self,privileges=[]):
		self.privileges = privileges

	def	show_privileges(self):
		self.privileges = ["can post","can add users","can ban users","can delete posts"]
		print("The admin has these sets of privileges: ")
		for privilege in self.privileges:
			print(privilege)	
		
		
							
												

new_user = User("Austin","Bell",25,"Phoenix")
new_user.describe_user()

new_admin = Admin("Austin","Bell",25,"Phoenix")

new_admin2 = Admin("Austin","Bell",25,"Phoenix")
new_admin2.privileges.show_privileges()	
















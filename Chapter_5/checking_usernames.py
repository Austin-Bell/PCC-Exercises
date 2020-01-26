
current_users = ["Eric","Raven","Charles","Logan","Scott"]

new_users = ["Steve","Tony","Raven","Charles","Bruce"]

for new_user in new_users:
	if new_user in current_users:
		print("Choose a new user name")
	else:
		print("That username is available")

"""Build a user profile of yourself by copying user_profile.py from page 153."""

def build_profile(first,last, **user_info):
	"""Build a dictionary containing everthing we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
		return profile

user_profile = build_profile('austin','bell',location = 'Phoenix',field='computer science')
print(user_profile)		
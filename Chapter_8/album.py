"""Write a function called make_album() that builds a dictionary describing a music album."""

def album(artist_name,album_title):
	artist_album = {'artist': artist_name, 'album': album_title}
	return artist_album

"""
album_1 = album("Kendrick Lamar","Good Kid MAAD City")
print(album_1)	
"""

# 8-8 User Albums

while True:
	print("\nPlease enter in album and artist information")
	print("\nType 'quit' at any time to quit the program")
	User_input1 = input("\nArtist: ")
	if User_input1 == 'quit':
		break

	User_input2 = input("\nAlbum title: ")
	if User_input2 == 'quit':
		break
	
	print("\n")
	user_album = album(User_input1,User_input2)
	print(user_album)		
with open('learning_python.txt') as file_object:
	content = file_object.read().replace("Python","C")

	print(content)
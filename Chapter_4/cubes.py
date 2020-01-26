#  Make a list of the first 10 cubes and use a for loop to print out each the value of each cube
cubes = list(range(1,11))

for cube in cubes:
	cube = cube**3
	#print(cube)

# use list comprehension to generate a list of the first 10 cubes.
cubed = [c**3 for c in range(1,11)]
print(cubed)	
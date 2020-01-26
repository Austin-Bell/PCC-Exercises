""" The module random contains functions that generate random numbers in a variety of ways.
Make a class Die with one attribute called sides, which has a default value of 6.
Write a method called roll_dice() that prints a random side."""

from random import randint

class Die(object):
	"""docstring for Die"""
	def __init__(self):
		self.sides = 6

	def roll_dice(self):
		x = randint(1,self.sides)

		print("Rolling the dice: " +str(x))


new_Die = Die()

new_Die.roll_dice()		

		
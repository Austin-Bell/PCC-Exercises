import sys

import pygame
from settings import Settings
from game_character import Viking

def run_game():

	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Blue Sky")

	bg_color = (4, 98, 249)

	# Make a viking character
	viking = Viking(screen)


	# Start loop for main game.
	while True:

		# Watch for keyboard and mouse events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(ai_settings.bg_color)
		viking.blitme()

		pygame.display.flip()

run_game()				


import pygame

class Viking():

	def __init__(self,screen):
		self.screen = screen

		#Load the viking image and get its rect.
		self.image = pygame.image.load('images/viking.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()


		# Start the viking at the bottom left of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.rect.left = self.screen_rect.left

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)	
		
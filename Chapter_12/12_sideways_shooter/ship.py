import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.midleft = self.screen_rect.midleft
        
        # Store a decimal value for the ship's center.
        self.bottom = float(self.rect.bottom)
        
        # Movement flags
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_up and self.rect.top > 0:
           self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom+= self.ai_settings.ship_speed_factor   
        
        # Update rect object from self.center.
        self.rect.bottom = self.bottom
                
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

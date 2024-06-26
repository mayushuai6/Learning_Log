# powerup.py
import pygame
from pygame.sprite import Sprite
import random

class PowerUp(Sprite):
    """A class to manage power-ups."""

    def __init__(self, ai_game):
        """Initialize the power-up and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the power-up image and get its rect.
        self.image = pygame.image.load('images/powerup.bmp')
        self.rect = self.image.get_rect()

        # Start each new power-up at a random position near the top of the screen.
        self.rect.x = random.randint(0, self.settings.screen_width - self.rect.width)
        self.rect.y = random.randint(0, max(0, self.settings.screen_height - self.rect.height))

        # Store the power-up's position as a decimal value.
        self.y = float(self.rect.y)

        # Set the power-up's speed.
        self.speed = self.settings.powerup_speed

    def update(self):
        """Move the power-up down the screen."""
        self.y += self.speed
        self.rect.y = self.y

    def blitme(self):
        """Draw the power-up at its current location."""
        self.screen.blit(self.image, self.rect)

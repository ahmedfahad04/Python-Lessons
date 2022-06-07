import pygame


class Ship():
    """Initialize the ship and set its starting position"""

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the image and get its rect.
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_resolution = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_resolution.centerx
        #self.rect.centery = self.screen_resolution.centery
        self.rect.bottom = self.screen_resolution.bottom

        # Store a decimal value for the ship's center
        self.centerX = float(self.rect.centerx)
        self.centerY = float(self.rect.centery)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""

        if self.moving_right and self.rect.right < self.screen_resolution.right:
            self.centerX += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.centerX -= self.ai_settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.centerY -= self.ai_settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_resolution.bottom:
            self.centerY += self.ai_settings.ship_speed

        # update rect object from self.center
        self.rect.centerx = self.centerX
        self.rect.centery = self.centerY

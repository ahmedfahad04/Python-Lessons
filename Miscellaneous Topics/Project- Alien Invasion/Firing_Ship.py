import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen obj
    pygame.init()

    # Create obj of Settings class
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_height, ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen, ai_settings)

    # Make a group to store bullets in.
    bullets = Group()

    # start the main loop for the game
    while True:
        gf.check_events(ai_settings,screen,ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()

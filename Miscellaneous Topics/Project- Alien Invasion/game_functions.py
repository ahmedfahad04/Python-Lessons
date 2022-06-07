import sys, pygame
from bullet import Bullet


def check_keyDown_events(event, ai_settings, screen, ship, bullets):
    """Respond to Keypress"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_UP:
        ship.moving_up = True

    elif event.key == pygame.K_DOWN:
        ship.moving_down = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)



def check_keyUp_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

    elif event.key == pygame.K_UP:
        ship.moving_up = False

    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """Respond to key presses and mouse events"""

    # watch for keyboard and mouse events
    for event in pygame.event.get():

        # watch for keyboard and mouse events
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # when key is pressed (right, left)
            check_keyDown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:  # when key is released
            check_keyUp_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""

    # redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # draw the ship image
    ship.blitme()

    # make screen visible
    pygame.display.flip()

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()


def update_bullets(bullets):
    # Update bullet positions
    bullets.update()

    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullets if limit not reached yet."""

    # Create a new bullet and add it to the bullets group
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


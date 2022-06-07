class Settings():
    """A class to store all settings for ALIEN INVASION"""

    def __init__(self):
        """Initialize the game's settings"""

        # Screen Settings
        self.screen_width = 720
        self.screen_height = 1080
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 2

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3

        


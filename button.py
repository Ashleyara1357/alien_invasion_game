import pygame.font

class Button:
    def __init__(self, ai_game, msg, y_offset=0):
        """Initialize button attributes with optional vertical offset."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set dimensions and properties
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # Green
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build button's rect and center it with offset
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y += y_offset  # Apply vertical offset
        
        # Prep button message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
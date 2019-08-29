import pygame

pygame.init()

DEFAULT_FONT = pygame.font.Font(None, 32)
INACTIVE_COLOUR = (69, 203, 239)
ACTIVE_COLOUR = (0, 80, 255)


def display_text(window, content, txt_size, colour, position):
    font = pygame.font.SysFont(None, txt_size)
    text = font.render(content, True, colour)
    window.blit(text, position)


# UI Component
class Button:
    def __init__(self, x, y, w, h, colour, txt=''):
        self.active = False
        self.rect = pygame.Rect(x, y, w, h)
        self.colour = colour
        self.txt = txt
        self.txt_render_settings = DEFAULT_FONT.render(self.txt, True, self.colour)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            # If the user clicked on the rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = True
                self.colour = ACTIVE_COLOUR

            else:
                self.active = False
                self.colour = INACTIVE_COLOUR

import pygame


def display_text(window, content, txt_size, colour, position):
    font = pygame.font.SysFont(None, txt_size)
    text = font.render(content, True, colour)
    window.blit(text, position)


import pygame


def drawText(screen, text, x, y, size=50, color=(200, 000, 000)):
    text = str(text)
    font = pygame.font.SysFont("Arial", 14)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))

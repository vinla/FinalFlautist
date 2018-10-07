import pygame


class Block():
    def __init__(self):
        self.x = 10
        self.y = 10
        self.width = 32
        self.height = 32
        self.color = (32, 132, 32)

    def Draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         [self.x, self.y, self.width, self.height])

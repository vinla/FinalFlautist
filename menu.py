import pygame
import gametext


class Menu():
    def __init__(self, options):
        self.selectedIndex = 0
        self.repeatDelay = 200
        self.options = options

    def Update(self, deltaTime):
        self.repeatDelay = max(self.repeatDelay - deltaTime, 0)
        if self.repeatDelay == 0:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                self.selectedIndex = (
                    self.selectedIndex - 1) % len(self.options)
                self.repeatDelay = 200
            if pressed[pygame.K_DOWN]:
                self.selectedIndex = (
                    self.selectedIndex + 1) % len(self.options)
                self.repeatDelay = 200
            if pressed[pygame.K_RETURN]:
                self.repeatDelay = 200
                self.OptionSelected(self.selectedIndex,
                                    self.options[self.selectedIndex])

    def OptionSelected(self, index, text):
        pass

    def Draw(self, screen):
        y_offset = 50
        index = 0
        for option in self.options:
            if index == self.selectedIndex:
                pygame.draw.rect(screen, (200, 10, 10), [
                                 45, y_offset, 200, 30])
                gametext.drawText(screen, option, 50,
                                  y_offset, 14, (255, 191, 77))
            else:
                gametext.drawText(screen, option, 50, y_offset, 14, (0, 0, 0))
            y_offset += 50
            index += 1

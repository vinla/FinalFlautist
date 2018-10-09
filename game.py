import pygame
import sys
from stack import Stack
from mainmenu import MainMenu


class Game():
    def __init__(self):
        self.screenSize = (800, 600)
        self.backgroundColor = (230, 230, 230)
        self.screen = pygame.display.set_mode(self.screenSize)
        self.clock = pygame.time.Clock()
        self.sceneStack = Stack()
        self.sceneStack.push(MainMenu(self))
        pygame.display.set_caption("Final Flautist")

    def Run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.backgroundColor)

            elapsed_ms = self.clock.tick(60)

            currentScene = self.sceneStack.peek()
            currentScene.Update(elapsed_ms)
            currentScene.Draw(self.screen)

            pygame.display.flip()

    def StartScene(self, scene):
        self.sceneStack.push(scene)

    def EndScene(self):
        self.sceneStack.pop()

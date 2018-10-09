import pygame
import sys
import gametext
from menu import Menu
from songmenu import SongMenu


class MainMenu(Menu):
    def __init__(self, game):
        options = ["Play a song", "Options", "Quit"]
        Menu.__init__(self, options)
        self.game = game

    def OptionSelected(self, index, text):
        if index == 0:
            self.game.StartScene(SongMenu(self.game))
        elif index == 2:
            sys.exit()

from menu import Menu
from playsong import PlaySong


class SongMenu(Menu):
    def __init__(self, game):
        options = ["My First Song", "Flute Sonata", "Mega Symphony",
                   "Eternal Sonata", "A Flute Song", "Back"]
        Menu.__init__(self, options)
        self.game = game

    def OptionSelected(self, index, text):
        if text == "Back":
            self.game.EndScene()
        else:
            self.game.StartScene(PlaySong(self.game))

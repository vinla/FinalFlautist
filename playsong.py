import pygame
from track import Track


class PlaySong():
    def __init__(self, game):
        self.game = game
        self.tracks = []
        self.tracks.append(Track((10, 100, 10), 50, pygame.K_a))
        self.tracks.append(Track((100, 10, 10), 100, pygame.K_s))
        self.tracks.append(Track((10, 10, 100), 150, pygame.K_d))
        self.tracks.append(Track((10, 100, 10), 200, pygame.K_j))
        self.tracks.append(Track((100, 10, 10), 250, pygame.K_k))
        self.tracks.append(Track((10, 10, 100), 300, pygame.K_l))

        self.tracks[0].AddNote(200, 200)
        self.tracks[0].AddNote(400, 200)
        self.tracks[1].AddNote(200, 200)
        self.tracks[2].AddNote(400, 200)

    def Update(self, elapsed):
        ended = True
        for track in self.tracks:
            track.Update(elapsed)
            ended = ended and track.ended

        if ended:
            self.game.EndScene()

    def Draw(self, screen):
        for track in self.tracks:
            track.Draw(screen)

import sys
import pygame
from settings import Settings
from track import Track


def run_game():
    gameSettings = Settings()
    pygame.init()

    screen = pygame.display.set_mode(gameSettings.screenSize)
    clock = pygame.time.Clock()
    tracks = []

    tracks.append(Track((10, 100, 10), 50))
    tracks.append(Track((100, 10, 10), 100))
    tracks.append(Track((10, 10, 100), 150))

    tracks[0].AddNote(200, 200)
    tracks[0].AddNote(400, 200)
    tracks[1].AddNote(200, 200)
    tracks[2].AddNote(400, 200)

    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(gameSettings.backgroundColor)

        elapsed_ms = clock.tick(60)

        for track in tracks:
            track.Update(elapsed_ms)
            track.Draw(screen)

        pygame.display.flip()


run_game()

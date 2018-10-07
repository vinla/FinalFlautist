import pygame
from enum import Enum


class TrackStatus(Enum):
    NotStarted = 0
    Playing = 1
    Finished = 2


class Track():
    def __init__(self, color, y_offset):
        self.status = TrackStatus.NotStarted
        self.elapsed_ms = 0
        self.color = color
        self.y_offset = y_offset
        self.notes = []

    def Update(self, deltaTime):
        self.elapsed_ms += deltaTime

    def AddNote(self, start, duration):
        self.notes.append((start, duration))
        self.notes.sort(key=lambda tup: tup[0])

    def Draw(self, screen):
        viewport_x = self.elapsed_ms / 10
        pygame.draw.line(screen, (0, 0, 0), (0, self.y_offset),
                         (800, self.y_offset), width=2)

        for note in self.notes:
            note_x = note[0] - viewport_x
            note_duration = note[1]
            if(note_x < 1000):
                pygame.draw.rect(screen, self.color, [
                    note_x, self.y_offset, note_duration, 20])

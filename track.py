import pygame
from enum import Enum


class TrackStatus(Enum):
    NotStarted = 0
    Playing = 1
    Finished = 2


class Track():
    def __init__(self, color, y_offset, key):
        self.status = TrackStatus.NotStarted
        self.elapsed_ms = 0
        self.color = color
        self.y_offset = y_offset
        self.notes = []
        self.key = key
        self.isPlayed = False
        self.shouldBePlayed = False
        self.end = 100
        self.ended = False

    def Update(self, deltaTime):

        if self.elapsed_ms > self.end:
            self.ended = True
            return

        pressed = pygame.key.get_pressed()
        self.elapsed_ms += deltaTime
        self.shouldBePlayed = False
        for note in self.notes:
            start = note[0] * 10
            end = start + (note[1] * 10)
            if start <= self.elapsed_ms and end >= self.elapsed_ms:
                self.shouldBePlayed = True

        self.isPlayed = pressed[self.key]

    def AddNote(self, start, duration):
        self.notes.append((start, duration))
        self.notes.sort(key=lambda tup: tup[0])
        finalNote = self.notes[len(self.notes)-1]
        self.end = (finalNote[0] * 10) + (finalNote[1] * 10) + 2000

    def Draw(self, screen):
        viewport_x = self.elapsed_ms / 10
        pygame.draw.line(screen, (0, 0, 0), (0, self.y_offset),
                         (20, self.y_offset), 2)
        pygame.draw.line(screen, (0, 0, 0), (40, self.y_offset),
                         (800, self.y_offset), 2)

        for note in self.notes:
            note_x = note[0] - viewport_x + 30
            note_duration = note[1]
            if(note_x < 1000):
                pygame.draw.rect(screen, self.color, [
                    note_x, self.y_offset-6, note_duration, 12])

        pygame.draw.circle(screen, (0, 0, 0), (30, self.y_offset), 10, 2)

        if (self.isPlayed and self.shouldBePlayed):
            pygame.draw.circle(screen, self.color, (30, self.y_offset), 8)
        elif (self.isPlayed or self.shouldBePlayed):
            pygame.draw.circle(screen, (255, 0, 0), (30, self.y_offset), 8)

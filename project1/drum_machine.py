import pygame
import time

from sound import Sound

class DrumMachine:
    def __init__(self, bpm=100):
        self.set_bpm(bpm)

        self.sound_map = {
            0: None,
            1: Sound("hi_hat"),
            2: Sound("snare"),
            3: Sound("tom"),
        }

        pygame.init()

    def set_bpm(self, bpm):
        self.bpm = bpm
        self.pause = 0.25 * (60 / bpm) 

    def play(self, measure):
        while True:
            for beat in range(len(measure)):
                if measure[beat] != 0:
                    self.sound_map[measure[beat]].play()

                time.sleep(self.pause)

if __name__ == "__main__":
    drum_machine = DrumMachine()

    measure = [
        3, 1, 1, 1,
        2, 1, 1, 3,
        1, 3, 1, 3,
        2, 1, 1, 1,
    ]

    drum_machine.play(measure)
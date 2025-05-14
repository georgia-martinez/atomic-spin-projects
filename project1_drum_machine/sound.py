import pygame
import os


class Sound():
    mixer = pygame.mixer.init()

    def __init__(self, sound_name):
        sound_file = os.path.join("sounds", sound_name + ".wav")
        self.sound = pygame.mixer.Sound(sound_file)

    def play(self):
        self.sound.play()
import pygame
import time

pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load("WayUp.wav")
pygame.mixer.music.play()
time.sleep(30)
#reproduzir mp3
import pygame
pygame.init()
pygame.mixer.music.load('3.3ex021mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

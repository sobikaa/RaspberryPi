import pygame
from gpiozero import Button

pygame.init()

piano_sound = pygame.mixer.Sound("/home/pi/Desktop/music/piano_notes/piano-mp3_A0.wav")
#piano_sound.play()

first_button = Button(17)

first_button.when_pressed = piano_sound.play

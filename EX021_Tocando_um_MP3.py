# EXERCÍCIO 021 - Tocando um MP3

import pygame

pygame.init()
pygame.mixer.music.load("EX021.mp3")
pygame.mixer.music.play()
parar = input('Digite qualquer tecla para parar.')

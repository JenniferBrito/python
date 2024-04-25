# ex021: Faça um programa em pyhton que abra e reproduza um arquivo mp3

import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Francesca.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
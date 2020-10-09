#!/usr/bin/python3
import pygames
import sys

pygame.init()

size = width, height = 1024, 768
white = 255, 255, 255
screen = pygame.display.set_mode(size)
screen.fill(white)
pygames.display.flip()

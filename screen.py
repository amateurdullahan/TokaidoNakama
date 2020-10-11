#!/usr/bin/python3
import pygame
import sys

pygame.init()

size = width, height = 1024, 768
white = 255, 255, 255
screen = pygame.display.set_mode(size)
screen.fill(white)
pygame.display.flip()

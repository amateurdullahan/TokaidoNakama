#!/usr/bin/python3
"""buttons"""
import pygame

class Button(pygame.Rect):
    """Button Class for menu buttons"""
    __screen = None

    def __init__(self, left=0, top=0, width=0, height=0, screen=None, color=(255, 0, 0), rectColor=(255, 150, 0)):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        if screen is not None:
            Button.__screen = self.screen = screen
        else:
            self.screen = Button.__screen
        self.color = color
        self.rectColor = rectColor

    def add_text(self, text, text_size=25, offset=0):
        self.font = pygame.font.SysFont('Arial', text_size)
        self.screen.blit(self.font.render(text, True, self.color), ((self.left + self.width / 3) - offset, self.top))

#!/usr/bin/python3
"""buttons"""
import pygame

class Button(pygame.Rect):
    """docstring for button"""
    __screen = None

    def __init__(self, left=0, top=0, width=0, height=0, screen=None, color=(255, 0, 0), rectColor=(255, 150, 0)):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        if screen is not None:
            button.__screen = self.screen = screen
        else:
            self.screen = button.__screen
        self.color = color
        self.rectColor = rectColor

    def draw(self, color=None):
        if color is None:
            btn = self.rectColor
        else:
            btn = color
        pygame.draw.rect(self.screen, btn, self.rect, 0)

    def add_text(self, text, offset=0):
        self.font = pygame.font.SysFont('Arial', 25)
        self.screen.blit(self.font.render(text, True, self.color), ((self.left + welf.width / 3) - offest, self.top))

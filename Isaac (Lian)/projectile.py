import pygame as pg
from settings import *

class Projectile:
    def __init__(self, x, y, direction) -> None:
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 10
        self.radio = 10
        self.color = CELESTE

    def update(self):
        if self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'right':
            self.x += self.speed

    def render(self, screen):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radio)
import pygame as pg
from settings import *

class Proyectil:
    def __init__(self, x, y, direccion):
        self.x = x
        self.y = y
        self.direccion = direccion
        self.velocidad = 10
        self.radio = 10
        self.color = CELESTE

    def update(self):
        if self.direccion == 'arriba':
            self.y -= self.velocidad
        elif self.direccion == 'abajo':
            self.y += self.velocidad
        elif self.direccion == 'izquierda':
            self.x -= self.velocidad
        elif self.direccion == 'derecha':
            self.x += self.velocidad

    def render(self, pantalla):
        pg.draw.circle(pantalla, self.color, (self.x, self.y), self.radio)

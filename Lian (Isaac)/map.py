import pygame as pg
from settings import *

class Map:
    def __init__(self) -> None:
        self.map = pg.image.load("inicio.png").convert()
        self.rectangulo1 = pg.Rect(0, 400, 165, 230)
        self.rectangulo2 = pg.Rect(0, 110, 165, 220)
        self.rectangulo3 = pg.Rect(1135, 0, 1300, 700)
        self.rectangulo4 = pg.Rect(0, 630, 1300, 630)
        self.rectangulo5 = pg.Rect(0, 0, 615, 110)
        self.rectangulo6 = pg.Rect(685, 0, 1300, 110)
    
    def render(self, pantalla):
        pantalla.blit(self.map, (0, 0))
        pg.draw.rect(pantalla, ("red"), self.rectangulo1, 2)
        pg.draw.rect(pantalla, ("red"), self.rectangulo2, 2)
        pg.draw.rect(pantalla, ("red"), self.rectangulo3, 2)
        pg.draw.rect(pantalla, ("red"), self.rectangulo4, 2)
        pg.draw.rect(pantalla, ("red"), self.rectangulo5, 2)
        pg.draw.rect(pantalla, ("red"), self.rectangulo6, 2)
    
   
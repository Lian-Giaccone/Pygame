import pygame as pg

class Map:
    def __init__(self) -> None:
        self.map = pg.image.load("inicio.png").convert()
        self.wall1 = pg.Rect(0, 400, 165, 230)
        self.wall2 = pg.Rect(0, 110, 165, 220)
        self.wall3 = pg.Rect(1135, 0, 1300, 700)
        self.wall4 = pg.Rect(0, 630, 1300, 630)
        self.wall5 = pg.Rect(0, 0, 615, 110)
        self.wall6 = pg.Rect(685, 0, 1300, 110)
    
    def render(self, pantalla):
        pantalla.blit(self.map, (0, 0))
        pg.draw.rect(pantalla, ("red"), self.wall1, 2)
        pg.draw.rect(pantalla, ("red"), self.wall2, 2)
        pg.draw.rect(pantalla, ("red"), self.wall3, 2)
        pg.draw.rect(pantalla, ("red"), self.wall4, 2)
        pg.draw.rect(pantalla, ("red"), self.wall5, 2)
        pg.draw.rect(pantalla, ("red"), self.wall6, 2)
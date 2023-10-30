import pygame as pg
import sys
from settings import *
from map import *
from pj import *
from enemy import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN))
        self.clock = pg.time.Clock()
        self.mapa = Map()
        self.personaje = Personaje()
        self.teclas_presionadas = {}
        self.proyectiles = []
        self.enemigo1 = Enemigo()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.teclas_presionadas[event.key] = True
                if event.key in [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]:
                    proyectil = Proyectil(self.personaje.x, self.personaje.y, self.personaje.direccion)
                    self.proyectiles.append(proyectil)
            elif event.type == pg.KEYUP:
                self.teclas_presionadas[event.key] = False
            print(event)


    def update(self):
        if self.teclas_presionadas.get(pg.K_w):
            self.personaje.mover(0, -7)        # Mover hacia arriba
        if self.teclas_presionadas.get(pg.K_a):
            self.personaje.mover(-7, 0)        # Mover hacia la izquierda
        if self.teclas_presionadas.get(pg.K_s):
            self.personaje.mover(0, 7)         # Mover hacia abajo
        if self.teclas_presionadas.get(pg.K_d):
            self.personaje.mover(7, 0)         # Mover hacia la derecha
            
        

        for proyectil in self.proyectiles:
            proyectil.update()

        self.personaje.update()
        self.enemigo1.update()
        self.clock.tick(FPS)
        fps = int(self.clock.get_fps())
        
        pg.display.set_caption("The Binding of Isaac {0}".format(fps))

    def render(self):
        self.screen.fill("white")
        mapa = pg.transform.scale(self.mapa.map, SCREEN)
        self.screen.blit(mapa, (0, 0))
        self.mapa.render(self.screen)
        self.personaje.render(self.screen)
        self.enemigo1.render(self.screen)
        for proyectil in self.proyectiles:
            proyectil.render(self.screen)
        pg.display.flip()

game = Game()
game.run()

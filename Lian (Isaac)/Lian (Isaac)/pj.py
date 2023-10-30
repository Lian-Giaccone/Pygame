import pygame as pg
from proyectil import *
from map import *
from colisiones import *

class Personaje:
    def __init__(self):
        self.personaje = pg.image.load('personaje.png').convert_alpha()
        self.cuadros_animacion = self.animacion()
        self.personaje_grande = pg.transform.scale(self.personaje, (200, 200))
        self.direccion = 'abajo'
        self.indice_animacion = 0
        self.x = 560
        self.y = 350
        self.hitbox = pg.Rect(self.x + 75, self.y + 120, 50, 50)

    def disparar(self):
        proyectil = Proyectil(self.hitbox.x, self.hitbox.y, self.direccion)
        return proyectil

    def animacion(self):
        caminar_abajo = []
        caminar_arriba = []
        caminar_derecha = []
        caminar_izquierda = []

        for fila in range(0, 4):
            for columna in range(0, 3):
                animation = pg.Rect(96 * columna, 64 * fila, 96, 64)
                if fila == 0:
                    #caminar_abajo.append(self.personaje.subsurface(animation))
                    cuadro = self.personaje.subsurface(animation)
                    cuadro_grande = pg.transform.scale(cuadro, (200, 200))
                    caminar_abajo.append(cuadro_grande)
                if fila == 1:
                    #caminar_izquierda.append(self.personaje.subsurface(animation))
                    cuadro = self.personaje.subsurface(animation)
                    cuadro_grande = pg.transform.scale(cuadro, (200, 200))
                    caminar_izquierda.append(cuadro_grande)
                if fila == 2:
                    #caminar_derecha.append(self.personaje.subsurface(animation))
                    cuadro = self.personaje.subsurface(animation)
                    cuadro_grande = pg.transform.scale(cuadro, (200, 200))
                    caminar_derecha.append(cuadro_grande)
                if fila == 3:
                    #caminar_arriba.append(self.personaje.subsurface(animation))
                    cuadro = self.personaje.subsurface(animation)
                    cuadro_grande = pg.transform.scale(cuadro, (200, 200))
                    caminar_arriba.append(cuadro_grande)
        return {
            'abajo': caminar_abajo,
            'arriba': caminar_arriba,
            'derecha': caminar_derecha,
            'izquierda': caminar_izquierda
        }

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

        if dx > 0:
            self.direccion = 'derecha'
        elif dx < 0:
            self.direccion = 'izquierda'
        elif dy > 0:
            self.direccion = 'abajo'
        elif dy < 0:
            self.direccion = 'arriba'

    def update(self):
        self.indice_animacion = (self.indice_animacion + 1) % len(self.cuadros_animacion[self.direccion])
        self.hitbox.topleft = (self.x + 75, self.y + 120)

    def render(self, pantalla):
        cuadro_actual = self.cuadros_animacion[self.direccion][self.indice_animacion]
        cuadro_actual_grande = pg.transform.scale(cuadro_actual, (200, 200))
        pantalla.blit(cuadro_actual_grande, (self.x, self.y))
        pg.draw.rect(pantalla, ("red"), self.hitbox, 2)

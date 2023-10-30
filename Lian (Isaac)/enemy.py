import pygame as pg
import random

class Enemigo:
    def __init__(self):
        self.enemigo = pg.image.load("enemigo1.png").convert_alpha()
        self.x = 300
        self.y = 400
        self.hitbox = pg.Rect(self.x, self.y, 64, 64)
        self.velocidad = 7
        #self.movimiento = self.animacion()
        self.indice_animacion = 0

    '''
    def animacion(self):
        mover = []
        for fila in range(0, 2):
            for columna in range(0, 4):
                animation = pg.Rect(65 * columna, 65 * fila, 65, 65)
                if fila == 0:
                    cuadro = self.enemigo.subsurface(animation)
                    cuadro_grande = pg.transform.scale(cuadro, (200, 200))
                    mover.append(cuadro_grande)
                elif fila == 0:
                    cuadro = self.enemigo.subsurface(animation)
                    cuadro_grande = pg.transform.scale(cuadro, (200, 200))
                    mover.append(cuadro_grande)
        return mover'''

    def mover(self):
        # Generar una dirección de movimiento aleatoria
        direccion = random.choice(['arriba', 'abajo', 'izquierda', 'derecha'])

        if direccion == 'arriba':
            self.y -= self.velocidad 
        elif direccion == 'abajo':
            self.y += self.velocidad 
        elif direccion == 'izquierda':
            self.x -= self.velocidad 
        elif direccion == 'derecha':
            self.x += self.velocidad 

        # Actualizar la posición del rectángulo de colisión
        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def update(self):
        self.mover()

    def render(self, pantalla):
        pantalla.blit(self.enemigo, (self.x, self.y))
        pg.draw.rect(pantalla, ("red"), self.hitbox, 2)



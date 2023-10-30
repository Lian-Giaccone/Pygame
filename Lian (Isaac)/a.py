import pygame as pg
import sys

#from pygame.sprite import _Group

pg.init()
screen = pg.display.set_mode((1300,700))

def animacion():
    caminar_abajo = []
    caminar_arriba = []
    caminar_derecha = []
    caminar_izquierda = []
    sheet = pg.image.load("personaje.png").convert_alpha()

    for fila in range(0, 4):
        for columna in range(0, 3):
            animation = pg.Rect(96 * columna, 64 * fila, 96, 64)
            if fila == 0:
                caminar_abajo.append(sheet.subsurface(animation))
                    
            if fila == 1:
                caminar_izquierda.append(sheet.subsurface(animation))
                    
            if fila == 2:
                caminar_derecha.append(sheet.subsurface(animation))
                    
            if fila == 3:
                caminar_arriba.append(sheet.subsurface(animation))
    return caminar_abajo, caminar_arriba, caminar_derecha, caminar_izquierda

caminar_abajo, caminar_arriba, caminar_derecha, caminar_izquierda = animacion()

class Player(pg.sprite.Sprite):
    def __init__(self) -> None:
        pg.sprite.Sprite.__init__(self)
        self.abajo = caminar_abajo
        self.arriba = caminar_arriba
        self.derecha = caminar_derecha
        self.izquierda = caminar_izquierda

        self.image = self.abajo[1]
        self.rect = self.image.get_rect()
        self.rect_topleft = 560, 350

        self.index = 0
        self.speed = 7
        self.direction = ""

    def update(self):
        if self.index > 2:
            self.index = 0
        #self.image = self.abajo[self.index]
        #self.index += 1

        if self.direction == "arriba":
            self.image = self.arriba[self.index]
            self.index += 1
        elif self.direction == "abajo":
            self.image = self.abajo[self.index]
            self.index += 1
        elif self.direction == "derecha":
            self.image = self.derecha[self.index]
            self.index += 1
        elif self.direction == "izquierda":
            self.image = self.izquierda[self.index]
            self.index += 1
        else:
            if self.direction == "stop_arriba":
                self.image = self.abajo[1]
            elif self.direction == "stop_abajo":
                self.image = self.abajo[1]
            elif self.direction == "stop_derecha":
                self.image = self.abajo[1]
            elif self.direction == "stop_izquierda":
                self.image = self.abajo[1]

    def handle_event(self, key):
        if key[pg.K_w]:
            self.rect.y -= self.speed
            self.direction = "arriba"
        elif key[pg.K_s]:
            self.rect.y += self.speed
            self.direction = "abajo"
        elif key[pg.K_a]:
            self.rect.x -= self.speed
            self.direction = "izquierda"
        elif key[pg.K_d]:
            self.rect.x += self.speed
            self.direction = "derecha"
        else:
            if self.direction == "arriba":
                self.direction = "stop_arriba"
            elif self.direction == "abajo":
                self.direction = "stop_abajo"
            elif self.direction == "derecha":
                self.direction = "stop_derecha"
            elif self.direction == "izquierda":
                self.direction = "stop_izquierda"
            else:
                self.direction = ""
        

jugador = Player()

grupo_sprites = pg.sprite.Group()
grupo_sprites.add(jugador)
FPS = 60
CLOCK = pg.time.Clock()

cerrar = False
while cerrar == False:
    CLOCK.tick(FPS)
    pg.display.update()
    screen.fill("white")

    grupo_sprites.draw(screen)
    grupo_sprites.update()

    key = pg.key.get_pressed()
    jugador.handle_event(key)

    for event in pg.event.get():
        if event.type == pg.quit:
            pg.quit()
            cerrar = True
            sys.exit()
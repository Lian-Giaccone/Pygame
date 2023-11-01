import pygame as pg
import sys
from settings import *
from map import *
from pj import *
from enemy import *
from projectile import *

class Game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((SCREEN))
        self.clock = pg.time.Clock()
        self.map = Map()
        self.player = Player((560,350))
        self.enemy = Enemy((400,300))
        self.key_pressed = pg.key.get_pressed()
        self.group_sprites = pg.sprite.Group()
        self.group_sprites.add(self.player, self.enemy)
        

    def run(self):
        while True:
            self.handle_event()
            self.update()
            self.render()
    
    def handle_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            
            self.key_pressed = pg.key.get_pressed()
           
            

    def update(self):
        self.clock.tick(FPS)
        fps = int(self.clock.get_fps())
        pg.display.set_caption("The Binding of Isaac {0}".format(fps))

        self.player.move(self.key_pressed)
        self.group_sprites.update()

    def render(self):
        self.screen.fill("white")
        mapa = pg.transform.scale(self.map.map, SCREEN)
        self.screen.blit(mapa, (0,0))
        self.map.render(self.screen)
        self.group_sprites.draw(self.screen)
        #self.group_sprites.draw(self.player.hitbox)
        #self.player.render(self.screen)
        for sprite in self.group_sprites.sprites():
            if type(sprite) == Player:
                sprite.hitbox.x = sprite.rect.x + 50
                sprite.hitbox.y = sprite.rect.y + 80
                print(sprite.hitbox)
                pg.draw.rect(self.screen, ("red"), sprite.hitbox, 2)

        pg.display.flip()

game = Game()
game.run()
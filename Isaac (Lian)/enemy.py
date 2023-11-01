import pygame as pg
import random

class Enemy(pg.sprite.Sprite):
    def __init__(self, position) -> None:
        pg.sprite.Sprite.__init__(self)
        self.enemy = pg.image.load("enemigo1.png").convert_alpha()
        self.movement = self.animation()
        self.x = 300
        self.y = 400
        self.hitbox = pg.Rect(self.x, self.y, 64, 64)
        self.speed = 7
        self.index = 0
        self.image = self.movement[0]
        self.rect = self.image.get_rect()
        self.rect.center = position

    def animation(self):
        movement = []
        for row in range(0,2):
            for column in range(0,4):
                animation = pg.Rect(65 * column, 64 * row, 60, 60)
                if row == 0:
                    movement.append(self.enemy.subsurface(animation))
                elif row == 1:
                    movement.append(self.enemy.subsurface(animation))
        return movement
    
    def move(self):
        direction = random.choice(["up", "down", "right", "left"])

        if self.index > 7:
            self.index = 0

        if direction == "up":
            self.rect.centery -= self.speed
            self.image = self.movement[self.index]
            self.index += 1
        elif direction == "down":
            self.rect.centery += self.speed
            self.image = self.movement[self.index]
            self.index += 1
        elif direction == "left":
            self.rect.centerx -= self.speed
            self.image = self.movement[self.index]
            self.index += 1
        elif direction == "right":
            self.rect.centerx += self.speed
            self.image = self.movement[self.index]
            self.index += 1
        

        self.hitbox.x = self.x
        self.hitbox.y = self.y



    def update(self):
        if self.index > 7:
            self.index = 0
        self.move()

    def render(self, screen):
        pg.draw.rect(screen, ("red"), self.hitbox, 2)
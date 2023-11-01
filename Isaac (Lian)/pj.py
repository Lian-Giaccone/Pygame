import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self,position) -> None:
        pg.sprite.Sprite.__init__(self)
        self.pj = pg.image.load("personaje.png").convert_alpha()
        self.pj_scale = pg.transform.scale(self.pj, (150,150))
        self.movement = {}
        self.movement = self.animation()
        self.x = 560
        self.y = 350
        self.index = 0
        self.speed = 7
        self.direction = ""
        self.image = self.down[1]
        self.rect = self.image.get_rect()
        self.rect.center = position

    def animation(self):
        self.up = []
        self.down = []
        self.left = []
        self.right = []
        for row in range(0,4):
            for column in range(0,3):
                animation = pg.Rect(96 * column, 64 * row, 96, 64)
                if row == 0:
                    frame = self.pj.subsurface(animation)
                    large_frame = pg.transform.scale(frame, (150,150))
                    self.down.append(large_frame)                      
                if row == 1:
                    frame = self.pj.subsurface(animation)
                    large_frame = pg.transform.scale(frame, (150,150))
                    self.left.append(large_frame)                        
                if row == 2:
                    frame = self.pj.subsurface(animation)
                    large_frame = pg.transform.scale(frame, (150,150))
                    self.right.append(large_frame)                
                if row == 3:
                    frame = self.pj.subsurface(animation)
                    large_frame = pg.transform.scale(frame, (150,150))
                    self.up.append(large_frame)
        return self.up, self.down, self.right, self.left
    
    def update(self):
        if self.index > 2:
            self.index = 0

        if self.direction == "up":
            self.image = self.up[self.index]
            self.index += 1
        elif self.direction == "down":
            self.image = self.down[self.index]
            self.index += 1
        elif self.direction == "right":
            self.image = self.right[self.index]
            self.index += 1
        elif self.direction == "left":
            self.image = self.left[self.index]
            self.index += 1
        else:
            if self.direction == "stop_up":
                self.image = self.down[1]
            elif self.direction == "stop_down":
                self.image = self.down[1]
            elif self.direction == "stop_right":
                self.image = self.down[1]
            elif self.direction == "stop_left":
                self.image = self.down[1]
        
        
        
    
    def move(self,key):
        if key[pg.K_w]:
            self.rect.y -= self.speed
            self.direction = "up"
        elif key[pg.K_s]:
            self.rect.y += self.speed
            self.direction = "down"
        elif key[pg.K_a]:
            self.rect.x -= self.speed
            self.direction = "left"
        elif key[pg.K_d]:
            self.rect.x += self.speed
            self.direction = "right"
        else:
            if self.direction == "up":
                self.direction = "stop_up"
            elif self.direction == "down":
                self.direction = "stop_down"
            elif self.direction == "right":
                self.direction = "stop_right"
            elif self.direction == "left":
                self.direction = "stop_left"
            else:
                self.direction = ""

    def render(self,screen):
        #screen.blit(self.pj, (self.x,self.y))
        pass
        
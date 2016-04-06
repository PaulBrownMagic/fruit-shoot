__author__ = 'brown'
import pygame, constants, math, os

class Player():
    gun1 = None
    gun2 = None
    gun3 = None
    gun4 = None
    crosshair = None

    def __init__(self):
        self.x = int(constants.WIDTH/2)
        self.y = constants.HEIGHT
        self.crosshair = pygame.image.load(os.path.join('images', 'crosshair.png')).convert_alpha()
        self.rect = self.crosshair.get_rect()
        self.gun1 = [self.x-int(self.rect.width/2),self.y]
        self.gun2 = [self.x,self.y-30]
        self.gun3 = [self.x,self.y-55]
        self.gun4 = [self.x,self.y-75]


    def update(self,pos):
        mouse_x = pos[0]
        mouse_y = pos[1]
        x_dist = self.x - mouse_x
        y_dist = self.y - mouse_y
        radius = math.hypot(x_dist,y_dist)
        angle = math.atan2(y_dist,x_dist)
        gun2r = radius/15
        gun3r = radius/8
        gun4r = radius/6
        self.gun2 = [self.x-int(math.cos(angle)*gun2r)-int(self.rect.width/2),self.y-int(math.sin(angle)*gun2r)]
        self.gun3 = [self.x-int(math.cos(angle)*gun3r)-int(self.rect.width/2),self.y-int(math.sin(angle)*gun3r)]
        self.gun4 = [self.x-int(math.cos(angle)*gun4r)-int(self.rect.width/2),self.y-int(math.sin(angle)*gun4r)]
        self.rect.centerx = mouse_x
        self.rect.centery = mouse_y


    def draw(self,screen):
        pygame.draw.circle(screen,constants.RED,(self.gun4),20)
        pygame.draw.circle(screen,constants.BLUE,(self.gun3),30)
        pygame.draw.circle(screen,constants.RED,(self.gun2),40)
        pygame.draw.circle(screen,constants.BLUE,(self.gun1),50)
        screen.blit(self.crosshair,[self.rect.x,self.rect.y])
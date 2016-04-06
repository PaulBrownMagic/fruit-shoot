__author__ = 'brown'

import pygame, constants, os, player, food

class Button():
    font = constants.FONT_SM
    text = None
    rtext = None
    rect = None
    status = "Locked"

    def __init__(self,text,pos):
        self.text = text
        self.rtext = self.font.render(self.text,True,constants.GREY)
        self.rect = self.rtext.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if self.status == "New":
            self.rtext = self.font.render(self.text,True,constants.RED)
        elif self.status == "Played":
            self.rtext = self.font.render(self.text,True,constants.BLUE)

    def draw(self,screen):
        screen.blit(self.rtext,(self.rect.x,self.rect.y))

class Menu():
    background = pygame.image.load(os.path.join('images', 'starburst_green.png'))
    font = constants.FONT
    title = None
    level1 = None
    level2 = None
    level3 = None
    level4 = None
    time = "Menu"
    player = None
    food1 = None
    food2 = None


    def __init__(self):
        self.background = self.background.convert()
        self.player = player.Player()
        self.title = self.font.render("Fruit Shoot", True, constants.RED)
        self.player_select = Button("Select Player", (350,600))
        self.level1 = Button("Fruit in a Barrel",(200,200))
        self.level2 = Button("Raining Fruit",(300,300))
        self.level3 = Button("Fruit Pop", (400,400))
        self.level4 = Button("Fruit Flies", (500,500))
        self.level1.status = "New"
        self.food1 = food.Food()
        self.food2 = food.Food()
        self.food1.rect.x = 900
        self.food1.rect.y = 150
        self.food2.rect.x = 150
        self.food2.rect.y = 500

    def update(self,pos):
        self.player.update(pos)
        self.player_select.update()
        self.level1.update()
        self.level2.update()
        self.level3.update()
        self.level4.update()

    def shot(self,pos):
        a = None
        if self.level1.rect.collidepoint(pos):
            a = 1
        elif self.level2.rect.collidepoint(pos):
            a = 2
        elif self.level3.rect.collidepoint(pos):
            a = 3
        elif self.level4.rect.collidepoint(pos):
            a = 4
        elif self.player_select.rect.collidepoint(pos):
            a = 5
        self.food1.reset()
        self.food2.reset()
        self.food1.rect.x = 950
        self.food1.rect.y = 150
        self.food2.rect.x = 150
        self.food2.rect.y = 500
        if a: return(a)

    def draw(self,screen):
        screen.blit(self.background,(0,0))
        screen.blit(self.title, (100,50))
        self.player_select.draw(screen)
        self.level1.draw(screen)
        self.level2.draw(screen)
        self.level3.draw(screen)
        self.level4.draw(screen)
        self.food1.draw(screen)
        self.food2.draw(screen)
        self.player.draw(screen)
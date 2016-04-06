__author__ = 'brown'

import pygame, os, constants

class GUI():
    font = constants.FONT
    splat = None
    splat_rect = None
    splat_surface = None
    rect = None

    def __init__(self,color):
        splat_img = 'color_'+color+'_sm.png'
        self.splat = pygame.image.load(os.path.join('images/splats', splat_img)).convert_alpha()
        self.splat_rect = self.splat.get_rect()
        self.splat_surface = pygame.Surface(self.splat_rect.size)
        self.splat_surface.set_colorkey((0,0,0))
        self.next_level = self.font.render("OK",True,constants.GREEN)
        self.rect = self.next_level.get_rect()
        self.surface = pygame.Surface(self.rect.size)
        self.surface.set_colorkey((0,0,0))
        self.surface.blit(self.next_level,[0,0])
        self.rect = self.surface.get_rect()
        self.rect.x = constants.WIDTH/2-self.rect.width/2
        self.rect.y = 550

    def draw(self,screen,time,score,title):
        if time == 0:
            title_text = self.font.render(title,True,constants.RED)
            title_text_rect = title_text.get_rect()
            screen.blit(title_text,[constants.WIDTH/2-title_text_rect.width/2, 100])
            screen.blit(self.surface,[self.rect.x,self.rect.y])
            score_text = self.font.render("You Scored: " + str(score),True,constants.RED)
            score_text_rect = score_text.get_rect()
            screen.blit(score_text,[constants.WIDTH/2 - score_text_rect.width/2,200])
        else:
            if time < 60:
                if score < 30:
                    score_text = self.font.render(str(score),True,constants.RED)
                else:
                    score_text = self.font.render(str(score),True,constants.GREEN)
                score_text_rect = score_text.get_rect()
                self.splat_surface.blit(self.splat,[0,0])
                self.splat_surface.blit(score_text,[self.splat_rect.width/2 - score_text_rect.width/2,self.splat_rect.height/2 - score_text_rect.height/2])
                screen.blit(self.splat_surface,[constants.WIDTH - self.splat_rect.width,0])
                if time < 6:
                    countdown_text = self.font.render(str(time),True,constants.RED)
                else:
                    countdown_text = self.font.render(str(time),True,constants.GREEN)
                countdown_text_rect = countdown_text.get_rect()
                self.splat_surface.blit(self.splat,[0,0])
                self.splat_surface.blit(countdown_text,[self.splat_rect.width/2 - countdown_text_rect.width/2,self.splat_rect.height/2 - countdown_text_rect.height/2])
                screen.blit(self.splat_surface,[0,0])
            elif time < 66:
                countdown_text = self.font.render(str(time-60),True,constants.RED)
                countdown_text_rect = countdown_text.get_rect()
                self.splat_surface.blit(self.splat,[0,0])
                self.splat_surface.blit(countdown_text,[self.splat_rect.width/2 - countdown_text_rect.width/2,self.splat_rect.height/2 - countdown_text_rect.height/2])
                screen.blit(self.splat_surface,[constants.WIDTH/2 - self.splat_rect.width/2,200])
                get_ready = self.font.render("Get Ready...",True,constants.RED)
                get_ready_rect = get_ready.get_rect()
                screen.blit(get_ready,[constants.WIDTH/2-get_ready_rect.width/2, 100])
            else:
                title_text = self.font.render(title,True,constants.RED)
                title_text_rect = title_text.get_rect()
                screen.blit(title_text,[constants.WIDTH/2-title_text_rect.width/2, 100])
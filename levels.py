__author__ = 'brown'
import player,os, pygame, food, threading, gui, random
pygame.mixer.init()

class Level():
    '''Base class all levels inherit from'''
    background = None
    player = None
    foods = None
    score = 0
    gui = None
    time = None
    title = ""
    counter_beep = pygame.mixer.Sound(os.path.join('sounds', 'Blip_Select3.ogg'))
    counter_end_beep = pygame.mixer.Sound(os.path.join('sounds', 'Pickup_Coin10.ogg'))
    hit_fruit = pygame.mixer.Sound(os.path.join('sounds', 'Pickup_Coin6.ogg'))
    hit_pastry = pygame.mixer.Sound(os.path.join('sounds', 'Powerup12.ogg'))

    def __init__(self,background_img,splat_img,food_no):
        self.gui = gui.GUI(splat_img)
        self.player = player.Player()
        self.background = pygame.image.load(os.path.join('images', background_img)).convert()
        self.foods = []
        for x in range(food_no):
            x = food.Food()
            self.foods.append(x)
        self.time = 70
        t = threading.Timer(1.0,self.countdown)
        t.start()

    def countdown(self):
        self.time -= 1
        if self.time < 66 and self.time > 60:
            self.counter_beep.play()
        elif self.time == 60:
            self.counter_end_beep.play()
        if self.time < 6 and self.time > 0:
            self.counter_beep.play()
        if self.time > 0:
            t = threading.Timer(1.0,self.countdown)
            t.start()

    def shot(self,point):
        if self.time == 0:
            if self.gui.rect.collidepoint(point):
                self.time = -1
        else:
            for food in self.foods:
                if food.rect.collidepoint(point):
                    try:
                        if food.image.get_at([point[0]-food.rect.x,point[1]-food.rect.y])[3] > 0:
                            food.shot = True
                            if food.food == "fruit":
                                self.hit_fruit.play()
                                self.score += 1
                            else:
                                self.hit_pastry.play()
                                self.score -= 1
                    except:
                        pass
                        ''' food.shot = True
                        if food.food == "fruit":
                            self.hit_fruit.play()
                            self.score += 1
                        else:
                            self.hit_pastry.play()
                            self.score -= 1'''

    def update(self, pos):
        self.player.update(pos)

    def draw(self,screen):
        screen.blit(self.background,(0,0))
        self.gui.draw(screen,self.time,self.score,self.title)
        if self.time < 66:
            if self.time != 0:
                for food in self.foods:
                    food.draw(screen)
            self.player.draw(screen)

class Level1(Level):

    def __init__(self):
        Level.__init__(self,'BG_Sea.png','blue',30)
        self.title = "Fruit in a Barrel"

    def update(self, pos):
        Level.update(self,pos)
        if self.time < 60:
            for food in self.foods:
                food.update("spin")

class Level2(Level):

    def __init__(self):
        Level.__init__(self,'BG_City.png','grey',15)
        self.title = "Raining Fruit"

    def update(self, pos):
        Level.update(self,pos)
        if self.time < 60:
            for food in self.foods:
                food.update("rain")

class Level3(Level):

    def __init__(self):
        Level.__init__(self,'BG_Sky.png','white',6)
        self.title = "Fruit Pop"
        for food in self.foods:
            t = threading.Timer(random.randint(10,15),food.pop)
            t.start()
            food.shot = True

    def update(self, pos):
        Level.update(self,pos)
        if self.time < 60:
            for food in self.foods:
                food.update("pop")

class Level4(Level):

    def __init__(self):
        Level.__init__(self,'BG_Jungle_hor_rpt_1280x800.png','green',15)
        self.title = "Fruit Flies"
        for food in self.foods:
            food.shot = True
            food.seed = random.randint(0,100)

    def update(self, pos):
        Level.update(self,pos)
        if self.time < 60:
            for food in self.foods:
                food.update("sine")


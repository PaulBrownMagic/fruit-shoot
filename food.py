__author__ = 'brown'
import pygame,os,random, constants, math, threading

class Food(pygame.sprite.Sprite):
    food = None
    image = None
    rect = None
    shot = False
    pastries = [pygame.image.load(os.path.join('images/Pastries_64x72','pastry_cookie01@2x.png')),
                pygame.image.load(os.path.join('images/Pastries_64x72','pastry_cookie02@2x.png')),
                pygame.image.load(os.path.join('images/Pastries_64x72','pastry_croissant@2x.png')),
                pygame.image.load(os.path.join('images/Pastries_64x72','pastry_cupcake@2x.png')),
                pygame.image.load(os.path.join('images/Pastries_64x72','pastry_donut@2x.png')),
                pygame.image.load(os.path.join('images/Pastries_64x72','pastry_macaroon@2x.png')),
                pygame.image.load(os.path.join('images/Pastries_64x72','pastry_pie@2x.png'))     ]
    fruits = [pygame.image.load(os.path.join('images/fruit','fruit_strawberry_200.png')),
              pygame.image.load(os.path.join('images/fruit','fruit_grape_200.png')),
              pygame.image.load(os.path.join('images/fruit','fruit_watermelon_200.png')),
              pygame.image.load(os.path.join('images/fruit','fruit_pineapple_200.png')),
              pygame.image.load(os.path.join('images/fruit','icon_jungle_bananabunch.png'))  ]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.food = random.choice(["fruit","pastry"])
        if self.food == "fruit":
            self.image = random.choice(self.fruits).convert_alpha()
        else:
            self.image = random.choice(self.pastries).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,constants.WIDTH-120)
        self.rect.y = random.randint(-1000,-200)
        self.radius = random.randint(300,constants.HEIGHT)
        self.angle = (random.random())*math.pi
        self.time = 70

    def update(self,motion):
        if motion == "rain":
            if self.shot or self.rect.y > constants.HEIGHT:
                self.reset()
            else:
                self.rect.y += 3
        elif motion == "spin":
            if self.shot or self.rect.y > constants.HEIGHT:
                self.reset()
            else:
                self.angle += 0.01
                self.rect.x = int(math.cos(self.angle) * self.radius) + constants.WIDTH/2
                self.rect.y = int(math.sin(self.angle) * self.radius) + constants.HEIGHT
        elif motion == "pop":
            if self.shot:
                self.rect.y = constants.HEIGHT
        elif motion == "sine":
            if self.shot or self.rect.x > constants.WIDTH:
                self.reset()
                self.rect.y = random.randint(250,600)
                self.rect.x = random.randint(0-constants.WIDTH*2,0-self.rect.width)
                self.seed = random.randint(0,100)
            else:
                self.rect.x += 5
                self.rect.y += math.sin(self.seed/25)*5
                self.seed += 1


        else:
            pass

    def draw(self,screen):
        screen.blit(self.image,[self.rect.x,self.rect.y])

    def reset(self):
        self.shot = False
        self.rect.y = random.randint(-1000,-200)
        self.rect.x = random.randint(0,constants.WIDTH-120)
        self.radius = random.randint(300,constants.HEIGHT)
        self.angle = (random.random())*math.pi
        self.food = random.choice(["fruit","pastry"])
        if self.food == "fruit":
            self.image = random.choice(self.fruits).convert_alpha()
        else:
            self.image = random.choice(self.pastries).convert_alpha()

    def pop(self):
        t = threading.Timer(random.randint(2,6), self.pop)
        t.start()
        self.reset()
        self.rect.y = random.randint(0,constants.HEIGHT-self.rect.height)
        self.rect.x = random.randint(0,constants.WIDTH-self.rect.width)

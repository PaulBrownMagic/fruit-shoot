import pygame, levels, constants, os, sys, gc, threading, menu, selection
__author__ = 'brown'
'''
wminput -c ir_ptr MAC:ADD:RES:S

Wii Remote with IR

'''
# initialize game engine
pygame.init()
# set screen width/height and caption
size = [constants.WIDTH, constants.HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Fruit Shoot')
pygame.mouse.set_visible(False)
# initialize clock. used later in the loop.
clock = pygame.time.Clock()
font = pygame.font.Font(os.path.join('fonts', 'ccaps.ttf'), 100)
menu = menu.Menu()
level = menu
laser_ogg =  pygame.mixer.Sound(os.path.join('sounds', 'Laser_Shoot16.ogg'))
bg_track = pygame.mixer.music.load(os.path.join('music', '234011__flatfly__wo1-loop.ogg'))
pygame.mixer.music.play(-1)
# Loop until the user clicks close button
done = False
while not done:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            try:
                if level.time < 60:
                    laser_ogg.play()
                    level.shot(pygame.mouse.get_pos())
                elif level.time > 65:
                    level.time = 65
            except:
                if level.time == "Menu":
                    laser_ogg.play()
                    nav = level.shot(pygame.mouse.get_pos())
                    if nav == 1 and level.level1.status != "Locked":
                        level = levels.Level1()
                    elif nav == 2 and level.level2.status != "Locked":
                        level = levels.Level2()
                    elif nav == 3 and level.level3.status != "Locked":
                        level = levels.Level3()
                    elif nav == 4 and level.level4.status != "Locked":
                        level = levels.Level4()
                    elif nav == 5:
                        level = selection.PlayerSelect()

    # write game logic here
    pos = pygame.mouse.get_pos()
    level.update(pos)
    if level.time == -1:
        #Clear Pop Timer threads
        for obj in gc.get_objects():
            if isinstance(obj, threading.Timer):
                obj.cancel()
        if nav == 1:
            menu.level1.status = "Played"
            if menu.level2.status == "Locked" and level.score >29:
                menu.level2.status = "New"
        elif nav == 2:
            menu.level2.status = "Played"
            if menu.level3.status == "Locked" and level.score >29:
                menu.level3.status = "New"
        elif nav == 3:
            if menu.level4.status == "Locked" and level.score >29:
                menu.level4.status = "New"
            menu.level3.status = "Played"
        elif nav == 4:
            menu.level4.status = "Played"
        level = menu
    # clear the screen before drawing
    screen.fill((255, 255, 255))
    # write draw code here
    level.draw(screen)
    # display what is drawn. This might change.
    pygame.display.update()
    # run at 60 fps
    clock.tick(constants.FPS)

# cancel all active timer threads, close the window and quit
for obj in gc.get_objects():
    if isinstance(obj, threading.Timer):
        obj.cancel()
pygame.quit()
sys.exit()

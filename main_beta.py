'''
This is the main file for beta release

If any changes are made, please update descriptions

beta v 1.00 Basic updating 

@author - Team Perpendicular

sources:

background: "Cool Background Images"/ "http://bsa-troop621.org/"
beep noise: http://www.soundjig.com/pages/soundfx/beeps.html
background music: "Trance Techno" by MrTranceful https://www.youtube.com/watch?v=BNHZNP9Pl4k
'''

import pygame, random
from pygame.locals import *
from Parallel import *
from globals import *
from win import *
from highscore import *

'''beginning of game'''
#initializing pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('PARALLEL')

#global variables
font = pygame.font.Font(None, 36)
screen_size = (1280,800)
origin = (0,0)
iterator = 0

# Keep track of attempts.
attempts = 1

#defining classes/methods
class gameMenu():
    def __init__(self, screen, highlighter_left, highlighter_right): 
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.images_data = []
        self.key = 0
        
        #getting dimension of selection highlighters
        self.highlighter_left = highlighter_left
        self.highlighter_right = highlighter_right
        self.width_hl = highlighter_left.get_rect().width
        self.height_hl = highlighter_left.get_rect().height
        
        #FPS
        self.clock = pygame.time.delay(100)
        
    def reset(self):
        del self.images_data[:]
        self.key = 0
        
    
    def playBGM(self):
        #plays background music
        self.backgroundmusic.play(-1,0)
        
    def toggleSound(self, iterator, soundfile):
        if (iterator % 2) == 0:                
            soundfile.set_volume(0.0)
        elif (iterator % 2) == 1:
            soundfile.set_volume(1.0)
            
    def soundOff(self, soundfile):
        soundfile.set_volume(0.0)
        
    def soundOn(self, soundfile):
        soundfile.set_volume(1.0)
        
    #displays background image onto screen     
    def displayMenu(self):
        screen.blit(background_image, origin)
    
    #displays instructions background    
    def displayInstructionsMenu(self):
        screen.blit(instructionsmenu_image, origin)
        
    #displays pause menu
    def displayPauseMenu(self):
        screen.blit(pausemenu_image, origin)
        
    #displays options for screen
    def displayOptions(self, images):
        #loops through all the images in array
        for index, image in enumerate(images):
            width = image.get_rect().width
            height = image.get_rect().height
            
            #centering the images x-axis
            posx = (self.screen_width / 2) - (width / 2)
            
            #assigning y-coordinates for images
            height_images = len(images) * height 
            posy = (self.screen_height / 2) - (height_images / 4) + (index * height / 2)
            
            self.images_data.append([image, (width, height), (posx, posy)])
        
        #space the options vertically
        for image, (width, height), (posx, posy) in self.images_data:
            self.screen.blit(image, (posx, posy))
    
    #checks which is selected
    def selectionDisplay(self, iterator, buttonSound):
        self.clock
        if self.key == 1:
            if iterator != 0:
                iterator = iterator - 1
                #plays music
                '''Music needs to be fixed'''
                buttonSound.play(0,0) 
        if self.key == 2:
            if iterator != len(self.images_data) - 1:
                iterator = iterator + 1
                #plays music
                buttonSound.play(0,0) 
        posy_hl = self.images_data[iterator][2][1] - 10
    
        posx_hlL = (self.screen_width / 2) - (self.images_data[iterator][1][0] / 3) - self.width_hl
        posx_hlR = (self.screen_width / 2) + (self.images_data[iterator][1][0] / 3) 
        
        self.screen.blit(self.highlighter_left, (posx_hlL, posy_hl))
        self.screen.blit(self.highlighter_right, (posx_hlR, posy_hl))
        return iterator
                                       
                                           
    #checks to see if an option is selected
    def checkSelect(self, buttonSound):
        if self.key == 3:
            select = True
            buttonSound.play(0,0)
            return select

    def checkInput(self):
        self.clock
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if key[pygame.K_UP]:
                self.key = 1
            elif key[pygame.K_DOWN]:
                self.key = 2
            elif key[pygame.K_RETURN]:
                self.key = 3
            elif key[pygame.K_ESCAPE]:
                self.key = 4
        #displays pause menu
    def displayWin(self):
        screen.blit(winbackground, origin)
        
    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state_2 = False
                state_1 = False
                state = False
                pygame.quit()
            elif self.key == 4:
                state_2 = False
                state_1 = False
                state = False
                pygame.quit()

'''LOADING'''
#initializing screen
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

#loading background image
background_image = pygame.image.load("title_background.png").convert()

#loading select highlighter
highlighter_left = pygame.image.load("highlighter_left.png").convert_alpha()
highlighter_right = pygame.image.load("highlighter_right.png").convert_alpha()

#load main menu screen
play_image = pygame.image.load("play.png").convert_alpha()
settings_image = pygame.image.load("settings.png").convert_alpha()
instructions_image = pygame.image.load("instructions.png").convert_alpha()
loadfile_image = pygame.image.load("loadfile.png").convert_alpha()
highscores_image = pygame.image.load("highscores.png").convert_alpha()
quit_image = pygame.image.load("quit.png").convert_alpha()

#load play menu screen
easy_image = pygame.image.load("easy.png").convert_alpha()
medium_image = pygame.image.load("medium.png").convert_alpha()
hard_image = pygame.image.load("hard.png").convert_alpha()

#load settings menu screen
display_image = pygame.image.load("display.png").convert_alpha()
sound_image = pygame.image.load("sound.png").convert_alpha()
customization_image = pygame.image.load("customization.png").convert_alpha()
defaultsettings_image = pygame.image.load("defaultsettings.png").convert_alpha()
saveandreturn_image = pygame.image.load("saveandreturn.png").convert_alpha()

#load sound options @settings menu screen
vsound_image = pygame.image.load("vsound.png").convert_alpha()
xsound_image = pygame.image.load("xsound.png").convert_alpha()
vsoundeffects_image = pygame.image.load("vsoundeffects.png").convert_alpha()
xsoundeffects_image = pygame.image.load("xsoundeffects.png").convert_alpha()
vbgm_image = pygame.image.load("vbgm.png").convert_alpha()
xbgm_image = pygame.image.load("xbgm.png").convert_alpha()

#load instructions menu image
instructionsmenu_image = pygame.image.load("instructions_menu.png").convert_alpha()

#pausemenu
pausemenu_image = pygame.image.load("pausemenu.png").convert()
backtogame_image = pygame.image.load("backtogame.png").convert_alpha()
tomainmenu_image = pygame.image.load("tomainmenu.png").convert_alpha()
savemap_image = pygame.image.load("savemap.png").convert_alpha()

#customization menu
blue_image = pygame.image.load("blue.png").convert_alpha()
yellow_image = pygame.image.load("yellow.png").convert_alpha()
pink_image = pygame.image.load("pink.png").convert_alpha()
vblue_image = pygame.image.load("vblue.png").convert_alpha()
vyellow_image = pygame.image.load("vyellow.png").convert_alpha()
vpink_image = pygame.image.load("vpink.png").convert_alpha()
#loading background music
pygame.mixer.music.load("Soundtrack2.wav")
backgroundmusic = pygame.mixer.Sound("Soundtrack2.wav")

#loading button sound
pygame.mixer.music.load("buttonSound.wav")
buttonSound = pygame.mixer.Sound("buttonSound.wav")

#array for menus
mainmenu_images = [play_image, settings_image, instructions_image, loadfile_image, quit_image]
playmenu_images = [easy_image, medium_image, hard_image, saveandreturn_image]
settings_images = [display_image, sound_image, customization_image, defaultsettings_image, saveandreturn_image]
sound_images = [vsound_image, vbgm_image, vsoundeffects_image, saveandreturn_image]
pausedmenu_images = [backtogame_image, savemap_image, tomainmenu_image]
display_images = [saveandreturn_image]
customization_images = [vblue_image, yellow_image, pink_image, saveandreturn_image]

instructions_images = [saveandreturn_image]


'''main code'''
#initializing state
state = True
FS = False
global STATE
STATE = True
speed = 15

#initializing counters
i = 0
j = 0 
k = 0
l = 0

a = 0
b = 0
c = 0



#plays background music
backgroundmusic.play(-1,0)

#main loop
while state == True:
    STATE = True
    state_1 = True
    state_2 = True
    #main menu
    #initialize class
    gm = gameMenu(screen, highlighter_left, highlighter_right)
    gm.displayMenu()
    gm.displayOptions(mainmenu_images)
    gm.checkInput()
    iterator = gm.selectionDisplay(iterator, buttonSound)
    select = gm.checkSelect(buttonSound)
    
    if a > 0:
        gm.soundOn(backgroundmusic)
    
    while select == True:
        #resets variables for new loop
        select = False
        gm.reset()
        if iterator == 0:
            '''play menu'''
            iterator = 0
            while state_1 == True:
                gm = gameMenu(screen, highlighter_left, highlighter_right)
                gm.displayMenu()
                gm.displayOptions(playmenu_images)
                gm.checkInput()
                iterator = gm.selectionDisplay(iterator, buttonSound)
                select = gm.checkSelect(buttonSound)
                
                while select == True:
                    select = False
                    
                    gm.reset()
                    
                    if iterator == 0:
                            
                        gm.soundOff(backgroundmusic)
                        LEVEL = 1
                        
                        # Generate random array.
                        array = []
                        for x in xrange(20):
                            array.append( [random.randint(1,9), random.randint(1,3)])
                        
                        # Game.
                        while STATE == True and LEVEL < 4:
                            game  = Game(LEVEL, array, attempts, speed, color)
                            LEVEL = game.lvl
                            STATE = game.gameState
                            attempts = game.attempts
                            state_1 = game.state_1
                            OBS.empty()
                            iterator = 0
                            if LEVEL > 3:
                                WSTATE = True
                                while WSTATE == True:
                                    gm = gameMenu(VIEW, highlighter_left, highlighter_right)
                                    gm.displayWin()
                                    gm.displayOptions(winmenu_images)
                                    gm.checkInput()
                                    iterator = gm.selectionDisplay(iterator, buttonSound)
                                    select = gm.checkSelect(buttonSound)
                                            
                                    if select == True:
                                        if iterator == 0:
                                            WSTATE = False
                                            STATE = False
                                        elif iterator == 1:
                                            WSTATE = False
                                            STATE = False
                                            state_1 = False
                                            
                                    pygame.display.update()         
                    elif iterator == 1:
                        '''medium'''
                        #ADJUST SPEED HERE
                        a = a + 1
                        
                        gm.soundOff(backgroundmusic)
                        LEVEL = 1
                        OBS.empty()

                        array = []
                        for x in xrange(20):
                            array.append( [random.randint(1,9), random.randint(1,3)])
                            
                        while STATE == True and LEVEL < 4:
                            
                            game  = Game(LEVEL, array, attempts, speed + 10, color)
                            LEVEL = game.lvl
                            STATE = game.gameState
                            attempts = game.attempts
                            state_1 = game.state_1
                            OBS.empty()
                            iterator = 0
                            if LEVEL > 3:
                                WSTATE = True
                                while WSTATE == True:
                                    gm = gameMenu(VIEW, highlighter_left, highlighter_right)
                                    gm.displayWin()
                                    gm.displayOptions(winmenu_images)
                                    gm.checkInput()
                                    iterator = gm.selectionDisplay(iterator, buttonSound)
                                    select = gm.checkSelect(buttonSound)
                                            
                                    if select == True:
                                        if iterator == 0:
                                            WSTATE = False
                                            STATE = False
                                        elif iterator == 1:
                                            WSTATE = False
                                            STATE = False
                                            state_1 = False
                                            
                                    pygame.display.update()  
                    elif iterator == 2:
                        '''hard'''
                        #ADJUST SPEED HERE
                        a = a + 1
                        gm.soundOff(backgroundmusic)
                        LEVEL = 1
                        OBS.empty()
                        
                        array = []
                        for x in xrange(20):
                            array.append( [random.randint(1,9), random.randint(1,3)])

                        while STATE == True and LEVEL < 4:
    
                            game  = Game(LEVEL, array, attempts, speed + 20, color)
                            LEVEL = game.lvl
                            STATE = game.gameState
                            attempts = game.attempts
                            state_1 = game.state_1
                            OBS.empty()
                            iterator = 0
                            if LEVEL > 3:
                                WSTATE = True
                                while WSTATE == True:
                                    gm = gameMenu(VIEW, highlighter_left, highlighter_right)
                                    gm.displayWin()
                                    gm.displayOptions(winmenu_images)
                                    gm.checkInput()
                                    iterator = gm.selectionDisplay(iterator, buttonSound)
                                    select = gm.checkSelect(buttonSound)
                                            
                                    if select == True:
                                        if iterator == 0:
                                            WSTATE = False
                                            STATE = False
                                        elif iterator == 1:
                                            WSTATE = False
                                            STATE = False
                                            state_1 = False
                                            
                                    pygame.display.update()
                    elif iterator == 3:
                        state_1 = False
                        iterator = 0
                
                gm.quit()
                
                pygame.display.update()
                
        elif iterator == 1:
            '''Settings Menu'''
            iterator = 0
            while state_1 == True:
                gm = gameMenu(screen, highlighter_left, highlighter_right)
                gm.displayMenu()
                gm.displayOptions(settings_images)
                gm.checkInput()
                iterator = gm.selectionDisplay(iterator, buttonSound)
                select = gm.checkSelect(buttonSound)
                
                while select == True:
                    #resets variables for new loop
                    select = False
                    state_2 = True
                    gm.reset()
                    '''Display'''
                    if iterator == 0:
                        while state_2 == True:
                            gm = gameMenu(screen, highlighter_left, highlighter_right)
                            gm.displayMenu()
                            gm.displayOptions(display_images)
                            gm.checkInput()
                            iterator = gm.selectionDisplay(iterator, buttonSound)
                            select = gm.checkSelect(buttonSound)
                            
                            '''enter options'''
                            while select == True:
                                select = False
                                if iterator == 0:
                                    state_2 = False
                                    
                            
                            pygame.display.update()
                    elif iterator == 1:
                        iterator = 0
                        '''sound'''
                        while state_2 == True:
                            gm = gameMenu(screen, highlighter_left, highlighter_right)
                            gm.displayMenu()
                            gm.displayOptions(sound_images)
                            gm.checkInput()
                            iterator = gm.selectionDisplay(iterator, buttonSound)
                            select = gm.checkSelect(buttonSound)
                            gm.quit()
                            pygame.display.update() 
                            
                            while select == True:
                                select = False
                                if iterator == 0:
                                    gm.reset()
                                    '''toggle sound'''
                                    gm.toggleSound(j, backgroundmusic)
                                    gm.toggleSound(j, buttonSound)
                                    
                                    j = j + 1
                                elif iterator == 1:
                                    gm.reset()
                                    '''toggle bgm'''
                                    gm.toggleSound(k, backgroundmusic)
                                    
                                    k = k + 1
                                elif iterator == 2:
                                    gm.reset()
                                    '''toggle sound effects'''
                                    gm.toggleSound(l, buttonSound)
                                    l = l + 1
                                elif iterator:
                                    '''save and return'''
                                    state_2 = False
                                    iterator = 0
                            
                                if (j % 2) == 0:
                                    if (k % 2) == 0:
                                        if (l % 2) == 0:
                                            sound_images = [vsound_image, vbgm_image, vsoundeffects_image, saveandreturn_image]
                                        else:
                                            sound_images = [vsound_image, vbgm_image, xsoundeffects_image, saveandreturn_image]
                                    else:
                                        if (l % 2) == 0:
                                            sound_images = [vsound_image, xbgm_image, vsoundeffects_image, saveandreturn_image]
                                        else:
                                            sound_images = [vsound_image, xbgm_image, xsoundeffects_image, saveandreturn_image]
                                else:
                                    if (k % 2) == 0:
                                        if (l % 2) == 0:
                                            sound_images = [xsound_image, vbgm_image, vsoundeffects_image, saveandreturn_image]
                                        else:
                                            sound_images = [xsound_image, vbgm_image, xsoundeffects_image, saveandreturn_image]
                                    else:
                                        if (l % 2) == 0:
                                            sound_images = [xsound_image, xbgm_image, vsoundeffects_image, saveandreturn_image]
                                        else:
                                            sound_images = [xsound_image, xbgm_image, xsoundeffects_image, saveandreturn_image]
                                gm.quit()
                                pygame.display.update() 
                    elif iterator == 2:
                        '''customization'''
                        iterator = 0
                        while state_2 == True:
                            gm = gameMenu(screen, highlighter_left, highlighter_right)
                            gm.displayMenu()
                            gm.displayOptions(customization_images)
                            gm.checkInput()
                            iterator = gm.selectionDisplay(iterator, buttonSound)
                            select = gm.checkSelect(buttonSound)
                            
                            while select == True:
                                select = False
                                if iterator == 0:
                                    customization_images = [vblue_image, yellow_image, pink_image, saveandreturn_image]
                                    color = 0
                                    #Game.color = color
                                elif iterator == 1:
                                    customization_images = [blue_image, vyellow_image, pink_image, saveandreturn_image]
                                    color = 1
                                    #Game.color = color
                                elif iterator == 2:
                                    color = 2
                                    #Game.color = color
                                    customization_images = [blue_image, yellow_image, vpink_image, saveandreturn_image]
                                elif iterator == 3:
                                    state_2 = False
                                    iterator = 0
                            pygame.display.update()
                    elif iterator == 3:
                        '''default settings'''
                        #display back to default
                        screen = screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                        #sound back to default
                        sound_images = [vsound_image, vbgm_image, vsoundeffects_image, saveandreturn_image]
                        customization_images = [vblue_image, yellow_image, pink_image, saveandreturn_image]
                        buttonSound.set_volume(1.0)
                        backgroundmusic.set_volume(1.0)
                        j = 0
                        k = 0
                        l = 0
                                  
                    elif iterator == 4:
                        '''Save and return'''
                        state_1 = False
                        iterator = 0
            
                #setting up ways to quit game
                gm.quit()
                            
                pygame.display.update()
                
        elif iterator == 2:
            '''instructions'''
            iterator = 0
            while state_1 == True:
                gm = gameMenu(screen, highlighter_left, highlighter_right)
                gm.displayInstructionsMenu()
                gm.displayOptions(instructions_images)
                gm.checkInput()
                iterator = gm.selectionDisplay(iterator, buttonSound)
                select = gm.checkSelect(buttonSound)
                
                while select == True:
                    select = False
                    state_1 = False
                    iterator = 0
                    
                
                gm.quit()
                
                pygame.display.update()
        elif iterator == 3:
            "load file"
            from save import *        
        elif iterator == 4:
            select = False
            state = False
        
    pygame.display.update()
    
    #setting up ways to quit game
    gm.quit()
    
pygame.quit()




        
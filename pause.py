import pygame
from pygame.locals import *
'''essential images loaded'''
pausemenu_image = pygame.image.load("pausemenu.png").convert()
backtogame_image = pygame.image.load("backtogame.png").convert_alpha()
tomainmenu_image = pygame.image.load("tomainmenu.png").convert_alpha()
savemap_image = pygame.image.load("savemap.png").convert_alpha()

#loading button sound
pygame.mixer.music.load("buttonSound.wav")
buttonSound = pygame.mixer.Sound("buttonSound.wav")

#loading select highlighter
highlighter_left = pygame.image.load("highlighter_left.png").convert_alpha()
highlighter_right = pygame.image.load("highlighter_right.png").convert_alpha()

pausedmenu_images = [backtogame_image, savemap_image, tomainmenu_image]

#initializing pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('PARALLEL')
#global variables
screen_size = (1280,800)
origin = (0,0)
iterator = 0
screen = pygame.display.set_mode(screen_size, 0, 32)


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
    
    def playBGM(self):
        #plays background music
        self.backgroundmusic.play(-1,0)
        
    def toggleSound(self, iterator, soundfile):
        if (iterator % 2) == 0:                
            soundfile.set_volume(0.0)
        elif (iterator % 2) == 1:
            soundfile.set_volume(1.0)
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
    
    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state_2 = False
                state_1 = False
                state = False
            elif self.key == 4:
                state_2 = False
                state_1 = False
                state = False

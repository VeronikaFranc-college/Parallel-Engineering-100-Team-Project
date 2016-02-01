'''
Obstacle is the main class that encompasses all traps in Parallel.
Created on Feb 10, 2015

@author: Joey Franc
@since:  March 17, 2015  v0.0.3
    Functions properly.
'''



import os, pygame
from pygame.locals import *
from globals import *
pygame.init()



class Obstacle(pygame.sprite.Sprite):
    '''
    Abstract class Obstacle contains subclasses Spike and Plat
    '''
    
    def __init__(self, x, y, lvl, container, currentLevel, speed):
        ''' 
        Constructor for an Obstacle
        
        @param x: The initial x coordinate of the trap.
        @param y: The initial y coordinate of the trap.
        @param lvl: Which level the trap spawns on.
        @param container:  A sprite Group that is used to keep track of the sprite.
        @param currentLevel:  The level that the player is currently on.
        '''       
        
        # INITIALIZE PARENT CLASS
        pygame.sprite.Sprite.__init__(self)
        
    def delete(self):
        '''Delete the object when it is no longer on screen'''
        
        self.kill()    
        del self
        
        

class Spike(Obstacle, pygame.sprite.Sprite):
    '''
    Spikes have a thinner hitbox than platforms, but CANNOT be touched in anyway.
    '''
    
    def __init__(self, x, y, lvl, container, cLevel, speed):
        '''Loads the image and blits it onto the surface.  Also defines the rect.'''
        global VIEW
        
        # Guard input
        if lvl > 3:
            lvl = lvl-3
            
        if lvl > cLevel:
            return
        
        # INITIALIZE PARENT CLASS
        Obstacle.__init__(self, x, y, lvl, container, cLevel, speed)
        self.speed = speed
        
        # LOAD SPRITE
        self.image = pygame.image.load('Spike.png')
        self.rect = pygame.Rect(1290 + x*40, (lvl)*270 - 85 - y*40, 20, 35) # Basically adjusts each spike to be level with the ball depending on the level.
        self.add(container)

    def move(self):
        
        # global to match the SPEED of the background.
        self.rect = self.rect.move(-self.speed, 0)
        VIEW.blit(self.image, [self.rect.left-10,self.rect.top-5])



class Plat (Obstacle):
    
    def __init__(self, x, y, lvl, container, cLevel):
        '''Loads the image and blits it onto the surface.  Also defines the rect.'''        
        global VIEW
        
        # Guard input
        if lvl > 3:
            lvl = lvl-3
            
        if lvl > cLevel:
            return
        
        # INITIALIZE PARENT CLASS
        Obstacle.__init__(self, x, y, lvl, container, cLevel)
        
        # LOAD SPRITE
        self.image = pygame.image.load('Platform.png')
        self.rect = pygame.Rect(x, y+(lvl-1)*150, 40, 40)
        self.add(container)
        VIEW.blit(self.image, self.rect.topleft)
        
    def move(self):
        
        #global SPEED # global to match the SPEED of the background.
        self.rect = self.rect.move(-SPEED, 0)
        VIEW.blit(self.image, self.rect.topleft)
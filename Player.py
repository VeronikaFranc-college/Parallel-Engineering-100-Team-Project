'''
Created on Feb 17, 2015

A proper player class.

@author: Niket, Joey
@version: 0.0.1 Feb 17, 2015
'''
import os, pygame
from pygame.locals import *
from globals import *
from Obstacle import *

class Player(pygame.sprite.Sprite):
    '''
    An instance of Player is a single player sprite on the map.  Multiple
    Player Sprites means multiple Player instances.
    '''
    
    def __init__(self, lvl, fn, speed):
        '''
        Constructs a player at the specified level.
        @param lvl: Which level the player will spawn on.
        @param fn:  The filname of the player's sprite.
        '''
        
        pygame.sprite.Sprite.__init__(self)
        
        '''PROPERTIES'''
        self.speed = speed
        self.jumpCount = 0
        self.isJumping = False
        self.willJump  = False
        self.gravity = 2.0*self.speed*self.speed*ARCHEIGHT[1]/(ARCHEIGHT[0]*ARCHEIGHT[0]) # 2self.speed^2*Max[y]/MAX[z]^2
        self.velocity = 0
        self.currentSprite = 0
        self.images = []
        
        '''Sprite handling'''
        # Load the image
        self.parent = pygame.image.load(fn).convert()
        width = self.parent.get_width()
        for i in xrange((width/40)):
            self.images.append(self.parent.subsurface( pygame.Rect(i*40, 0, 40, 40) ))
            self.images[i].set_colorkey((0,0,0))
        self.image = self.images[0]
        
        
        #makes black color around ball transparent
        self.image.set_colorkey((0,0,0)) 
        # set the rectangle defined for this image for collision detection and position tracking
        self.rect = pygame.Rect(60, (lvl)*270 - 90, 40, 40)
        self.yOrig = self.rect.top
        VIEW.blit(self.image, self.rect.topleft)
        
        
        
    def jump(self):
        '''
        Makes the player jump in the air relative to global self.speed.
        
        Uses Euler's method to imitate actual gravity.
        '''
                
        self.velocity += self.gravity
        self.rect.top += self.velocity
        # Stop jumping when appropriate.
        if ( self.rect.top >= self.yOrig ):
            
            self.rect.top = self.yOrig
            if self.willJump:
                self.velocity = -2.0*self.speed*ARCHEIGHT[1]/ARCHEIGHT[0]
            else:
                self.isJumping = False
    
            
            
    def getCollision(self, Obstacle):
        '''
        Ends the game if the player collides with an obstacle.
        '''
        if pygame.sprite.collide_rect(self, Obstacle):
            STATE = False
            
            
            
    def updateSprite(self):
        '''
        Update the image to create the illusion of animation
        '''
        self.image.set_colorkey((0,0,0)) 
        self.currentSprite += 1
        self.image.set_colorkey((0,0,0)) 
        if self.currentSprite+1 > len(self.images):
            self.currentSprite = 0
            self.image = self.images[self.currentSprite]
        else:
            self.image = self.images[self.currentSprite]
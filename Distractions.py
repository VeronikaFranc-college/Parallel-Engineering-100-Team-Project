'''
Created on Apr 19, 2015

@author: Joey
'''

import os, pygame, random
from pygame.locals import *
from globals import *



'''
SOUND EFFECTS COURTESY OF:
"Buzz Grid Sounds," by claudeb, http://opengameart.org/content/buzz-grid-sounds
'''



class Projectile(pygame.sprite.Sprite):
    '''
    Aesthetic projectile that moves at random speeds.
    '''


    def __init__(self, container):
        '''
        Constructor
        '''
        
        
        self.updateTimer = 4
        
        # Init parent class
        pygame.sprite.Sprite.__init__(self)
        
        # Set an appropriate random speed.
        self.vel = random.randint(int(SPEED/5), SPEED*3)
        
        # Load sprite and rect
        self.parent = pygame.image.load('star.png').convert()
        self.images = [self.parent.subsurface( pygame.Rect( 0, 0, 20, 20) ), 
                       self.parent.subsurface( pygame.Rect(20, 0, 20, 20) )]
        self.current = 0
        self.image = self.images[0]
        
        # Spawn and add to container
        self.rect = pygame.Rect(1280, random.randint(0, 760), 20, 20)
        self.add(container)
        
        
        
    def delete(self):
        '''Delete the object when it is no longer on screen'''
        
        self.kill()    
        del self
    
    
    
    def move(self):
        '''Update the position of the star on-screen'''
        
        self.updateTimer -= 1
        
        if self.updateTimer <= 0:
            self.updateTimer = 4
            self.current += 1
            self.image = self.images[self.current%2]
        
        self.rect = self.rect.move(-self.vel, -1)
        VIEW.blit(self.image, self.rect.topleft)
        
        if self.rect.right <= 0 or self.rect.top >= 800:
            self.delete()
            
            
            
class Sound():
    '''
    Aesthetic sound that goes off every 4 to 15 seconds.
    '''
    
    def __init__(self):
        
        self.count = random.randint(40, 200)
        self.sound1 = pygame.mixer.Sound('bzzzt.wav')
        self.sound2 = pygame.mixer.Sound('crash.wav')
        self.sound3 = pygame.mixer.Sound('thunk.wav')
        
     
        
    def countdown(self):
        
        self.count -= 1
        if self.count <= 0:
            self.count = random.randint(80, 300)
            sound = random.randint(1,3)
            if sound is 1:
                self.sound1.play()
            elif sound is 2:
                self.sound2.play()
            else:
                self.sound3.play()
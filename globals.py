'''
This file contains all global variables in Parallel.
These are the set standards from which all properties of the game derive.

Please import this file in all modules.

Created on March 20, 2015

@author: Joey
'''
import pygame 
from pygame.locals import *



'''ALL GLOBALS'''
global SPEED, VIEW, STATE, OBS, ARCHEIGHT, FPS, LEVEL, SCORE, ATTEMPTS

# Constants
SPEED = 20  # The default speed of in-game objects.  (SPEED * FPS) = Pixels/Second
FPS = 20 # Frames per Second
ARCHEIGHT = [160, 200]

VIEW  = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # The default screen size is 1280 pixels wide by 800 pixels.
OBS = pygame.sprite.Group() # The collection of active sprites.

# Variables  .
LEVEL = 1
SCORE = 0
ATTEMPS = 0



'''How do I import this file?'''
    # Step 1:  Put global.py in the same folder as your files.
    # Step 2:  Write 'from globals import *' at the top of your files. '''
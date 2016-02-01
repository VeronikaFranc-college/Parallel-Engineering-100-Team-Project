'''
Created on Feb 10, 2015

@author: Joey

@version: 
'''

import pygame
from pygame.locals import *
from globals import *
from Obstacle import *

global OBS, STATE, FILECOMPLETE, FPS


def combos(seed, cLevel, speed):
    '''
    combos spawns a grouping of the 2 types of Obstacles to make the game more interesting.
    Think of this function as a menu, and you're ordering delicious obstacles.
    
    @param seed  A two element array containing the trap combo in [0] and the level it spawns on in [1].
    @param cLevel:  The level the player is currently on.
    
    @return How many "spaces" the game should wait before spawning another trap.  In other words, the game
    will not spawn another trap until all traps have moved 40 pixels per "space" delay.
    '''

    case = seed[0]
    lvl =  seed[1]-1 #Minus 1 by convention.
    
    if case == 0:
        STATE = False
        return 0
    
    elif case == 1:
        Spike( 0, 0, 1+lvl, OBS, cLevel, speed )
        return 1
    
    elif case == 2:
        Spike( 0, 0, 1+lvl, OBS, cLevel, speed )
        Spike( 4, 0, 2+lvl, OBS, cLevel, speed )
        return 6
    
    elif case == 3: 
        Spike( 0, 0, 1+lvl, OBS, cLevel, speed )
        Spike( 0, 1, 2+lvl, OBS, cLevel, speed )
        return 4
    
    elif case == 4: 
        Spike( 0, 0, 1+lvl, OBS, cLevel, speed )
        Spike( 4, 0, 2+lvl, OBS, cLevel, speed )
        Spike( 5, 0, 3+lvl, OBS, cLevel, speed )
        return 7
    
    elif case == 5: 
        Spike( 1, 0, 1+lvl, OBS, cLevel, speed )
        Spike( 1, 1, 1+lvl, OBS, cLevel, speed )
        Spike( 2, 0, 2+lvl, OBS, cLevel, speed )
        Spike( 0, 0, 3+lvl, OBS, cLevel, speed )
        return 6
    
    elif case == 6: 
        Spike( 1, 0, 1+lvl, OBS, cLevel, speed )
        Spike( 0, 1, 2+lvl, OBS, cLevel, speed )
        Spike( 1, 1, 2+lvl, OBS, cLevel, speed )
        Spike( 2, 0, 3+lvl, OBS, cLevel, speed )
        return 6
    
    elif case == 7: 
        Spike( 0, 0, 1+lvl, OBS, cLevel, speed )
        Spike( 0, 1, 1+lvl, OBS, cLevel, speed )
        Spike( 1, 0, 2+lvl, OBS, cLevel, speed )
        Spike( 1, 1, 2+lvl, OBS, cLevel, speed )
        Spike( 0, 0, 3+lvl, OBS, cLevel, speed )
        return 5
    
    elif case == 8: 
        Spike( 0, 0, 1+lvl, OBS, cLevel, speed )
        Spike( 0, 1, 2+lvl, OBS, cLevel, speed )
        Spike( 1, 0, 2+lvl, OBS, cLevel, speed )
        Spike( 4, 0, 3+lvl, OBS, cLevel, speed )
        return 8
    
    elif case == 9: 
        Spike( 3, 0, 1+lvl, OBS, cLevel, speed )
        Spike( 3, 1, 1+lvl, OBS, cLevel, speed )
        Spike( 0, 0, 2+lvl, OBS, cLevel, speed )
        Spike( 4, 0, 3+lvl, OBS, cLevel, speed )
        return 8
    
    else:
        Spike( 1, 0, 2, OBS, speed )
        Spike( 2, 0, 2, OBS, speed )
        Spike( 3, 0, 2, OBS, speed )
        Spike( 4, 0, 2, OBS, speed )
        return 999
    
def initDelay(FPS):
    ''' 
    Finds a stable input for the pygame.time.delay() function that is close to the intended FPS
    
    @update OBSOLETE AS OF BETA
    '''
    actual = pygame.time.delay(1000/FPS)
    lastAttempt = 1000/FPS
    highAttempt = 4000/FPS
    lowAttempt  = 0
    # Use a binary search until the actual delay is within 15ms of the intended delay.
    while (1000/FPS)-15 > actual or actual > (1000/FPS)+15:
        if (1000/FPS)-15 > actual:
            lowAttempt  = lastAttempt
            lastAttempt = (lastAttempt + highAttempt)/2
            actual = pygame.time.delay(lastAttempt)
        elif actual > (1000/FPS)+15:
            highAttempt = lastAttempt
            lastAttempt = (lastAttempt + lowAttempt)/2
            actual = pygame.time.delay(lastAttempt)
            
    for x in xrange(3):
        test = pygame.time.delay(lastAttempt)
        if (1000/FPS)-15 > test or test > (1000/FPS)+15:
            return initDelay(lastAttempt)
        
    return lastAttempt
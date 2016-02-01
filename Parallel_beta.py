

import pygame, random
from   pygame.locals import *
from   globals import *
from   combos import *
from   Obstacle import *
from   Player import *
#from   save import*



global SPEED, VIEW, FPS, STATE, OBS, LVLCOMPLETE
pygame.init()



'''INITIALIZE'''

# The screen
back = pygame.image.load("level1.png")
VIEW.blit(back, [0,270] )

# The soundtrack
soundtrack = pygame.mixer.music
soundtrack.load('Soundtrack2.mp3')
soundtrack.play(-1, 0)

# The traps.
#array = []
#for x in xrange(20): #shows how many traps
#    array.append(random.randint(1,4))
array = [ [1,1],[2,2],[2,1],[2,3],[1,3],[2,2] ]

# Initializes the clock to create a stable frame rate and consistent new frame delay across machines..
clock = pygame.time.Clock()
global attempts
attempts = 0


def game(lvl, array):
    ''' 
    Creates a playable instance of a level.
    
    @param lvl:  Which level the player will start on.
    @param array:  The 2 dimensional array that acts as the game's "seed."  array[0] = trapCombo #, array[1] = Which level the trap spawns on.
    
    @return:  Returns lvl+1 if the player beat the level, or simply lvl if the player lost and must replay the level.
    '''
    
    # Initialize variables.
    global STATE # State of the entire game.
    lvlState = True # Win/lose state of the current level. 
    global attempts
    
    # Iterators.
    i = 0 # The index of the trap.
    t = 5 # The initial trap spawn delay
    
    # Play the game with different conditions for each level.
    if lvl == 1:

        
        back = pygame.image.load("level1.png")
        VIEW.blit(back, [0,0] )
        
        player1 = Player(1, "RealBall.png")
        
        while lvlState:
            
            pygame.display.set_caption('Attempts: %d' %attempts)
            # Standardizes FPS across platforms.
            clock.tick_busy_loop(FPS)
            
            if player1.isJumping:
                player1.jump()
                
            # Update the display
            player1.updateSprite()
            VIEW.fill([255,255,255])
            VIEW.blit(back, [0,0])
            VIEW.blit(player1.image, player1.rect.topleft)
                
            for trap in iter(OBS):
                trap.move()
                # If a trap moves into a player, they lose the level.
                if trap.rect.colliderect(player1.rect):
                    attempts += 1
                    lvlState = False
                if trap.rect.right+10 < 0: 
                    trap.delete() # Delete traps that move off of the left side.
                    if len(OBS) <= 0: # End the file when all traps have moved off the left side and advance to next level.
                        lvlState = False
                        lvl = lvl+1
            pygame.display.update()
        
            # Spawn traps when appropriate.
            if (t <= 0) and (i+1 <= len(array)):
                if (array[i][1] < 2):
                    t = combos(array[i])
                    t = t*40 + 400
                i += 1
            t -= SPEED
            
            # Command list
            for event in pygame.event.get():
                
                # If the user quits, the game exits
                if event.type == QUIT:
                    STATE = False
                    lvlState = False
                    
                # Input list
                elif event.type == pygame.KEYDOWN:
                    
                    if (event.key == pygame.K_SPACE) and (player1.isJumping == False):
                        #sound = pygame.mixer.music
                        #sound.load('JumpSound.mp3')
                        #sound.play(1,0)
                        player1.jumpCount += 1
                        player1.isJumping = True
                        player1.velocity = -2.0*SPEED*ARCHEIGHT[1]/ARCHEIGHT[0] #-2SPEED*MAX[y]/MAX[x]
                        player1.rect.top -= 1
                        
        return lvl #End of "if lvl == 1"
    
    elif lvl == 2:
            
       
        back = pygame.image.load("level2.png")
        VIEW.blit(back, [0,0] )
        
        player1 = Player(1, "RealBall.png")
        player2 = Player(2, "RealBall.png")
        
        while lvlState:

            pygame.display.set_caption('Attempts: %d' %attempts) 
            
            # Standardizes FPS across platforms.
            clock.tick_busy_loop(FPS)
            
            if player1.isJumping:
                player1.jump()
                player2.jump()
                
            # Update the display
            player1.updateSprite()
            player2.updateSprite()
            VIEW.fill([255,255,255])
            VIEW.blit(back, [0,0])
            VIEW.blit(player1.image, player1.rect.topleft)
            VIEW.blit(player2.image, player2.rect.topleft)
                
            for trap in iter(OBS):
                trap.move()
                if trap.rect.colliderect(player1.rect) or trap.rect.colliderect(player2.rect):
                    attempts += 1
                    lvlState = False
                if trap.rect.right+10 < 0: # Delete traps that move off of the left side.
                    trap.delete()
                    if len(OBS) <= 0: # End the file when all traps have moved off the left side.
                        lvlState = False
                        lvl = lvl+1
            pygame.display.update()
        
            # Spawn traps when appropriate.
            if (t <= 0) and (i+1 <= len(array)):
                if (array[i][1] < 3):
                    t = combos(array[i])
                    t = t*40 + 400
                i += 1
            t -= SPEED
            
            # Command list
            for event in pygame.event.get():
                
                # If the user quits, the game exits
                if event.type == QUIT:
                    STATE = False
                    lvlState = False
                # Input list
                elif event.type == pygame.KEYDOWN:
                    
                    if (event.key == pygame.K_SPACE) and (player1.isJumping == False):
                        #sound = pygame.mixer.music
                        #sound.load('JumpSound.mp3')
                        #sound.play(1,0)
                        player1.jumpCount += 1
                        player2.jumpCount += 1
                        player1.isJumping = True
                        player2.isJumping = True
                        player1.velocity = -2.0*SPEED*ARCHEIGHT[1]/ARCHEIGHT[0] #-2SPEED*MAX[y]/MAX[x]
                        player2.velocity = -2.0*SPEED*ARCHEIGHT[1]/ARCHEIGHT[0]
                        player1.rect.top -= 1
                        player2.rect.top -= 1
                        
        return lvl
    
    elif lvl == 3:
        
        back = pygame.image.load("level3.png")
        VIEW.blit(back, [0,0] )
        
        player1 = Player(1, "RealBall.png")
        player2 = Player(2, "RealBall.png")
        player3 = Player(3, "RealBall.png")
        
        while lvlState:

            pygame.display.set_caption('Attempts: %d' %attempts)
            # Standardizes FPS across platforms.
            clock.tick_busy_loop(FPS)
            
            if player1.isJumping:
                player1.jump()
                player2.jump()
                player3.jump()
                    
            # Update the display
            player1.updateSprite()
            player2.updateSprite()
            player3.updateSprite()
            VIEW.fill([255,255,255])
            VIEW.blit(back, [0,0])
            VIEW.blit(player1.image, player1.rect.topleft)
            VIEW.blit(player2.image, player2.rect.topleft)
            VIEW.blit(player3.image, player3.rect.topleft)
                
            for trap in iter(OBS):
                trap.move()
                if trap.rect.colliderect(player1.rect) or trap.rect.colliderect(player2.rect) or trap.rect.colliderect(player3.rect):
                    attempts += 1
                    lvlState = False
                if trap.rect.right+10 < 0: # Delete traps that move off of the left side.
                    trap.delete()
                    if len(OBS) <= 0: # End the file when all traps have moved off the left side.
                        lvlState = False
                        lvl = lvl+1
            pygame.display.update()
        
            # Spawn traps when appropriate.
            if (t <= 0) and (i+1 <= len(array)):
                t = combos(array[i])
                t = t*40 + 400
                i += 1
            t -= SPEED
            
            # Command list
            for event in pygame.event.get():
                
                # If the user quits, the game exits
                if event.type == QUIT:
                    STATE = False
                    lvlState = False
                # Input list
                elif event.type == pygame.KEYDOWN:
                    
                    if (event.key == pygame.K_SPACE) and (player1.isJumping == False):
                        #sound = pygame.mixer.music
                        #sound.load('JumpSound.mp3')
                        #sound.play(1,0)
                        player1.jumpCount += 1
                        player1.isJumping = True
                        player1.velocity = -2.0*SPEED*ARCHEIGHT[1]/ARCHEIGHT[0] #-2SPEED*MAX[y]/MAX[x]
                        player2.velocity = -2.0*SPEED*ARCHEIGHT[1]/ARCHEIGHT[0]
                        player3.velocity = -2.0*SPEED*ARCHEIGHT[1]/ARCHEIGHT[0]
                        player1.rect.top -= 1
                        player2.rect.top -= 1
                        player3.rect.top -= 1
                        
        return lvl



'''BODY'''

LEVEL = game(1, array)
OBS.empty()

while STATE and LEVEL < 4:
    
    LEVEL = game(LEVEL, array)
    OBS.empty()
    
if LEVEL > 3:
    print("You win!")
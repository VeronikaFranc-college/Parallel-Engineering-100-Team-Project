'''
Created on March 14, 2015

@author: Derek, Joey, Kevin, Niket
@version: v0.1.1
    Removed faulty player code.
    Added file importing and exporting. (Check details in save.py)
    Spikes should work entirely properly.
    Jumping follows a predictable arc.  Game running at a consistent speed on all machines is uncertain.
@todo:
    Kevin:  Integrate your new menus, add a pause function.
    Niket:  Add the ability to detect and land on top of platforms in the Player.jump() method.
    Joey:   Update spike resources, design more trap combos, create file tracking system.
    Derek:  Finish level generator, create new background resources, animate backgrounds.
@attention: 
    WHO IS ADDING THE ABILITY TO DETECT WHEN TO ADD ANOTHER LEVEL?
    
    Yes.
'''

import pygame, random
from   pygame.locals import *
from   globals import *
from   combos import *
from   Obstacle import *
from   Player import *
from   save import*



global SPEED, VIEW, STATE, OBS, FILECOMPLETE
pygame.init()



'''SETTINGS'''
VIEW.fill([255,255,255])

#Initializing the screen
back = pygame.image.load("background.png")
VIEW.blit(back, [0,270] )

'''soundtrack = pygame.mixer.music
soundtrack.load('Soundtrack2.wav')
soundtrack.play(-1, 0)'''
pygame.display.update()

array = []
for x in xrange(20): #shows how many traps
    array.append(random.randint(1,4))

player = Player(2, 'GreenBall.png')
player2 = Player(2, 'GreenBall2.png')
player3 = Player(2, 'GreenBall3.png')
player4 = Player(2, 'GreenBall4.png')
player5 = Player(2, 'GreenBall5.png')

i = 0 # The index of the trap.
t = 0 # The time delay
# loop that controls when game will stop, along with the keyboard control
while STATE == True:
      
    # Controls the framerate on Windows
    pygame.time.delay(FPS/1000)  
    
    # Update the display
    VIEW.fill([255,255,255])
    VIEW.blit(back, [0,270])
    
    VIEW.blit(player.image, player.rect.topleft)
    """VIEW.blit(player2.image, player2.rect.topleft)
    VIEW.blit(player3.image, player3.rect.topleft)
    VIEW.blit(player4.image, player4.rect.topleft)
    VIEW.blit(player5.image, player5.rect.topleft)"""
    
    # Cycle through all active sprites
    if player.isJumping:
        player.jump()
    """#if player2.isJumping:
        player2.jump()
    #if player3.isJumping:
        player3.jump()
    #if player4.isJumping:
        player4.jump()
    #if player5.isJumping:
        player5.jump()"""
    for trap in iter(OBS):
        trap.move()
        if trap.rect.colliderect(player.rect):
            STATE = False
        if trap.rect.right+10 < 0: # Delete traps that move off of the left side.
            trap.delete()
            if len(OBS) <= 0: # End the file when all traps have moved off the left side.
                FILECOMPLETE = True
                STATE = False
    pygame.display.update()
    """pygame.transform.rotate(player.image,300)
    pygame.display.update()
    pygame.transform.rotate(player.image,80)
    pygame.display.update()"""
    # Spawn traps when appropriate.
    if (t <= 0) and (i+1 <= len(array)):
        t = combos(array[i])
        t = t*40 + 400
        i += 1
    t -= SPEED
    
    
    
    
    # Controls the framerate on Windows
    pygame.time.delay(FPS/1000)  
    
    # Update the display
    VIEW.fill([255,255,255])
    VIEW.blit(back, [0,270])
    
    VIEW.fill([255,255,255])
    VIEW.blit(back, [0,270])
    
    VIEW.blit(player2.image, player2.rect.topleft)
    
    if player2.isJumping:
        player2.jump()
    
    for trap in iter(OBS):
        trap.move()
        if trap.rect.colliderect(player2.rect):
            STATE = False
        if trap.rect.right+10 < 0: # Delete traps that move off of the left side.
            trap.delete()
            if len(OBS) <= 0: # End the file when all traps have moved off the left side.
                FILECOMPLETE = True
                STATE = False
    pygame.display.update()
    
    if (t <= 0) and (i+1 <= len(array)):
        t = combos(array[i])
        t = t*40 + 400
        i += 1
    t -= SPEED
    
    
    
    
        # Controls the framerate on Windows
    pygame.time.delay(FPS/1000)  
    
    # Update the display
    VIEW.fill([255,255,255])
    VIEW.blit(back, [0,270])
    
    VIEW.fill([255,255,255])
    VIEW.blit(back, [0,270])
    
    VIEW.blit(player3.image, player3.rect.topleft)
    
    if player3.isJumping:
        player3.jump()
    
    for trap in iter(OBS):
        trap.move()
        if trap.rect.colliderect(player3.rect):
            STATE = False
        if trap.rect.right+10 < 0: # Delete traps that move off of the left side.
            trap.delete()
            if len(OBS) <= 0: # End the file when all traps have moved off the left side.
                FILECOMPLETE = True
                STATE = False
    pygame.display.update()
    
    if (t <= 0) and (i+1 <= len(array)):
        t = combos(array[i])
        t = t*40 + 400
        i += 1
    t -= SPEED
    
    
    
    
        # Controls the framerate on Windows
    pygame.time.delay(FPS/1000)  
    
    # Update the display
    VIEW.fill([255,255,255])
    VIEW.blit(back, [0,270])
    
    VIEW.fill([255,255,255])
    VIEW.blit(back, [0,270])
    
    VIEW.blit(player4.image, player4.rect.topleft)
    
    if player4.isJumping:
        player4.jump()
    
    for trap in iter(OBS):
        trap.move()
        if trap.rect.colliderect(player4.rect):
            STATE = False
        if trap.rect.right+10 < 0: # Delete traps that move off of the left side.
            trap.delete()
            if len(OBS) <= 0: # End the file when all traps have moved off the left side.
                FILECOMPLETE = True
                STATE = False
    pygame.display.update()
    
    if (t <= 0) and (i+1 <= len(array)):
        t = combos(array[i])
        t = t*40 + 400
        i += 1
    t -= SPEED
    
    
    
    
        # Controls the framerate on Windows
    pygame.time.delay(FPS/1000)  
    
    # Update the display
    VIEW.fill([255,255,255])
    VIEW.blit(back, [0,270])
    
    VIEW.fill([255,255,255])
    VIEW.blit(back, [0,270])
    
    VIEW.blit(player5.image, player5.rect.topleft)
    
    if player5.isJumping:
        player5.jump()
    
    for trap in iter(OBS):
        trap.move()
        if trap.rect.colliderect(player5.rect):
            STATE = False
        if trap.rect.right+10 < 0: # Delete traps that move off of the left side.
            trap.delete()
            if len(OBS) <= 0: # End the file when all traps have moved off the left side.
                FILECOMPLETE = True
                STATE = False
    pygame.display.update()
    
    if (t <= 0) and (i+1 <= len(array)):
        t = combos(array[i])
        t = t*40 + 400
        i += 1
    t -= SPEED
    
    
    
    
    for event in pygame.event.get():
        #if the user quits, the game exits
        if event.type == QUIT:
            STATE = False

        # Jump command.
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE) and (player.isJumping == False):
                #sound = pygame.mixer.music
                #sound.load('JumpSound.mp3')
                #sound.play(1,0)
                player.jumpCount += 1
                player2.jumpCount += 1
                player3.jumpCount += 1
                player4.jumpCount += 1
                player5.jumpCount += 1
                
                player.isJumping = True
                player2.isJumping = True
                player3.isJumping = True
                player4.isJumping = True
                player5.isJumping = True
                
                player.velocity = -2.0*SPEED*ARCHEIGHT[1]/ARCHEIGHT[0] #-2SPEED*MAX[y]/MAX[x]
                player2.velocity = -2.0*SPEED*ARCHEIGHT[1]/ARCHEIGHT[0]
                player3.velocity = -2.0*SPEED*ARCHEIGHT[1]/ARCHEIGHT[0]
                player4.velocity = -2.0*SPEED*ARCHEIGHT[1]/ARCHEIGHT[0]
                player5.velocity = -2.0*SPEED*ARCHEIGHT[1]/ARCHEIGHT[0]
                
                player.rect.top -= 1
                player2.rect.top -= 1
                player3.rect.top -= 1
                player4.rect.top -= 1
                player5.rect.top -= 1
                
# Give the player a moment to realize they died.
pygame.time.delay(500)
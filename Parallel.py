'''
Created on March 14, 2015

@author: Derek, Joey, Kevin, Niket
@version: v0.3.0
    Changed Parallel from a function to a class for easier data access.
    Check list of ivars for new list of accessible variables.
@todo:
    Niket:  Add the ability to detect and land on top of platforms in the Player.jump() method.
    Derek:  Finish level generator, create new background resources, animate backgrounds.
    
    Yes.
'''



import pygame, random
from   pygame.locals import *
from   globals import *
from   combos import *
from   Obstacle import *
from   Player import *
from   save import *
from   pause import*
from   Distractions import*

# Constants
global VIEW, FPS, STATE, OBS, PAUSE



class Game():
    ''' 
    Creates a playable instance of a level.
    '''
    
    def __init__(self, lvl, array, attempts, speed, color):
        '''
        @param lvl:  Which level the player will start on.
        @param array:  The 2 dimensional array that acts as the game's "seed."  array[0] = trapCombo #, array[1] = Which level the trap spawns on.
        @param attempts:  How many "attempts" the player has.
        
        @ivar gameState:  True when the whole program, Parallel, is running. 
        @ivar lvlState:  False when the player has failed a level and needs to restart.
        @ivar lvlComplete:  True when the player has successfully completed a level.
        @ivar lvl:  Which level the player has reached.  (1, 2, or 3)
        @ivar attempts:  How many times the player has attempted to beat the game.
        '''
    
        '''INITIALIZE'''
        
        # Initializes the clock to create a stable frame rate and consistent new frame delay across machines..
        clock = pygame.time.Clock()
        STARS = pygame.sprite.Group()
        
        # Initialize instance variables
        self.speed = speed
        self.gameState   =  True
        self.lvlState    =  True
        self.state_1 = True
        self.lvlComplete =  False
        self.lvl         =  lvl
        self.attempts    =  attempts
        self.color       = color
        
        # Initialize the soundtrack
        soundtrack = pygame.mixer.music
        soundtrack.load('Soundtrack2.wav')
        soundtrack.play(-1, 0)
        if self.color == 0: 
            ball = "BlueRing.png"
        elif self.color == 1:
            ball = "YellowRing.png"
        elif self.color == 2:
            ball = "PinkRing.png"
        else:
            ball = "BlueRing.png"
        # Iterators.
        i = 0 # The index of the trap.
        t = 5 # The initial trap spawn delay
        p = 9 # The initial star spawn delay
        
        # Sound effects
        sfx = Sound()
    
        # Play the game with different conditions for each level.
        '''Level 1'''
        if lvl == 1:
                
            player1 = Player(1, ball, self.speed)
            back = pygame.image.load("level1.png")
            VIEW.blit(back, [0,0] )
            
            while self.lvlState:
                pygame.display.set_caption('Attempts: %d' %attempts)
                # Standardizes FPS across platforms.
                clock.tick_busy_loop(FPS)
                
                if player1.isJumping:
                    player1.jump()
                    
                # Update the display
                player1.updateSprite()
                VIEW.fill([255,255,255])
                VIEW.blit(back, origin)
                VIEW.blit(player1.image, player1.rect.topleft)
                    
                for trap in iter(OBS):
                    trap.move()
                    # If a trap moves into a player, they lose the level.
                    if trap.rect.colliderect(player1.rect):
                        self.attempts += 1
                        self.lvlState = False
                    if trap.rect.right+10 < 0: 
                        trap.delete() # Delete traps that move off of the left side.
                        if len(OBS) <= 0: # End the file when all traps have moved off the left side and advance to next level.
                            self.lvlState = False
                            self.lvl += 1
                pygame.display.update()
            
                # Spawn traps when appropriate.
                if (t <= 0) and (i+1 <= len(array)):
                    if (array[i][1] < 2):
                        t = combos(array[i], lvl, self.speed)
                        t = t*40 + 400
                    i += 1
                t -= self.speed
                
                # Spawn stars randomly
                if p <= 0:
                    p = random.randint(30, 180)
                    Projectile(STARS)
                p -= 1
                    
                # Update all stars
                for star in iter(STARS):
                    star.move()
                    
                # Play sfx when appropriate
                sfx.countdown()
                
                # Command list
                for event in pygame.event.get():
                    
                    # If the users quits, the game exits
                    if event.type == QUIT:
                        self.gameState = False
                        self.lvlState  = False
                        
                    # Input list
                    elif event.type == pygame.KEYDOWN:
                        
                        if (event.key == pygame.K_SPACE) and (player1.isJumping == False):
                            #sound = pygame.mixer.music
                            #sound.load('JumpSound.mp3')
                            #sound.play(1,0)
                            player1.jumpCount += 1
                            player1.isJumping = True
                            player1.willJump  = True
                            player1.velocity = -2.0*self.speed*ARCHEIGHT[1]/ARCHEIGHT[0] #-2self.speed*MAX[y]/MAX[x]
                            player1.rect.top -= 1
                            
                        #PAUSE menu
                        elif (event.key == pygame.K_p) or (event.key == pygame.K_ESCAPE):
                            #body
                            PSTATE = True
                            iterator = 0
                            while PSTATE == True:
                                gm = gameMenu(screen, highlighter_left, highlighter_right)
                                gm.displayPauseMenu()
                                gm.displayOptions(pausedmenu_images)
                                gm.checkInput()
                                iterator = gm.selectionDisplay(iterator, buttonSound)
                                select = gm.checkSelect(buttonSound)
                                        
                                if select == True:
                                    if iterator == 0:
                                        PSTATE = False
                                    elif iterator == 1:
                                        arbitrary = 0
                                    elif iterator == 2:
                                        PSTATE = False
                                        self.lvlState  = False
                                        self.gameState = False
                                        self.state_1 = False
                                        
                                pygame.display.update()
                                
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            player1.willJump = False
                        
            if self.lvl == 2:
                import transition
            
            soundtrack.stop()
        
        #LEVEL 2#
        elif self.lvl == 2:
            back = pygame.image.load("level2.png")
            VIEW.blit(back, [0,0] )
            player1 = Player(1, ball, self.speed)
            player2 = Player(2, ball, self.speed)
            
            while self.lvlState:
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
                VIEW.blit(back, origin)
                VIEW.blit(player1.image, player1.rect.topleft)
                VIEW.blit(player2.image, player2.rect.topleft)
                    
                for trap in iter(OBS):
                    trap.move()
                    if trap.rect.colliderect(player1.rect) or trap.rect.colliderect(player2.rect):
                        self.attempts += 1
                        self.lvlState = False
                    if trap.rect.right+10 < 0: # Delete traps that move off of the left side.
                        trap.delete()
                        if len(OBS) <= 0: # End the file when all traps have moved off the left side.
                            self.lvlState = False
                            self.lvl += 1
                pygame.display.update()
            
                # Spawn traps when appropriate.
                if (t <= 0) and (i+1 <= len(array)):
                    if (array[i][1] < 3):
                        t = combos(array[i], lvl, self.speed)
                        t = t*40 + 400
                    i += 1
                t -= self.speed
                
                # Spawn stars randomly
                if p <= 0:
                    p = random.randint(30, 180)
                    Projectile(STARS)
                p -= 1
                    
                # Update all stars
                for star in iter(STARS):
                    star.move()
                    
                # Play sfx when appropriate
                sfx.countdown()
                
                # Command list
                for event in pygame.event.get():
                    
                    # If the user quits, the game exits
                    if event.type == QUIT:
                        self.gameState = False
                        self.lvlState = False
                    # Input list
                    elif event.type == pygame.KEYDOWN:
                        
                        if (event.key == pygame.K_SPACE) and (player1.isJumping == False):
                            #sound = pygame.mixer.music
                            #sound.load('JumpSound.mp3')
                            #sound.play(1,0)
                            player1.jumpCount += 1
                            player1.isJumping = True
                            player1.willJump  = True
                            player2.willJump  = True
                            player1.velocity = -2.0*self.speed*ARCHEIGHT[1]/ARCHEIGHT[0] #-2self.speed*MAX[y]/MAX[x]
                            player2.velocity = -2.0*self.speed*ARCHEIGHT[1]/ARCHEIGHT[0]
                            player1.rect.top -= 1
                            player2.rect.top -= 1
                            
                        #PAUSE menu
                        elif (event.key == pygame.K_p) or (event.key == pygame.K_ESCAPE):
                            #body
                            PSTATE = True
                            iterator = 0
                            while PSTATE == True:
                                gm = gameMenu(screen, highlighter_left, highlighter_right)
                                gm.displayPauseMenu()
                                gm.displayOptions(pausedmenu_images)
                                gm.checkInput()
                                iterator = gm.selectionDisplay(iterator, buttonSound)
                                select = gm.checkSelect(buttonSound)
                                        
                                if select == True:
                                    if iterator == 0:
                                        PSTATE = False
                                    elif iterator == 1:
                                        arbitrary = 0
                                    elif iterator == 2:
                                        PSTATE = False
                                        self.lvlState  = False
                                        self.gameState = False
                                        self.state_1 = False
                                               
                                pygame.display.update()
                                
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:                            
                            player1.willJump = False
                            player2.willJump = False
                            
            if self.lvl == 3:
                import transition
                reload(transition)
            soundtrack.stop()
        
        #LEVEL 3#
        elif self.lvl == 3:
            back = pygame.image.load("level3.png")
            VIEW.blit(back, [0,0] )
            player1 = Player(1, ball, self.speed)
            player2 = Player(2, ball, self.speed)
            player3 = Player(3, ball, self.speed)
            
            while self.lvlState:
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
                VIEW.blit(back, origin)
                VIEW.blit(player1.image, player1.rect.topleft)
                VIEW.blit(player2.image, player2.rect.topleft)
                VIEW.blit(player3.image, player3.rect.topleft)
                    
                for trap in iter(OBS):
                    trap.move()
                    if trap.rect.colliderect(player1.rect) or trap.rect.colliderect(player2.rect) or trap.rect.colliderect(player3.rect):
                        self.attempts += 1
                        self.lvlState = False
                    if trap.rect.right+10 < 0: # Delete traps that move off of the left side.
                        trap.delete()
                        if len(OBS) <= 0: # End the file when all traps have moved off the left side.
                            self.lvlState = False
                            self.lvl += 1
                pygame.display.update()
            
                # Spawn traps when appropriate.
                if (t <= 0) and (i+1 <= len(array)):
                    t = combos(array[i], lvl, self.speed)
                    t = t*40 + 400
                    i += 1
                t -= self.speed
                
                # Spawn stars randomly
                if p <= 0:
                    p = random.randint(30, 180)
                    Projectile(STARS)
                p -= 1
                    
                # Update all stars
                for star in iter(STARS):
                    star.move()
                    
                # Play sfx when appropriate
                sfx.countdown()
                
                # Command list
                for event in pygame.event.get():
                    
                    # If the user quits, the game exits
                    if event.type == QUIT:
                        self.gameState = False
                        self.lvlState = False
                    # Input list
                    elif event.type == pygame.KEYDOWN:
                        
                        if (event.key == pygame.K_SPACE) and (player1.isJumping == False):
                            #sound = pygame.mixer.music
                            #sound.load('JumpSound.mp3')
                            #sound.play(1,0)
                            player1.jumpCount += 1
                            player1.isJumping = True
                            player1.willJump  = True
                            player2.willJump  = True
                            player3.willJump  = True
                            player1.velocity = -2.0*self.speed*ARCHEIGHT[1]/ARCHEIGHT[0] #-2self.speed*MAX[y]/MAX[x]
                            player2.velocity = -2.0*self.speed*ARCHEIGHT[1]/ARCHEIGHT[0]
                            player3.velocity = -2.0*self.speed*ARCHEIGHT[1]/ARCHEIGHT[0]
                            player1.rect.top -= 1
                            player2.rect.top -= 1
                            player3.rect.top -= 1
                        
                        #PAUSE menu
                        elif (event.key == pygame.K_p) or (event.key == pygame.K_ESCAPE):
                            #body
                            PSTATE = True
                            iterator = 0
                            while PSTATE == True:
                                gm = gameMenu(screen, highlighter_left, highlighter_right)
                                gm.displayPauseMenu()
                                gm.displayOptions(pausedmenu_images)
                                gm.checkInput()
                                iterator = gm.selectionDisplay(iterator, buttonSound)
                                select = gm.checkSelect(buttonSound)
                                        
                                if select == True:
                                    if iterator == 0:
                                        PSTATE = False
                                    elif iterator == 1:
                                        arbitrary = 0
                                    elif iterator == 2:
                                        PSTATE = False
                                        self.lvlState  = False
                                        self.gameState = False
                                        self.state_1 = False
                                                                            
                                pygame.display.update()
                                
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            
                            player1.willJump = False
                            player2.willJump = False
                            player3.willJump = False
                            
            soundtrack.stop()
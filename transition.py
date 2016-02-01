import pygame
from pygame.locals import *
from globals import *

pygame.init()
pygame.display.set_caption('PARALLEL')

screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
origin = (0,0)

#load images
transition1_image = pygame.image.load("transition1.png").convert_alpha()
transition2_image = pygame.image.load("transition2.png").convert_alpha()
transition3_image = pygame.image.load("transition3.png").convert_alpha()
transition4_image = pygame.image.load("transition4.png").convert_alpha()
transition5_image = pygame.image.load("transition5.png").convert_alpha()
transition_images = [transition5_image, transition4_image, transition3_image, transition2_image, transition1_image]

def transition(images):
    for image in images:
        pygame.time.delay(1000)
        VIEW.blit(image, origin)
        pygame.display.update()
        
transition(transition_images)
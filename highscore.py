import pygame
from pygame.locals import *
import os.path

def highscore(attempts): 
    player_score = attempts
    n = 0
    i = 6
    j = 0
    array = []
    n_array = []
    s_array = []
    temp_array = []
    player_name = raw_input("Enter Your Name: ")
    with open ("highscore.txt") as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                array.append(word)
    
    array.append(player_name)
    array.append(player_score)
    
    #print(array)
    for index, element in enumerate(array):
        if index % 2 == 0:
            n_array.append(element)
        else:
            s_array.append(int(element))

            
    while i >= 0:
        print(s_array)
        index = s_array.index(min(s_array))
        temp_array.append([n_array[index], s_array[index]])
        del s_array[index]
        del n_array[index]
        i = i - 1

    os.remove('highscore.txt')
    print(temp_array)
    
    highscore_file = open("highscore.txt", 'w+')
    while j <= 6:
        highscore_file.write(temp_array[j][0])
        highscore_file.write(" ")
        temp = str(temp_array[j][1])
        highscore_file.write(temp)
        highscore_file.write("\n")
        
        j = j + 1
    

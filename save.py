'''
Save is a list of functions that allow the user to save and load
array files.

@todo:  Make the interface compatible with parallel.

Created on April 10, 2015

@author: Joey Franc
'''



import pygame
from pygame.locals import *
from globals import *



def backspace(string):
    '''
    backspace removes the final character from a string
    
    @param string: A string to have its final character removed.
    @return: The original string sans its final character.
    '''
    
    output = ''
    for s in xrange(len(string)-1):
        output = output+string[s]
        
    return output


def checkInput(string):
    '''
    checkInput checks each character in a string to make sure
    it is compatible as a file name.
    
    @param string: The string to be checked.
    @return: True if the file is compatible as a file name, False if the file is not.
    '''
    
    if string == 'fileList.txt':
        return False
    
    for s in xrange(len(string)):
        if  string[s] == '?'  or  string[s] == ':'  \
        or  string[s] == '*'  or  string[s] == '|'  \
        or  string[s] == '\"' or  string[s] == '>'  \
        or  string[s] == '<'  or  string[s] == '/'  \
        or  string[s] == '\\' or  string[s] == '\t' \
        or  string[s] == '\r' or  string[s] == '^[':
            
            print(r'Valid file names do not include "?, :, *, |, <, >, \, /"')
            return False
                
        else:
            return True      
        
    
def save(array):
    '''
    save saves an array in a .txt file.  Save will prompt the user to enter a 
    file name.  
    Using text input, save will name the .txt file under whichever name the 
    user types.
    Each element of each array will be saved on a new line in the .txt
    
    @param array: The array that will be saved in a .txt
    '''
    
    ''' Initialize the console for input'''
    pygame.init()
    font = pygame.font.SysFont("Arial", 40, True, False)
    VIEW.blit(font.render('Enter in a filename', True, [255,255,255],[0,0,0]), [0,100])
    pygame.display.update()
    
    
    fn = ''
    typing = True
        
    while typing:
    
        for event in pygame.event.get():

            # Stop typing command.
            if event.type == QUIT:
                if fn:
                    if checkInput(fn): # Only allow quitting if the user inputs a valid filename.
                        typing = False
                        
            # Input to filename.
            elif event.type == pygame.KEYDOWN:
                
                if event.key is K_BACKSPACE: # Adds backspace functionality.
                    
                    fn = backspace(fn)
                    VIEW.fill([0,0,0])
                    VIEW.blit(font.render(fn, True, [255,255,255],[0,0,0]), [0, 0])
                    pygame.display.update()
                    
                elif checkInput(event.unicode): #If the input is valid, update the screen with the filename.
                    fn = fn + event.unicode
                    VIEW.fill([0,0,0])
                    VIEW.blit(font.render(fn, True, [255,255,255],[0,0,0]), [0, 0])
                    pygame.display.update()
                    
    # Save the file under the entered filename.
    if checkInput(fn):
        currentFile = open(fn, 'w')
        log(fn)
        for i in xrange(len(array)):
            currentFile.write( str(array[i])+'\n')
            
        
    
def load(fn):
    '''
    load takes a .txt file as input and returns an array whose
    individual elements represents a single line of the file
    
    @param fn: The filename of a .txt that contains an int on each line.
    @return: An array of ints of unknown length.
    '''

    currentFile=open(fn,'r')
    array = list()
    line = currentFile.readline()
    
    while line:
        array.append(int(line))
        line = currentFile.readline()
    
    return array



def log(fn):
    '''
    Adds a filename to the master log file, 'fileList.txt'
    
    @param fn:  A string representing the filename of the .txt to be logged.
    '''
    
    # Initialize reading the log.
    currentFile = open('fileList.txt', 'r')
    oldFiles = list()
    
    # Read all previously saved files.
    line = currentFile.readline()
    while line:
        # Don't log the file if it's being overwritten.
        if line == (fn+'\n') or line == fn:
            line = currentFile.readline()
            continue
        # Log all files that have already been logged.
        else:
            oldFiles.append(line)
            line = currentFile.readline()
    
    currentFile = open('fileList.txt', 'w')        
    for i in xrange( len(oldFiles)-1 ):
        # Rewrite the fileList.txt to include the old files.
        currentFile.write( oldFiles[i] )
    # Add final two files
    if len(oldFiles) is not 0:
        currentFile.write(oldFiles[len(oldFiles)-1]+'\n')
    currentFile.write(fn)
    
def loadFiles():
    '''
    @return files:  Returns an array of all files currently stored in the log file, 'fileList.txt'
    '''
    
    currentFile = open('fileList.txt', 'r')
    files = list()
    
    # Add each line (which represents a file) to the log array.
    line = currentFile.readline()
    while line:
        files.append(line)
        line = currentFile.readline()
        
    # Remove '\n's from the file.'
    for i in xrange( len(files)-1 ):
        files[i] = backspace(files[i])
        
    return files
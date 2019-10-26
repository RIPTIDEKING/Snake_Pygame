import pygame
import random

from resorces_basic import *
from button import *
from snake import *
from apple import *
from mods import *

pygame.init()

pygame.display.set_icon(appleMain)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('slither')
pygame.display.update()




def game_intro():
    
    intro = [True]
    plBut = Button(gameDisplay,green,"Play",175,450,100,50,intro_play,(intro,))
    opBtn = Button(gameDisplay,yellow,"Option",450,450,100,50,None)
    qtBtn = Button(gameDisplay,red,"Quit",725,450,100,50,onC_quit)
    while intro[0]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen(gameDisplay,"Welocme to slither",green,0,-100,"large")
        message_to_screen(gameDisplay,"The objective of the game is to eat red Apples.",
                          black,y_displace = -30)
        message_to_screen(gameDisplay,"The more apple you eat the longer you get.",
                          black,y_displace =10)
        message_to_screen(gameDisplay,"If you run into yourself or edges you die!!.",
                          black,y_displace =50)

        plBut.drawBtn()
        opBtn.drawBtn()
        qtBtn.drawBtn()
        pygame.display.update()
        clock.tick(20)


def gameLoop():

    gameExit = [False]
    orgMode = levelMod(gameDisplay,gameLoop,gameExit)
    while not gameExit[0] :
        orgMode.updateOriginal()
        clock.tick(FPS)
       
    quit()

game_intro()
gameLoop()
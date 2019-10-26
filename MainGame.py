import pygame
import time
import random

from resorces_basic import *
from button import *
from snake import *
from apple import *

pygame.init()

pygame.display.set_icon(appleMain)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('slither')
pygame.display.update()

clock = pygame.time.Clock()

def scoreDisplay(score):
    text = smallFont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text,(0,0))

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

def pause():
    pause = [True,]
    message_to_screen(gameDisplay,"Paused!!",black,0,-50,'large')
    plBtn = Button(gameDisplay,blue,'Resume',183,400,150,50,pause_onClick,[pause],fade=100)
    qtBtn = Button(gameDisplay,red,'Quit',667,400,150,50,onC_quit)
    newBtn = Button(gameDisplay,yellow,'New Game',425,400,150,50,newGame,[gameLoop])
    while pause[0]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                onC_quit()
        
        plBtn.drawBtn()
        qtBtn.drawBtn()
        newBtn.drawBtn()
        pygame.display.update()
        clock.tick(20)

def gameLoop():

    randAppArgs = {'countApple':0,'randAppleX':0,'randAppleY':0}
    randA2Args = {'randAppleX2':0,'randAppleY2':0}
    randAsArgs = {'randAppleXSpecial':0,'randAppleYSpecial':0}

    direction = "Right"
    gameExit = False
    gameOver = False

    randomApple([],randAppArgs)
    
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = MovementSpeed
    lead_y_change = 0

    appleEnable = True
    apple2Enable = False
    appleSpecialEnable = False

    tempCountA2 = 0
    tempCountAS = 0

    last_btn = 0

    # snakeList = []
    # snake_length = 1
 
    
    while not gameExit :
        score = int((snake_length-1))

        
                    

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_LEFT and  lead_x_change == 0:
                    lead_x_change = -MovementSpeed
                    lead_y_change = 0
                    direction = "Left"
                    break
                elif event.key == pygame.K_RIGHT and lead_x_change == 0:
                    lead_x_change = MovementSpeed
                    lead_y_change = 0
                    direction = "Right"
                    break
                elif event.key == pygame.K_UP and lead_y_change == 0:
                    lead_y_change = -MovementSpeed
                    lead_x_change = 0
                    direction = "Up"
                    break
                elif event.key == pygame.K_DOWN and lead_y_change == 0:
                    lead_y_change = MovementSpeed
                    lead_x_change = 0
                    direction = "Down"
                    break
      
        if lead_x >=display_width or lead_y >= display_height or lead_x < 0 or lead_y < 0:
            gameOver = True

        lead_y += lead_y_change
        lead_x += lead_x_change
        
        gameDisplay.fill(white)
        
        gameDisplay.blit(appleMain,(randAppArgs['randAppleX'],randAppArgs['randAppleY']))
        if apple2Enable:
            gameDisplay.blit(apple2,(randA2Args['randAppleX2'],randA2Args['randAppleY2']))
        if appleSpecialEnable:
            gameDisplay.blit(appleSpecial,(randAsArgs['randAppleXSpecial'],randAsArgs['randAppleYSpecial']))
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snake_length:
            del snakeList[0]

        for segment in snakeList[:-1]:
            if segment == snakeHead:
                gameOver = True
        
        snake(gameDisplay,snakeList,imgHead,darkGreen,direction,block_size)
        scoreDisplay(score)
        
        pygame.display.update()
     
        if lead_x == randAppArgs['randAppleX'] and lead_y == randAppArgs['randAppleY']:
            snake_length += 1
            randomApple(snakeList,randAppArgs)
            if randAppArgs['countApple']%5 == 0:
                randomApple2(snakeList,randA2Args)
                apple2Enable = True
            if randAppArgs['countApple']%10 == 0:
                randomAppleSpecial(snakeList,randAsArgs)
                appleSpecialEnable = True
                
        if lead_x == randA2Args['randAppleX2'] and lead_y == randA2Args['randAppleY2'] and apple2Enable:
            snake_length += 2
            tempCountA2 = 0
            apple2Enable = False

        if lead_x == randAsArgs['randAppleXSpecial'] and lead_y == randAsArgs['randAppleYSpecial'] and appleSpecialEnable:
            snake_length += 3
            appleSpecialEnable = False
            tempCountAS = 0

        if apple2Enable:
            if tempCountA2 < 60:
                tempCountA2 += 1
            else:
                apple2Enable = False
                tempCountA2 =0
                
        if appleSpecialEnable:
            if tempCountAS < 30:
                tempCountAS += 1
            else:
                appleSpecialEnable = False
                tempCountAS = 0

        clock.tick(FPS)
    quit()

game_intro()
gameLoop()
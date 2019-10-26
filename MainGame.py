import pygame
import time
import random
from resorces_basic import *
from button import *

pygame.init()

FPS = 10
display_width = 1000
display_height = 600
block_size = 20
MovementSpeed = (block_size)

pygame.display.set_icon(appleMain)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('slither')
pygame.display.update()

direction = "Right"

randAppleX = 0
randAppleY = 0
randAppleX2 = 0
randAppleY2 = 0
randAppleXSpecial = 0
randAppleYSpecial = 0

countApple = 0

clock = pygame.time.Clock()

def newGameStart():
    global countApple
    countApple = 0

def scoreDisplay(score):
    text = smallFont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text,(0,0))

def randomApple(ls):
    global randAppleX,randAppleY,countApple
    countApple += 1
    rAx = 0
    rAy = 0
    rAx = round(random.randrange(0,display_width-block_size,block_size)/block_size)*block_size
    rAy = round(random.randrange(0,display_height-block_size,block_size)/block_size)*block_size
    for snakePart in ls:
        if rAx == snakePart[0] and rAy == snakePart[1]:
            randomApple(ls)
            print(len(ls))
            return
    randAppleX = rAx
    randAppleY = rAy

def randomApple2(ls):
    global randAppleX2,randAppleY2
    rAx = 0
    rAy = 0
    rAx = round(random.randrange(0,display_width-block_size,block_size)/block_size)*block_size
    rAy = round(random.randrange(0,display_height-block_size,block_size)/block_size)*block_size
    for snakePart in ls:
        if rAx == snakePart[0] and rAy == snakePart[1]:
            randomApple2(ls)
            return
    randAppleX2 = rAx
    randAppleY2 = rAy
    
def randomAppleSpecial(ls):
    global randAppleXSpecial,randAppleYSpecial
    rAx = 0
    rAy = 0
    rAx = round(random.randrange(0,display_width-block_size,block_size)/block_size)*block_size
    rAy = round(random.randrange(0,display_height-block_size,block_size)/block_size)*block_size
    for snakePart in ls:
        if rAx == snakePart[0] and rAy == snakePart[1]:
            randomAppleSpecial(ls)
            return
    randAppleXSpecial = rAx
    randAppleYSpecial = rAy

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
        message_to_screen("Welocme to slither",green,0,-100,"large")
        message_to_screen("The objective of the game is to eat red Apples.",
                          black,y_displace = -30)
        message_to_screen("The more apple you eat the longer you get.",
                          black,y_displace =10)
        message_to_screen("If you run into yourself or edges you die!!.",
                          black,y_displace =50)

        plBut.drawBtn()
        opBtn.drawBtn()
        qtBtn.drawBtn()
        pygame.display.update()
        clock.tick(20)

def snake(snakeList,block_size):

    if direction == "Right":
        headImg = pygame.transform.rotate(imgHead,270)
    elif direction == "Down":
        headImg = pygame.transform.rotate(imgHead,180)
    elif direction == "Left":
        headImg = pygame.transform.rotate(imgHead,90)
    elif direction == "Up":
        headImg = imgHead

    gameDisplay.blit(headImg,(snakeList[-1][0],snakeList[-1][1]))
    
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay,darkGreen,[XnY[0],XnY[1],block_size,block_size])


def message_to_screen(msg,color,x_displace=0,y_displace=0,size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width/2)+ x_displace,(display_height/2)+ y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():

    global direction,countApple
    

    direction = "Right"
    gameExit = False
    gameOver = False

    randomApple([])
    
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = MovementSpeed
    lead_y_change = 0

    appleEnable = True
    apple2Enable = False
    appleSpecialEnable = False

    tempCountA2 = 0
    tempCountAS = 0

    tempx = 0
    tempy = 0
    pauPla = 0

    last_btn = 0

    snakeList = []
    snake_length = 1
    #snakeList.append([display_width,display_height-block_size])
    #snakeList.append([display_width,display_height-(2*block_size)])
    newGameBtn = Button(gameDisplay,blue,"New Game",266,330,150,50,newGame_over,[gameLoop,newGameStart],fade = 100)
    quitBtn = Button(gameDisplay,red,"Quit",634,330,150,50,onC_quit)
    while not gameExit :
      #  event = pygame.event.get()
        score = int((snake_length-1))

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over!!!",red,y_displace = -50,size = "medium")
            message_to_screen("Your Score: {}".format(score),blue)
            
            newGameBtn.drawBtn()
            quitBtn.drawBtn()
            pygame.display.update()

            for event in pygame.event.get() :

                if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
                    

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                #gameDisplay.fill(white)
                gameExit = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p and pauPla == 0:
                    tempx = lead_x_change
                    tempy = lead_y_change
                    lead_x_change = 0
                    lead_y_change = 0
                    pauPla = 1
                    break
                elif event.key == pygame.K_p and pauPla == 1:
                    lead_x_change = tempx
                    lead_y_change = tempy
                    pauPla = 0
                    break

                if pauPla == 1:
                    break
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
      
        if pauPla == 1:
            continue

        if lead_x >=display_width or lead_y >= display_height or lead_x < 0 or lead_y < 0:
            gameOver = True

        lead_y += lead_y_change
        lead_x += lead_x_change
        
        gameDisplay.fill(white)
        #pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,block_size,block_size])
        
        gameDisplay.blit(appleMain,(randAppleX,randAppleY))
        if apple2Enable:
            gameDisplay.blit(apple2,(randAppleX2,randAppleY2))
        if appleSpecialEnable:
            gameDisplay.blit(appleSpecial,(randAppleXSpecial,randAppleYSpecial))
        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snake_length:
            del snakeList[0]

        for segment in snakeList[:-1]:
            if segment == snakeHead:
                gameOver = True
        
        snake(snakeList,block_size)
        scoreDisplay(score)
        
        pygame.display.update()
     
        if lead_x == randAppleX and lead_y == randAppleY:
            snake_length += 1
            randomApple(snakeList)
            if countApple%5 == 0:
                randomApple2(snakeList)
                apple2Enable = True
            if countApple%10 == 0:
                randomAppleSpecial(snakeList)
                appleSpecialEnable = True
                
        if lead_x == randAppleX2 and lead_y == randAppleY2 and apple2Enable:
            snake_length += 2
            tempCountA2 = 0
            apple2Enable = False

        if lead_x == randAppleXSpecial and lead_y == randAppleYSpecial and appleSpecialEnable:
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
##        if lead_x > randAppleX and lead_x < randAppleX+block_size or lead_x+block_size > randAppleX and lead_x+block_size < randAppleX+block_size:
##                if lead_y >= randAppleY and lead_y <= randAppleY+block_size or lead_y+block_size >= randAppleY and lead_y+block_size <= randAppleY+block_size:
##                    randAppleX = round(random.randrange(0,display_width-block_size,block_size)/block_size)*block_size
##                    randAppleY = round(random.randrange(0,display_height-block_size,block_size)/block_size)*block_size
##                    snake_length += 2


        clock.tick(FPS)
    quit()

game_intro()
gameLoop()



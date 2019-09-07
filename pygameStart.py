import pygame
import time
import random
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
darkGreen = (0,155,0)
blue = (0,0,255)

FPS = 15
display_width = 800
display_height = 600
block_size = 10

imgHead = pygame.image.load('snakeHead.png')
imgBody = pygame.image.load('snakeBody.png')
imgTail = pygame.image.load('snakeTail.png')

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('slither')
pygame.display.update()

direction = "Right"


#gameDisplay.fill(white)

clock = pygame.time.Clock()

#functions Section
smallFont = pygame.font.SysFont("comicsansms",25)
medFont = pygame.font.SysFont("comicsansms",50)
largeFont = pygame.font.SysFont("comicsansms",80)

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
       # gameDisplay.blit(imgBody,(XnY[0],XnY[1]))
        pygame.draw.rect(gameDisplay,darkGreen,[XnY[0],XnY[1],block_size,block_size])

##    if not len(snakeList) == 1:
##        gameDisplay.blit(imgTail,(snakeList[0][0],snakeList[0][1]))    

def text_objects(msg,color,size):
    if size == "small":
        screen_text = smallFont.render(msg, True, color)
    elif size == "medium":
        screen_text = medFont.render(msg, True, color)
    elif size == "large":
        screen_text = largeFont.render(msg, True, color)
    
    return screen_text, screen_text.get_rect()

def message_to_screen(msg,color,x_displace=0,y_displace=0,size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width/2)+ x_displace,(display_height/2)+ y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():

    global direction
    
    gameExit = False
    gameOver = False

    randAppleX = random.randrange(0,display_width-block_size,block_size)
    randAppleY = random.randrange(0,display_height-block_size,block_size)

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0

    last_btn = 0

    snakeList = []
    snake_length = 1
    #snakeList.append([display_width,display_height-block_size])
    #snakeList.append([display_width,display_height-(2*block_size)])
    
    while not gameExit:
      #  event = pygame.event.get()

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over!!!",red,y_displace = -50,size = "medium")
            message_to_screen("Press N for new game and Q for quit",black,y_displace = 50)
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                    elif event.key == pygame.K_n:
                        gameLoop()
                    
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                #gameDisplay.fill(white)
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and  lead_x_change == 0:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "Left"
                    break
                elif event.key == pygame.K_RIGHT and lead_x_change == 0:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "Right"
                    break
                elif event.key == pygame.K_UP and lead_y_change == 0:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "Up"
                    break
                elif event.key == pygame.K_DOWN and lead_y_change == 0:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "Down"
                    break
      
        '''        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    lead_x_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP:
                    lead_y_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y_change = 0 
        '''
        if lead_x >=display_width or lead_y >= display_height or lead_x < 0 or lead_y < 0:
            gameOver = True

        lead_y += lead_y_change
        lead_x += lead_x_change
        
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,block_size,block_size])

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
        pygame.display.update()
     
        if lead_x == randAppleX and lead_y == randAppleY:
                randAppleX = random.randrange(0,display_width-block_size,block_size)
                randAppleY = random.randrange(0,display_height-block_size,block_size)
                snake_length += 1

        clock.tick(FPS)
    quit()

gameLoop()



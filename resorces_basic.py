import pygame
import time
pygame.init()

smallFont = pygame.font.SysFont("comicsansms",25)
medFont = pygame.font.SysFont("comicsansms",50)
largeFont = pygame.font.SysFont("comicsansms",80)

white = (255,255,255)
black = (0,0,0)
red = (190,0,0)
green = (0,128,0)
yellow = (200,200,0)
l_green = (0,255,0)
darkGreen = (0,155,0)
blue = (0,0,255)

imgHead = pygame.image.load('snakeHead.png')
imgBody = pygame.image.load('snakeBody.png')
imgTail = pygame.image.load('snakeTail.png')
appleMain = pygame.image.load('appleSimple.png')
apple2 = pygame.image.load('apple2.png')
appleSpecial = pygame.image.load('appleultimate.png')

FPS = 10
display_width = 1000
display_height = 600
block_size = 20
MovementSpeed = (block_size)

clock = pygame.time.Clock()

def text_objects(msg,color,size):
    if size == "small":
        screen_text = smallFont.render(msg, True, color)
    elif size == "medium":
        screen_text = medFont.render(msg, True, color)
    elif size == "large":
        screen_text = largeFont.render(msg, True, color)
    
    return screen_text, screen_text.get_rect()

def message_to_screen(gameDisplay,msg,color,x_displace=0,y_displace=0,size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width/2)+ x_displace,(display_height/2)+ y_displace
    gameDisplay.blit(textSurf, textRect)

def lColor(col,change = 50):
    lcol = []
    for i in col:
        tcol = i+change
        if tcol > 255:
            tcol = 255
        lcol.append(tcol)
    return lcol

def onC_quit():
    pygame.quit()
    quit()

def intro_play(intro):
    intro[0] = False

def newGame(gameLoop):
    gameLoop()

def pause_onClick(pause):
    pause[0] = False

def scoreDisplay(gameDisplay,score,color = black):
    text = smallFont.render("Score: "+str(score), True, color)
    gameDisplay.blit(text,(0,0))
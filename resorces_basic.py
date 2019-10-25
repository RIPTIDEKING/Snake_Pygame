import pygame
pygame.init()

smallFont = pygame.font.SysFont("comicsansms",25)
medFont = pygame.font.SysFont("comicsansms",50)
largeFont = pygame.font.SysFont("comicsansms",80)

white = (255,255,255)
black = (0,0,0)
red = (190,0,0)
green = (0,128,0)
l_green = (0,255,0)
darkGreen = (0,155,0)
blue = (0,0,255)

imgHead = pygame.image.load('snakeHead.png')
imgBody = pygame.image.load('snakeBody.png')
imgTail = pygame.image.load('snakeTail.png')
appleMain = pygame.image.load('appleSimple.png')
apple2 = pygame.image.load('apple2.png')
appleSpecial = pygame.image.load('appleultimate.png')

def text_objects(msg,color,size):
    if size == "small":
        screen_text = smallFont.render(msg, True, color)
    elif size == "medium":
        screen_text = medFont.render(msg, True, color)
    elif size == "large":
        screen_text = largeFont.render(msg, True, color)
    
    return screen_text, screen_text.get_rect()

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
import pygame
from button import *

pygame.init()

gameDisplay = pygame.display.set_mode((500,500))
pygame.display.set_caption("buttons")
gameDisplay.fill(white)

def text_objects(msg,color,size):
    if size == "small":
        screen_text = smallFont.render(msg, True, color)
    elif size == "medium":
        screen_text = medFont.render(msg, True, color)
    elif size == "large":
        screen_text = largeFont.render(msg, True, color)

    return screen_text, screen_text.get_rect()

def tt(a,*b,c):
    print(a)
    t(a,*b)
    print(c)
def pri():
    print("hello")

def t(a,b,c,d):
    print(a,b,c,d)


tt(1,2,3,4,c=45)

plyBtn = Button(gameDisplay,blue,'play',100,200,100,50,pri,fade=80)
quiBtn = Button(gameDisplay,red,'Quit',300,200,100,50,pri)
while True:
    #gameDisplay.fill(white)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    plyBtn.drawBtn()
    quiBtn.drawBtn()
    pygame.display.update()
    #pygame.time.Clock().tick(5)

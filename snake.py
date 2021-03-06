from resorces_basic import *

def snake(gameDisplay,snakeList,hImg,snakeColor,direction,block_size):
    
    if direction == "Right":
        hImg = pygame.transform.rotate(hImg,270)
    elif direction == "Down":
        hImg = pygame.transform.rotate(hImg,180)
    elif direction == "Left":
        hImg = pygame.transform.rotate(hImg,90)
    elif direction == "Up":
        hImg = hImg

    
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay,snakeColor,[XnY[0],XnY[1],block_size,block_size])

    gameDisplay.blit(hImg,(snakeList[-1][0],snakeList[-1][1]))
    
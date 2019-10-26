from resorces_basic import *

class orgMod:

    def __init__(self):
        self.snakeList = []
        self.snake_length = 1
        newGameBtn = Button(gameDisplay,blue,"New Game",223,330,150,50,newGame,[gameLoop],fade = 100)
        quitBtn = Button(gameDisplay,red,"Quit",627,330,150,50,onC_quit)

    def updateOriginal(self):
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen(gameDisplay,"Game Over!!!",red,y_displace = -50,size = "medium")
            message_to_screen(gameDisplay,"Your Score: {}".format(score),blue)
            
            newGameBtn.drawBtn()
            quitBtn.drawBtn()
            pygame.display.update()

            for event in pygame.event.get() :

                if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
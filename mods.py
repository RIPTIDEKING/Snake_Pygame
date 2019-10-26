from resorces_basic import *
from button import *
from apple import *
from snake import *

class orgMod:

    def __init__(self,gameDisplay,gameLoop,gameExit):

        self.gameLoop = gameLoop
        self.gameDisplay = gameDisplay
        self.gameExit = gameExit

        self.snakeList = []
        self.snake_length = 1
        self.randAppArgs = {'countApple':0,'randAppleX':0,'randAppleY':0}
        self.randA2Args = {'randAppleX2':0,'randAppleY2':0}
        self.randAsArgs = {'randAppleXSpecial':0,'randAppleYSpecial':0}

        self.direction = "Right"
        self.gameOver = False

        randomApple([],self.randAppArgs)
    
        self.lead_x = display_width/2
        self.lead_y = display_height/2
        self.lead_x_change = MovementSpeed
        self.lead_y_change = 0

        self.appleEnable = True
        self.apple2Enable = False
        self.appleSpecialEnable = False

        self.tempCountA2 = 0
        self.tempCountAS = 0

        self.last_btn = 0


        self.newGameBtn = Button(gameDisplay,blue,"New Game",223,330,150,50,newGame,[gameLoop],fade = 100)
        self.quitBtn = Button(gameDisplay,red,"Quit",627,330,150,50,onC_quit)

    def updateOriginal(self):
        score = int((self.snake_length-1))
        while self.gameOver:
            self.gameDisplay.fill(white)
            message_to_screen(self.gameDisplay,"Game Over!!!",red,y_displace = -50,size = "medium")
            message_to_screen(self.gameDisplay,"Your Score: {}".format(score),blue)
            
            self.newGameBtn.drawBtn()
            self.quitBtn.drawBtn()
            pygame.display.update()

            for event in pygame.event.get() :

                if event.type == pygame.QUIT:
                        self.gameExit = [True]
                        self.gameOver = False

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.gameExit = [True]
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_p:
                    self.pause()
                elif event.key == pygame.K_LEFT and  self.lead_x_change == 0:
                    self.lead_x_change = -MovementSpeed
                    self.lead_y_change = 0
                    self.direction = "Left"
                    break
                elif event.key == pygame.K_RIGHT and self.lead_x_change == 0:
                    self.lead_x_change = MovementSpeed
                    self.lead_y_change = 0
                    self.direction = "Right"
                    break
                elif event.key == pygame.K_UP and self.lead_y_change == 0:
                    self.lead_y_change = -MovementSpeed
                    self.lead_x_change = 0
                    self.direction = "Up"
                    break
                elif event.key == pygame.K_DOWN and self.lead_y_change == 0:
                    self.lead_y_change = MovementSpeed
                    self.lead_x_change = 0
                    self.direction = "Down"
                    break
        if self.lead_x >= display_width or self.lead_y >= display_height or self.lead_x < 0 or self.lead_y < 0:
            self.gameOver = [True]

        self.lead_y += self.lead_y_change
        self.lead_x += self.lead_x_change
    
        self.gameDisplay.fill(white)
    
        self.gameDisplay.blit(appleMain,(self.randAppArgs['randAppleX'],self.randAppArgs['randAppleY']))
        if self.apple2Enable:
            self.gameDisplay.blit(apple2,(self.randA2Args['randAppleX2'],self.randA2Args['randAppleY2']))
        if self.appleSpecialEnable:
            self.gameDisplay.blit(appleSpecial,(self.randAsArgs['randAppleXSpecial'],self.randAsArgs['randAppleYSpecial']))
    
        snakeHead = []
        snakeHead.append(self.lead_x)
        snakeHead.append(self.lead_y)
        self.snakeList.append(snakeHead)

        if len(self.snakeList) > self.snake_length:
            del self.snakeList[0]

        for segment in self.snakeList[:-1]:
            if segment == snakeHead:
                self.gameOver = True
    
        snake(self.gameDisplay,self.snakeList,imgHead,darkGreen,self.direction,block_size)
        scoreDisplay(self.gameDisplay,score)
    
        pygame.display.update()
    
        if self.lead_x == self.randAppArgs['randAppleX'] and self.lead_y == self.randAppArgs['randAppleY']:
            self.snake_length += 1
            randomApple(self.snakeList,self.randAppArgs)
            if self.randAppArgs['countApple']%5 == 0:
                randomApple2(self.snakeList,self.randA2Args)
                self.apple2Enable = True
            if self.randAppArgs['countApple']%10 == 0:
                randomAppleSpecial(self.snakeList,self.randAsArgs)
                self.appleSpecialEnable = True
            
        if self.lead_x == self.randA2Args['randAppleX2'] and self.lead_y == self.randA2Args['randAppleY2'] and self.apple2Enable:
            self.snake_length += 2
            self.tempCountA2 = 0
            self.apple2Enable = False

        if self.lead_x == self.randAsArgs['randAppleXSpecial'] and self.lead_y == self.randAsArgs['randAppleYSpecial'] and self.appleSpecialEnable:
            self.snake_length += 3
            self.appleSpecialEnable = False
            self.tempCountAS = 0

        if self.apple2Enable:
            if self.tempCountA2 < 60:
                self.tempCountA2 += 1
            else:
                self.apple2Enable = False
                self.tempCountA2 =0
            
        if self.appleSpecialEnable:
            if self.tempCountAS < 30:
                self.tempCountAS += 1
            else:
                self.appleSpecialEnable = False
                self.tempCountAS = 0

    def pause(self):
        pause = [True,]
        message_to_screen(self.gameDisplay,"Paused!!",black,0,-50,'large')
        plBtn = Button(self.gameDisplay,blue,'Resume',183,400,150,50,pause_onClick,[pause],fade=100)
        qtBtn = Button(self.gameDisplay,red,'Quit',667,400,150,50,onC_quit)
        newBtn = Button(self.gameDisplay,yellow,'New Game',425,400,150,50,newGame,[self.gameLoop])
        while pause[0]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    onC_quit()

            plBtn.drawBtn()
            qtBtn.drawBtn()
            newBtn.drawBtn()
            pygame.display.update()
            clock.tick(20)

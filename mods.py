from resorces_basic import *
from button import *
from apple import *
from snake import *

class orgMod:

    def __init__(self,gameDisplay,gameLoop,gameExit):

        self.gameLoop = gameLoop
        self.gameDisplay = gameDisplay
        self.gameExit = gameExit

        #pygame.draw.rect(gameDisplay,red,[0,0,20,20])
        self.gameStart = True
        self.snakeList = []
        self.snake_length = 1
        self.randAppArgs = {'countApple':0,'randAppleX':0,'randAppleY':0}
        self.randA2Args = {'randAppleX2':0,'randAppleY2':0}
        self.randAsArgs = {'randAppleXSpecial':0,'randAppleYSpecial':0}

        self.direction = "Right"
        self.gameOver = False

        self.randomAppleStart()
    
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
        self.score = 0

        self.newGameBtn = Button(gameDisplay,blue,"New Game",223,330,150,50,newGame,[gameLoop],fade = 100)
        self.quitBtn = Button(gameDisplay,red,"Quit",627,330,150,50,onC_quit)

    def randomAppleStart(self):
        randomApple([],self.randAppArgs)

    def updateOriginal(self):
        
        if self.gameStart:
            self.gameInit()
        
        if self.leveLogic():
            return

        self.score = int((self.snake_length-1))
        
        self.orgGameOver()

        self.controls()
        
        self.lead_y += self.lead_y_change
        self.lead_x += self.lead_x_change
        
        if self.boundaryCondition():
            return

        self.gameDisplay.fill(white)
        pygame.draw.rect(self.gameDisplay,l_yellow,[0,0,1000,40])
        scoreDisplay(self.gameDisplay,self.score)
        self.drawLevel()

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
        
        pygame.display.update()
    
        if self.lead_x == self.randAppArgs['randAppleX'] and self.lead_y == self.randAppArgs['randAppleY']:
            self.snake_length += 100
            self.newAppleLogic()
            
        if self.lead_x == self.randA2Args['randAppleX2'] and self.lead_y == self.randA2Args['randAppleY2'] and self.apple2Enable:
            self.snake_length += 2
            self.tempCountA2 = 0
            self.apple2Enable = False

        if self.lead_x == self.randAsArgs['randAppleXSpecial'] and self.lead_y == self.randAsArgs['randAppleYSpecial'] and self.appleSpecialEnable:
            self.snake_length += 5
            self.appleSpecialEnable = False
            self.tempCountAS = 0

        if self.apple2Enable:
            if self.tempCountA2 < 70:
                self.tempCountA2 += 1
            else:
                self.apple2Enable = False
                self.tempCountA2 =0
            
        if self.appleSpecialEnable:
            if self.tempCountAS < 40:
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

    def boundaryCondition(self):
        if self.lead_x >= display_width or self.lead_y >= display_height or self.lead_x < 0 or self.lead_y < 0:
            self.gameOver = [True]
            return True
        return False

    def orgGameOver(self):
        while self.gameOver:
            self.gameDisplay.fill(white)
            message_to_screen(self.gameDisplay,"Game Over!!!",red,y_displace = -50,size = "medium")
            message_to_screen(self.gameDisplay,"Your Score: {}".format(self.score),blue)
            
            self.newGameBtn.drawBtn()
            self.quitBtn.drawBtn()
            pygame.display.update()

            for event in pygame.event.get() :

                if event.type == pygame.QUIT:
                        self.gameExit[0] = True
                        self.gameOver = False

    def controls(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.gameExit[0] = True
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
    
    def newAppleLogic(self):
        randomApple(self.snakeList,self.randAppArgs)
        if self.randAppArgs['countApple']%5 == 0:
            randomApple2(self.snakeList,self.randA2Args)
            self.apple2Enable = True
        if self.randAppArgs['countApple']%10 == 0:
            randomAppleSpecial(self.snakeList,self.randAsArgs)
            self.appleSpecialEnable = True
    
    def drawLevel(self):
        pass
    
    def leveLogic(self):
        pass

    def gameInit(self):
        self.gameStart = False

class orgModS(orgMod):

    def boundaryCondition(self):
        if self.lead_x >=  display_width:
            self.lead_x = 0
        elif self.lead_y >= display_height:
            self.lead_y = 40
        elif self.lead_x < 0:
            self.lead_x = display_width-20
        elif self.lead_y < 40:
            self.lead_y = display_height-20
        return False

class levelMod(orgModS):

    def __init__(self,gameDisplay,gameLoop,gameExit):
        self.level = 1
        # self.gameLoop = gameLoop
        # self.gameExit = gameExit
        self.rectInfo = [
            [],
            [[0,40,480,20],[520,40,480,20],[0,60,20,220],[0,320,20,280],[980,60,20,220],[980,320,20,280],[20,580,460,20],[520,580,460,20]],        
            [[0,40,1000,20],[0,60,20,540],[980,60,20,540],[20,580,960,20]],
            [[0,40,480,20],[520,40,480,20],[0,60,20,240],[0,340,20,260],[980,60,20,240],[980,340,20,260],[20,580,460,20],[520,580,460,20],[160,200,320,20],[160,220,20,80],[160,340,20,100],[180,420,300,20],[840,220,20,80],[520,200,340,20],[840,340,20,80],[520,420,340,20]]
        ]
        super().__init__(gameDisplay,gameLoop,gameExit)

    
    def randomAppleStart(self):
        randomApple([],self.randAppArgs,self.rectInfo[(self.level-1)%4])

    def drawLevel(self):
        message_to_screen(self.gameDisplay,"target: {}".format(self.level*50),black,y_displace=-285)
        for recNo in self.rectInfo[(self.level-1)%4]:
            pygame.draw.rect(self.gameDisplay,grey,recNo)
        
    def newAppleLogic(self):
        randomApple(self.snakeList,self.randAppArgs,self.rectInfo[(self.level-1)%4])
        if self.randAppArgs['countApple']%5 == 0:
            randomApple2(self.snakeList,self.randA2Args,self.rectInfo[(self.level-1)%4])
            self.apple2Enable = True
        if self.randAppArgs['countApple']%10 == 0:
            randomAppleSpecial(self.snakeList,self.randAsArgs,self.rectInfo[(self.level-1)%4])
            self.appleSpecialEnable = True

    def boundaryCondition(self):
        super().boundaryCondition()
        if checkBigRect(self.rectInfo[(self.level-1)%4],self.lead_x,self.lead_y):
            self.gameOver = [True]
            return True
        return False
    
    def levelInfo(self):
        self.gameDisplay.fill(white)
        ydisplace = -250
        xdisplace = 50
        textSize = 'medium'
        if self.level == 1:
            message_to_screen(self.gameDisplay,"Welcome to Level mode!!",blue,y_displace=-150,size="large")
            message_to_screen(self.gameDisplay,"You have to chase the target",black,y_displace=-50,size="medium")
            message_to_screen(self.gameDisplay,"to move to next level.",black,y_displace=-5,size="medium")
            ydisplace = 0
            textSize = 'small'

        message_to_screen(self.gameDisplay,"target:",black,-35-xdisplace,50+ydisplace,textSize)
        message_to_screen(self.gameDisplay,"{}".format(self.level*50),green,35+xdisplace,50+ydisplace,textSize)
        message_to_screen(self.gameDisplay,"level:",black,-30-xdisplace,90+ydisplace-(ydisplace*0.2),textSize)
        message_to_screen(self.gameDisplay,"{}".format(self.level),green,30+xdisplace,90+ydisplace-(ydisplace*0.2),textSize)

    def stsGm(self):
        self.gameStart = False
    
    def leveLogic(self):
        if self.score >= (self.level*50):
            super().__init__(self.gameDisplay,self.gameLoop,self.gameExit)
            self.level += 1
            self.gameStart = True
            return True
        else:
            return False

    def gameInit(self):
        if self.level == 1:
            self.levelInfo()
            plBtnSt = Button(self.gameDisplay,green,"Play",450,500,100,50,self.stsGm)

            while self.gameStart:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                        
                plBtnSt.drawBtn()
                pygame.display.update()
                clock.tick(20)
        else:
            for  i in range(3,0,-1):
                self.levelInfo()        
                message_to_screen(self.gameDisplay,str(i),red,y_displace=160,size='large')
                pygame.display.update()
                clock.tick(1)
                
            self.gameStart = False

        
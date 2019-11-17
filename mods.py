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
        self.randAppArgsE = {'randAppleXE':0,'randAppleYE':0}

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
        self.appleEEnable = False

        self.tempCountA2 = 0
        self.tempCountAS = 0

        self.last_btn = 0
        self.score = 0

        self.newGameBtn = Button(gameDisplay,blue,"New Game",223,330,150,50,newGame,[gameLoop],fade = 100)
        self.quitBtn = Button(gameDisplay,red,"Quit",627,330,150,50,onC_quit)

        self.cheatKey = True
        
        self.ls = [[0,40,1000,20],[0,60,20,540],[980,60,20,540],[20,580,960,20]]

        self.eEval = True
        self.foundE = False

    def randomAppleStart(self):
        randomApple([],self.randAppArgs)

    def updateOriginal(self):
        
        if self.gameStart:
            self.gameInit()
        
        if self.leveLogic():
            return

        self.score = int((self.snake_length-1))
        
        self.orgGameOver(self.score)

        self.controls()
        
        self.lead_y += self.lead_y_change
        self.lead_x += self.lead_x_change
        
        if self.boundaryCondition():
            return

        self.gameDisplay.fill(white)
        pygame.draw.rect(self.gameDisplay,l_yellow,[0,0,1000,40])
        scoreDisplay(self.gameDisplay,self.score)
        if self.foundE:
            self.easterEgg()
        self.drawLevel()

        if self.appleEEnable:
            self.gameDisplay.blit(appleEaster,(self.randAppArgsE['randAppleXE'],self.randAppArgsE['randAppleYE']))
        else:
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

        if self.lead_x == self.randAppArgsE['randAppleXE'] and self.lead_y == self.randAppArgsE['randAppleYE']:
            self.snake_length += 100
            self.eEval = False
            self.appleEEnable = False
            self.foundE = True
            self.newAppleLogic()
    
        if self.lead_x == self.randAppArgs['randAppleX'] and self.lead_y == self.randAppArgs['randAppleY']:
            self.snake_length += 1
            self.newAppleLogic()
            
        if self.lead_x == self.randA2Args['randAppleX2'] and self.lead_y == self.randA2Args['randAppleY2'] and self.apple2Enable:
            self.snake_length += 2
            self.tempCountA2 = 0
            self.apple2Enable = False
            if self.randAppArgs['countApple'] == 10 and self.eEval:
                if self.appleSpecialEnable:
                    self.eEval = False
            else:    
                self.eEval = False
            print(self.eEval,self.randAppArgs['countApple'])

        if self.lead_x == self.randAsArgs['randAppleXSpecial'] and self.lead_y == self.randAsArgs['randAppleYSpecial'] and self.appleSpecialEnable:
            self.snake_length += 5
            self.appleSpecialEnable = False
            self.tempCountAS = 0
            if self.randAppArgs['countApple'] == 10 and self.eEval:
                pass
            else:
                self.eEval = False
            print(self.eEval,self.randAppArgs['countApple'])

        if self.apple2Enable:
            if self.tempCountA2 < 70:
                if self.randAppArgs['countApple']==10 and self.eEval:
                    pass
                else:
                    self.tempCountA2 += 1
            else:
                self.apple2Enable = False
                self.tempCountA2 =0
            
        if self.appleSpecialEnable:
            if self.tempCountAS < 40:
                if self.randAppArgs['countApple']==10 and self.eEval:
                    pass
                else:    
                    self.tempCountAS += 1
            else:
                self.appleSpecialEnable = False
                self.tempCountAS = 0

    def pause(self):
        pause = [True,]
        message_to_screen(self.gameDisplay,"Paused!!",black,0,-50,'large')
        plBtn = Button(self.gameDisplay,blue,'Resume',183,400,150,50,pause_onClick,[pause],fade=100)
        qtBtn = Button(self.gameDisplay,red,'Quit',667,400,150,50,onC_quit)
        newBtn = Button(self.gameDisplay,yellow,'Menu',425,400,150,50,newGame,[self.gameLoop])
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
        if checkBigRect(self.ls,self.lead_x,self.lead_y):
            self.gameOver = [True]
            return True
        return False

    def highScore(self,hscore,mode = 0):
        print(mode)
        f = open("HighScore.txt","r")
        ls = []
        for i in f:
            ls.append(i)
        f.close()
        # print(ls)
        if int(ls[mode]) < hscore:
            ls[mode] = str(hscore)+'\n'
            w = open("HighScore.txt","w")
            for i in ls:
                w.write(i)
            w.close()
        rhs = int(ls[mode])
        return rhs

    def orgGameOver(self,fscore,mode=0):
        flag = True
        rhs = 0
        while self.gameOver:
            if flag:
                hs = self.highScore(fscore,mode)
                flag = False
                self.gameDisplay.fill(white)
                message_to_screen(self.gameDisplay,"Game Over!!!",red,y_displace = -100,size = "medium")
                message_to_screen(self.gameDisplay,"Your Final Score: {}".format(fscore),blue,y_displace=-50)
                message_to_screen(self.gameDisplay,"High Score: {} ".format(hs),blue)

            self.newGameBtn.drawBtn()
            
            self.quitBtn.drawBtn()
            pygame.display.update()

            for event in pygame.event.get() :

                if event.type == pygame.QUIT:
                        self.gameExit[0] = True
                        self.gameOver = [False]

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
                elif event.key == pygame.K_a and self.cheatKey:
                    self.snake_length += 50
                    self.cheatKey = False
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.cheatKey = True

    def newAppleLogic(self):
        if self.randAppArgs['countApple'] == 11 and self.eEval:
            if self.appleSpecialEnable or self.apple2Enable:
                self.eEval = False 
            else:
                randomAppleE(self.snakeList,self.randAppArgsE)
                self.appleEEnable = True
        else:
            randomApple(self.snakeList,self.randAppArgs)
        if (self.randAppArgs['countApple'])%5 == 0:
            randomApple2(self.snakeList,self.randA2Args)
            self.apple2Enable = True
        if (self.randAppArgs['countApple'])%10 == 0:
            randomAppleSpecial(self.snakeList,self.randAsArgs)
            self.appleSpecialEnable = True
    
    def drawLevel(self):
        for recNo in self.ls:
            pygame.draw.rect(self.gameDisplay,grey,recNo)
    
    def leveLogic(self):
        pass

    def gameInit(self):
        self.gameStart = False

    def easterEgg(self):
        #print("Here")
        message_to_screen(self.gameDisplay,"Created By: Ayush Agarwal",green,y_displace=-280,size="small")

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
    
    def drawLevel(self):
        pass

    def orgGameOver(self, fscore, mode=1):
        return super().orgGameOver(fscore, mode)


class levelMod(orgModS):

    def __init__(self,gameDisplay,gameLoop,gameExit):
        self.level = 1
        self.scores = []
        self.tscore = 0
        self.mode = 2
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
        message_to_screen(self.gameDisplay,"total Score: {}".format(self.tscore+self.score),black,y_displace=-285,x_displace=380)
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
            ts = self.score
            tss = self.scores
            super().__init__(self.gameDisplay,self.gameLoop,self.gameExit)
            self.level += 1
            self.gameStart = True
            self.scores.append(ts)
            self.tscore = lsAdd(tss)
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

    def orgGameOver(self, fscore,mode = 2):
        return super().orgGameOver(self.tscore+fscore,mode)
    

class multiPlayer(orgModS):
    def __init__(self ,gameDisplay,gameLoop,gameExit):
        super().__init__(gameDisplay,gameLoop,gameExit)

        self.snakeList1 = []
        self.snake_length1 = 1
        self.direction1 = "Down"
        self.direction  = "Down"

        self.lead_x = (display_width/2)+(block_size*5)
        self.lead_y = display_height/2
        self.lead_x1 = (display_width/2)-(block_size*5)
        self.lead_y1 = display_height/2

        self.lead_x_change = 0
        self.lead_y_change = MovementSpeed
        self.lead_x_change1 = 0
        self.lead_y_change1 = MovementSpeed

        self.winnerInfo = []

        self.newGameBtn = Button(gameDisplay,blue,"New Game",223,380,150,50,newGame,[gameLoop],fade = 100)
        self.quitBtn = Button(gameDisplay,red,"Quit",627,380,150,50,onC_quit)


    def updateOriginal(self):
        
        if self.gameStart:
            self.gameInit()
        
        if self.leveLogic():
            return

        self.score = int((self.snake_length-1))
        self.score1 = int((self.snake_length1-1))

        self.orgGameOver(self.winnerInfo)

        self.controls()
        
        self.lead_y += self.lead_y_change
        self.lead_x += self.lead_x_change
        self.lead_x1 += self.lead_x_change1
        self.lead_y1 += self.lead_y_change1
        
        if self.boundaryCondition():
            return

        self.gameDisplay.fill(white)
        pygame.draw.rect(self.gameDisplay,l_yellow,[0,0,1000,40])
        scoreDisplay(self.gameDisplay,self.score,lbl="Score Player 1: ")
        self.drawLevel(self.score1)

        self.gameDisplay.blit(appleMain,(self.randAppArgs['randAppleX'],self.randAppArgs['randAppleY']))
        if self.apple2Enable:
            self.gameDisplay.blit(apple2,(self.randA2Args['randAppleX2'],self.randA2Args['randAppleY2']))
        if self.appleSpecialEnable:
            self.gameDisplay.blit(appleSpecial,(self.randAsArgs['randAppleXSpecial'],self.randAsArgs['randAppleYSpecial']))
    
        snakeHead = []
        snakeHead.append(self.lead_x)
        snakeHead.append(self.lead_y)
        self.snakeList.append(snakeHead)

        snakeHead1 = []
        snakeHead1.append(self.lead_x1)
        snakeHead1.append(self.lead_y1)
        self.snakeList1.append(snakeHead1)

        if len(self.snakeList) > self.snake_length:
            del self.snakeList[0]

        if len(self.snakeList1) > self.snake_length1:
            del self.snakeList1[0]

        if snakeHead == snakeHead1:
            self.gameOver = True
            if self.snake_length > self.snake_length1:
                self.winnerInfo.clear()
                self.winnerInfo.append(self.score)
                self.winnerInfo.append(self.score1)
                self.winnerInfo.append(1)
            elif self.snake_length < self.snake_length1:
                self.winnerInfo.clear()
                self.winnerInfo.append(self.score)
                self.winnerInfo.append(self.score1)
                self.winnerInfo.append(2)
            else:
                self.winnerInfo.clear()
                self.winnerInfo.append(self.score)
                self.winnerInfo.append(self.score1)
                self.winnerInfo.append(0)

        for segment in self.snakeList[:-1]:
            if segment == snakeHead1:
                self.gameOver = True
                self.winnerInfo.clear()
                self.winnerInfo.append(self.score)
                self.winnerInfo.append(self.score1)
                self.winnerInfo.append(1)
        
        for segment in self.snakeList1[:-1]:
            if segment == snakeHead:
                self.gameOver = True
                self.winnerInfo.clear()
                self.winnerInfo.append(self.score)
                self.winnerInfo.append(self.score1)
                self.winnerInfo.append(2)
    
        snake(self.gameDisplay,self.snakeList,imgHead,darkGreen,self.direction,block_size)
        snake(self.gameDisplay,self.snakeList1,imgHead1,blue,self.direction1,block_size)

        pygame.display.update()
    
        if self.lead_x == self.randAppArgs['randAppleX'] and self.lead_y == self.randAppArgs['randAppleY']:
            self.snake_length += 1
            self.newAppleLogic()
            
        if self.lead_x == self.randA2Args['randAppleX2'] and self.lead_y == self.randA2Args['randAppleY2'] and self.apple2Enable:
            self.snake_length += 2
            self.tempCountA2 = 0
            self.apple2Enable = False

        if self.lead_x == self.randAsArgs['randAppleXSpecial'] and self.lead_y == self.randAsArgs['randAppleYSpecial'] and self.appleSpecialEnable:
            self.snake_length += 5
            self.appleSpecialEnable = False
            self.tempCountAS = 0

        if self.lead_x1 == self.randAppArgs['randAppleX'] and self.lead_y1 == self.randAppArgs['randAppleY']:
            self.snake_length1 += 1
            self.newAppleLogic()
            
        if self.lead_x1 == self.randA2Args['randAppleX2'] and self.lead_y1 == self.randA2Args['randAppleY2'] and self.apple2Enable:
            self.snake_length1 += 2
            self.tempCountA2 = 0
            self.apple2Enable = False

        if self.lead_x1 == self.randAsArgs['randAppleXSpecial'] and self.lead_y1 == self.randAsArgs['randAppleYSpecial'] and self.appleSpecialEnable:
            self.snake_length1 += 5
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
                
                elif event.key == pygame.K_RIGHT and self.lead_x_change == 0:
                    self.lead_x_change = MovementSpeed
                    self.lead_y_change = 0
                    self.direction = "Right"
                
                elif event.key == pygame.K_UP and self.lead_y_change == 0:
                    self.lead_y_change = -MovementSpeed
                    self.lead_x_change = 0
                    self.direction = "Up"

                elif event.key == pygame.K_DOWN and self.lead_y_change == 0:
                    self.lead_y_change = MovementSpeed
                    self.lead_x_change = 0
                    self.direction = "Down"
                
                elif event.key == pygame.K_c and self.cheatKey:
                    self.snake_length += 50
                    self.cheatKey = False
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    self.cheatKey = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and self.lead_x_change1 == 0:
                    self.lead_x_change1 = -MovementSpeed
                    self.lead_y_change1 = 0
                    self.direction1 = "Left"
                    break
                elif event.key == pygame.K_d and self.lead_x_change1 == 0:
                    self.lead_x_change1 = MovementSpeed
                    self.lead_y_change1 = 0
                    self.direction1 = "Right"
                    break
                elif event.key == pygame.K_w and self.lead_y_change1 == 0:
                    self.lead_y_change1 = -MovementSpeed
                    self.lead_x_change1 = 0
                    self.direction1 = "Up"
                    break
                elif event.key == pygame.K_s and self.lead_y_change1 == 0:
                    self.lead_y_change1 = MovementSpeed
                    self.lead_x_change1 = 0
                    self.direction1 = "Down"
                    break
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_v:
                    self.snake_length += 50  

    def boundaryCondition(self):
        a =  super().boundaryCondition()

        if self.lead_x1 >=  display_width:
            self.lead_x1 = 0
        elif self.lead_y1 >= display_height:
            self.lead_y1 = 40
        elif self.lead_x1 < 0:
            self.lead_x1 = display_width-20
        elif self.lead_y1 < 40:
            self.lead_y1 = display_height-20
        
        return a
    
    def drawLevel(self,score1):
        message_to_screen(self.gameDisplay,"Score Player 2: {}".format(score1),black,y_displace=-285)

    def orgGameOver(self,winInfo):
        while self.gameOver:
            self.gameDisplay.fill(white)
            if winInfo[2] == 0:
                message_to_screen(self.gameDisplay,"Match Tied!!!",red,y_displace=-50,size="medium")
            else:
                message_to_screen(self.gameDisplay,"Player {} Wins!!!".format(winInfo[2]),green,y_displace = -50,size = "medium")
            message_to_screen(self.gameDisplay,"Player 1 Score: {}".format(winInfo[0]),blue,y_displace=10)
            message_to_screen(self.gameDisplay,"Player 2 Score: {}".format(winInfo[1]),blue,y_displace=50)
            
            self.newGameBtn.drawBtn()
            self.quitBtn.drawBtn()
            pygame.display.update()

            for event in pygame.event.get() :

                if event.type == pygame.QUIT:
                        self.gameExit[0] = True
                        self.gameOver = [False]


        
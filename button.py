from resorces_basic import *

class Button:


    def __init__(self,gDisplay,color,msg,buttonX,buttonY,buttonWidth,buttonHeigth,onClicked,args=[],size="small",textColor = black,fade = 50):

        self.gameDisplay = gDisplay
        self.color = color
        self.text = msg
        self.xPos = buttonX
        self.yPos = buttonY
        self.width = buttonWidth
        self.heigth = buttonHeigth
        self.textSize = size
        self.textColor = textColor
        self.hoverColor = lColor(self.color,fade)
        self.click = onClicked
        self.oneClick = True
        self.checkClick = False
        self.args = args

    def drawBtn(self):
        mousePt = pygame.mouse.get_pos()
        mouseClicked = pygame.mouse.get_pressed()
        if self.xPos+self.width > mousePt[0] > self.xPos and self.yPos+self.heigth > mousePt[1] > self.yPos:
            pygame.draw.rect(self.gameDisplay,self.hoverColor,(self.xPos,self.yPos,self.width,self.heigth))
            if mouseClicked[0] == 1 and self.oneClick:
                self.oneClick = False
                self.checkClick = True
            elif mouseClicked[0] == 0 and self.checkClick:
                self.oneClick = True
                self.checkClick = False
                self.onClick()
                
        else:
            pygame.draw.rect(self.gameDisplay,self.color,(self.xPos,self.yPos,self.width,self.heigth))
            self.checkClick = False
            self.oneClick = True

        textSurf,textRect = text_objects(self.text,black,self.textSize)
        textRect.center = (self.xPos+(self.width//2),self.yPos+(self.heigth//2))
        self.gameDisplay.blit(textSurf,textRect)

    def onClick(self):
        if self.args == []:
            self.click()
        else:
            self.click(*self.args)
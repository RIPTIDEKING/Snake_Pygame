from mods import *

class menus:
    def __init__(self,gameDisplay,gameExit,intro):
        self.gameDisplay = gameDisplay
        self.gameExit = gameExit
        self.intro = intro

        self.buttons = {"selectMode":None}
        self.pages = {"modes":None}

    def modeSelectOnClick(self,num):
        while not self.gameExit[0]:
            self.pages['modes'][num].updateOriginal()
            clock.tick(FPS)
    
    def selectModeInit(self,gameLoop):
        ls = []
        for i in range(4):
            print(-150+(60*i))
            ls.append(Button(self.gameDisplay,green,"Play",600,130+(60*i),100,50,self.modeSelectOnClick,[i]))
        ls.append(Button(self.gameDisplay,blue,"< back",450,400,100,50,self.intro,fade=100))
        self.buttons['selectMode'] = ls
        ls = []
        ls.append(orgModS(self.gameDisplay,gameLoop,self.gameExit))
        ls.append(orgMod(self.gameDisplay,gameLoop,self.gameExit))
        ls.append(levelMod(self.gameDisplay,gameLoop,self.gameExit))
        ls.append(multiPlayer(self.gameDisplay,gameLoop,self.gameExit))
        self.pages['modes'] = ls

    def modeSelectMenu(self):
        self.gameDisplay.fill(white)
        message_to_screen(self.gameDisplay,"Select Mode:",blue,y_displace=-240,size="large")
        message_to_screen(self.gameDisplay,"Infinite Mode 1 ",black,-280,-150,'medium')
        message_to_screen(self.gameDisplay,"Infinite Mode 2",black,-285,-90,'medium')
        message_to_screen(self.gameDisplay,"Level Mode",black,-345,-30,'medium')
        message_to_screen(self.gameDisplay,"Multiplayer Mode",black,-280,30,'medium')

        
        while not self.gameExit[0]:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()        
        

            for db in self.buttons['selectMode']:
                db.drawBtn()
            clock.tick(30)
            pygame.display.update()
            
    
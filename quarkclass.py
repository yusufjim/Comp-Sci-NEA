##################CLASS FOR QUARKS##################################
import pygame, sys

class Quark(object):
    SIZE = 20
    X = 100
    Y = 100
    def __init__(self,name,charge,spin,colour):
        self.name = name
        self.charge = charge
        self.spin = spin
        self.colour = colour
        self.size = Quark.SIZE
        self.thickness = Quark.SIZE
        self.x = Quark.X
        self.y = Quark.Y


    def getName(self):
        #"variablename".getName()
        return self.name

    def getCharge(self):
        #"variablename".getCharge()
        return self.charge

    def getSpin(self):
        #"variablename".getSpin()
        return self.spin
    
    def getColour(self):
        #"variablename".getColour()
        return self.colour

    def getSize(self):
        #"variablename".getSize()
        return self.size
    
    def getThickness(self):
        #"variablename".getThickness()
        return self.thickness

    def getX(self):
        #"variablename".getX()
        return self.x

    def getY(self):
        #"variablename".getY()
        return self.y
        
    def drawCircle(self,screen):
        pygame.draw.circle(screen,self.colour,(self.x, self.y),self.thickness,self.size)

class Up(Quark):
    def __init__(self):
        Quark.__init__(self,"Up","2/3","1/2",(0,0,102))

        '''
        self.name = "Up"
        self.charge = +2/3 #e
        self.spin = 1/2
        self.colour = (0, 0, 102) #Dark Blue
        '''

class ANTIUp(Quark):
    def __init__(self):
        Quark.__init__(self,"Anti-Up","-2/3","1/2",(51, 204, 255))

        '''        
        self.name = "Anti-Up"
        self.charge = -2/3 
        self.spin = 1/2
        self.colour = (51, 204, 255) #Light Blue
        '''

class Down(Quark):
    def __init__(self):
        Quark.__init__(self,"Down","-1/3","1/2",(0, 102, 0))

        '''
        self.name = "Down"
        self.charge = -1/3 #e
        self.spin = 1/2
        self.colour = (0, 102, 0) #Dark Green
        '''

class ANTIDown(Quark):
    def __init__(self):
        Quark.__init__(self,"Anti-Down","1/3","1/2",(153, 255, 51))

        '''
        self.name = "Anti-Down"
        self.charge = +1/3 #e
        self.spin = 1/2
        self.colour =(153, 255, 51) #Light Green
        '''

class Charm(Quark):
    def __init__(self):
        Quark.__init__(self,"Charm","2/3","1/2",(255,0,0))

        '''
        self.name = "Charm"
        self.charge = +2/3 #e
        self.spin = 1/2
        self.colour = (255,0,0) #Red
        '''
        
class ANTICharm(Quark):
    def __init__(self):
        Quark.__init__(self,"Anti-Charm","-2/3","1/2",(255,165,0))

        '''
        self.name = "Anti-Charm"
        self.charge = -2/3 #e
        self.spin = 1/2
        self.colour = (255,165,0) #Orange
        '''
        
class Top(Quark):
    def __init__(self):
        Quark.__init__(self,"Top","2/3","1/2",(102, 51, 0))

        '''
        self.name = "Top"
        self.charge = +2/3 #e
        self.spin = 1/2
        self.colour = (102, 51, 0) #Brown
        '''
        
class ANTITop(Quark):
    def __init__(self):
        Quark.__init__(self,"Anti-Top","-2/3","1/2",(255,255,0))

        '''
        self.name = "Anti-Top"
        self.charge = -2/3 #e
        self.spin = 1/2
        self.colour = (255,255,0) #Yellow
        '''
        
class Strange(Quark):
    def __init__(self):
        Quark.__init__(self,"Strange","-1/3","1/2",(170,170,170))

        '''
        self.name = "Strange"
        self.charge = -1/3 #e
        self.spin = 1/2
        self.colour = (170,170,170) #Grey
        '''

class ANTIStrange(Quark):
    def __init__(self):
        Quark.__init__(self,"Anti-Strange","1/3","1/2",(0,0,0))

        '''
        self.name = "Anti-Strange"
        self.charge = +1/3 #e
        self.spin = 1/2
        self.colour = (0,0,0) #Black
        '''

class Bottom(Quark):
    def __init__(self):
        Quark.__init__(self,"Bottom","-1/3","1/2",(77, 0, 153))

        '''
        self.name = "Bottom"
        self.charge = -1/3 #e
        self.spin = 1/2
        self.colour = (77, 0, 153) #Dark Purple
        '''

class ANTIBottom(Quark):
    def __init__(self):
        Quark.__init__(self,"Anti-Bottom","1/3","1/2",(191, 128, 255))

        '''
        self.name = "Anti-Bottom"
        self.charge = +1/3 #e
        self.spin = 1/2
        self.colour = (191, 128, 255) #Light Purple

        '''

###test for charge view ###    
def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def main():

    #trial in pygame
    background_colour = (255,255,255)

    (width, height) = (640, 480)
    pygame.init()

####test for charge view###########################
    smallText = pygame.font.Font("freesansbold.ttf",20)

    
    screen = pygame.display.set_mode((width, height))
    screen.fill(background_colour)
    pygame.display.set_caption('Quark Movement')

    
    bottom = Bottom()
    bottom.drawCircle(screen)
    msg = str(bottom.getCharge())
    
    textSurf, textRect = text_objects(msg, smallText,(255,255,0))
    textRect.center = (98,102)
    screen.blit(textSurf, textRect)
###################################################
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
    
    

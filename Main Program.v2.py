import pygame,quarkclass,sys,particleclass

 
pygame.init()
 
display_width = 1100
display_height = 700

 
white = (255,255,255)
black = (0,0,0) 


up = quarkclass.Up()
antiup = quarkclass.ANTIUp()
down = quarkclass.Down()
antidown = quarkclass.ANTIDown()
charm = quarkclass.Charm()
anticharm = quarkclass.ANTICharm()
top = quarkclass.Top()
antitop = quarkclass.ANTITop()
strange = quarkclass.Strange()
antistrange = quarkclass.ANTIStrange()
bottom = quarkclass.Bottom()
antibottom = quarkclass.ANTIBottom()

proton = particleclass.Proton()
antiproton = particleclass.AntiProton()
neutron = particleclass.Neutron()
antineutron = particleclass.AntiNeutron()
kaonkplus = particleclass.KaonKplus()
kaonk0 = particleclass.KaonK0()
sigmaplus = particleclass.Sigmaplus()
sigma0 = particleclass.Sigma0()
sigmaminus = particleclass.Sigmaminus()
pionplus = particleclass.Pionplus()
pionminus = particleclass.Pionminus()
pion01 = particleclass.Pion01()
pion02 = particleclass.Pion02()


screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Quark Button Generator') 

 
def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()




def button(msg,x,y,w,h,ic,quarks):
   
    mouse = pygame.mouse.get_pos()

    

    quarkpos = [(500,150),(600,150),(550,250)]
   
    pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",11)
    mediumText = pygame.font.Font("freesansbold.ttf",15)

    #colour text depends on colour of button (easier to read)
    if (quarks == 1) or (quarks == 3) or (quarks == 5) or (quarks == 7) or (quarks == 11):
        textSurf, textRect = text_objects(msg, smallText,black)
    elif quarks == 99:
        textSurf, textRect = text_objects(msg, mediumText,black)
        
    else:
        textSurf, textRect = text_objects(msg, smallText,white)


    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)


    return [msg,x,y,w,h,ic,quarks]
    
def particle_borders():
    for x in range(400, 700):
        pygame.draw.rect(screen, black, [x, 75, 10, 10])
        pygame.draw.rect(screen, black, [x, 300, 10, 10])

    for y in range(75, 300):
        pygame.draw.rect(screen, black, [400, y, 10, 10])
        pygame.draw.rect(screen, black, [700, y, 10, 10])

def particleinfo_borders():
    for x in range(800,1080):
        pygame.draw.rect(screen, black, [x, 50, 10, 10])
        pygame.draw.rect(screen, black, [x, 450, 10, 10])

    for y in range(50,450):
        pygame.draw.rect(screen, black, [800, y, 10, 10])
        pygame.draw.rect(screen, black, [1080, y, 10, 10])

def quarkdata_borders():
    for x in range(20,250):
        pygame.draw.rect(screen, black, [x, 50, 10, 10])
        pygame.draw.rect(screen, black, [x, 450, 10, 10])

    for y in range(50,450):
        pygame.draw.rect(screen, black, [20, y, 10, 10])
        pygame.draw.rect(screen, black, [250, y, 10, 10])

def nonebutton_borders():
    for x in range(455,655):
        pygame.draw.rect(screen, black, [x, 325, 3, 3])
        pygame.draw.rect(screen, black, [x, 375, 3, 3])

    for y in range(325,375):
        pygame.draw.rect(screen, black, [455, y, 3, 3])
        pygame.draw.rect(screen, black, [655, y, 3, 3])
    
################fix this function asap!!!######################################
def equaltri():
    
    pygame.draw.line(screen,black,(520,150),(580,150),3)
    pygame.draw.line(screen,black,(508,167),(540,232),3)
    pygame.draw.line(screen,black,(591,167),(558,232),3)
###############################################################################
def addQuark(Quarkinfo):
    
    quarks = Quarkinfo[6]
    quarkpos = [(500,150),(600,150),(550,250)]
    if quarks == 0:
        pygame.draw.circle(screen,(up.getColour()),quarkpos[0],(up.getSize()),(up.getSize()))
                        #print("UP QUARK CREATED")
    elif quarks == 1:
        pygame.draw.circle(screen,(antiup.getColour()),quarkpos[0],(antiup.getSize()),(antiup.getSize()))
                        #print("ANTI-UP QUARK CREATED")
    elif quarks == 2:
        pygame.draw.circle(screen,(down.getColour()),quarkpos[0],(down.getSize()),(down.getSize()))
                        #print("DOWN QUARK CREATED")
    elif quarks == 3:
        pygame.draw.circle(screen,(antidown.getColour()),quarkpos[0],(antidown.getSize()),(antidown.getSize()))
                        #print("ANTI-DOWN QUARK CREATED")
    elif quarks == 4:
        pygame.draw.circle(screen,(charm.getColour()),quarkpos[0],(charm.getSize()),(charm.getSize()))
                        #print("CHARM QUARK CREATED")
    elif quarks == 5:
        pygame.draw.circle(screen,(anticharm.getColour()),quarkpos[0],(anticharm.getSize()),(anticharm.getSize()))
                        #print("ANTI-CHARM QUARK CREATED")
    elif quarks == 6:
        pygame.draw.circle(screen,(top.getColour()),quarkpos[0],(top.getSize()),(top.getSize()))
                        #print("TOP QUARK CREATED")
    elif quarks == 7:
        pygame.draw.circle(screen,(antitop.getColour()),quarkpos[0],(antitop.getSize()),(antitop.getSize()))
                        #print("ANTI-TOP QUARK CREATED")
    elif quarks == 8:
        pygame.draw.circle(screen,(strange.getColour()),quarkpos[0],(strange.getSize()),(strange.getSize()))
                        #print("STRANGE QUARK CREATED")
    elif quarks == 9:
        pygame.draw.circle(screen,(antistrange.getColour()),quarkpos[0],(antistrange.getSize()),(antistrange.getSize()))
                        #print("ANTI-STRANGE QUARK CREATED")
    elif quarks == 10:
        pygame.draw.circle(screen,(bottom.getColour()),quarkpos[0],(bottom.getSize()),(bottom.getSize()))
                        #print("BOTTOM QUARK CREATED")
    elif quarks == 11:
        pygame.draw.circle(screen,(antibottom.getColour()),quarkpos[0],(antibottom.getSize()),(antibottom.getSize()))
                        #print("ANTI-BOTTOM QUARK CREATED")
    elif quarks == 99:
        noquark = None
        
def printquarks(config,positions):
    for each, pos in zip(config,positions):
        if each is not None:
            pygame.draw.circle(screen,each[5],pos,20,20)

def particletext(particleName,particleType,particleCharge,particleSpin,particleStrangeness):
    #also draws circle when particle created
    nametext = pygame.font.SysFont('freesansbold.ttf', 20)
    TextSurf5, TextRect5 = text_objects(particleName, nametext,black)
    TextSurf6, TextRect6 = text_objects(particleType, nametext,black)
    TextSurf7, TextRect7 = text_objects(particleCharge, nametext,black)
    TextSurf8, TextRect8 = text_objects(particleSpin, nametext,black)
    TextSurf9, TextRect9 = text_objects(particleStrangeness, nametext,black)
    

    TextRect5.center = (155,100)
    TextRect6.center = (155,175)
    TextRect7.center = (155,250)
    TextRect8.center = (155,325)
    TextRect9.center = (155,400)
    
    
    screen.blit(TextSurf5, TextRect5)
    screen.blit(TextSurf6, TextRect6)
    screen.blit(TextSurf7, TextRect7)
    screen.blit(TextSurf8, TextRect8)
    screen.blit(TextSurf9, TextRect9)

def filledparticle(filled):
    if filled == True:
        pygame.draw.circle(screen,(0,0,0),(550,190),100,5)

#def particletext1(parCharge)

    
     
def main():
   QUARKPOS = [(500,150),(600,150),(550,250)]
   p = particleclass.Particle() 
   running = True
   texttoprint = []

   chargeview = False
   refresh = False
   
   while running:
        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',75)
        headingText = pygame.font.Font('freesansbold.ttf',25)
        infoFont = pygame.font.SysFont('Comic Sans MS', 13)
        nametext = pygame.font.SysFont('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects("Quarks", largeText,black)
        TextSurf3, TextRect3 = text_objects("Particle Info", headingText,black)
        TextSurf4, TextRect4 = text_objects("Particle Data", headingText,black)
        TextSurf10, TextRect10 = text_objects("Name: ", nametext,black)
        TextSurf11, TextRect11 = text_objects("Type: ", nametext,black)
        TextSurf12, TextRect12 = text_objects("Charge: ", nametext,black)
        TextSurf13, TextRect13 = text_objects("Spin: ", nametext,black)
        TextSurf14, TextRect14 = text_objects("Strangeness: ", nametext,black)
        
        TextRect.center = ((display_width/2),(435))
        TextRect3.center = (940,20)
        TextRect4.center = (135,20)
        TextRect10.center = (65,100)
        TextRect11.center = (60,175)
        TextRect12.center = (70,250)
        TextRect13.center = (60,325)
        TextRect14.center = (90,400)

        screen.blit(TextSurf4,TextRect4)
        screen.blit(TextSurf3,TextRect3)
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf10, TextRect10)
        screen.blit(TextSurf11, TextRect11)
        screen.blit(TextSurf12, TextRect12)
        screen.blit(TextSurf13, TextRect13)
        screen.blit(TextSurf14, TextRect14)
        


        buttons = []
        button("Quarks",0,500,110,50,white,99)
        button(("Anti-Quarks"),0,600,110,50,white,99)
        #QUARKS
        buttons.append(button("Up",130,500,100,50,(up.getColour()),0))
        buttons.append(button("Down",310,500,100,50,(down.getColour()),2))
        buttons.append(button("Charm",475,500,100,50,(charm.getColour()),4))
        buttons.append(button("Top",640,500,100,50,(top.getColour()),6))
        buttons.append(button("Strange",805,500,100,50,(strange.getColour()),8))
        buttons.append(button("Bottom",970,500,100,50,(bottom.getColour()),10))

        #AntiQuarks
        buttons.append(button("Anti-Up",130,600,100,50,(antiup.getColour()),1))
        buttons.append(button("Anti-Down",310,600,100,50,(antidown.getColour()),3))
        buttons.append(button("Anti-Charm",475,600,100,50,(anticharm.getColour()),5))
        buttons.append(button("Anti-Top",640,600,100,50,(antitop.getColour()),7))
        buttons.append(button("Anti-Strange",805,600,100,50,(antistrange.getColour()),9))
        buttons.append(button("Anti-Bottom",970,600,100,50,(antibottom.getColour()),11) )
        refresh = button("Refresh",450,15,200,50,(100,100,100),99)
        buttons.append(button("None",455,325,200,50,(255,255,255),99))

        #edits -> making charge view button - extra functionallity
        chargeview = button("ChargeView",275,100,120,50,(168,50,186),99)

        
      
        particle_borders()
        particleinfo_borders()
        quarkdata_borders()
        equaltri()
        nonebutton_borders()
        text = []
    
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if (refresh[1] < x < refresh[1] + refresh[3]) and (refresh[2] < y < refresh[2] + refresh[4]):
                    p.clear()
                    texttoprint = []
                    
              #edits -> making charge view button - extra functionallity
              #  if p.isSpace() == False:
              #      if (chargeview[1] < x < chargeview[1] + chargeview[3]) and (chargeview[2] < y < chargeview[2] + chargeview[4]):
                        
                
                for each in buttons:
                    if (each[1] < x < each [1] + each [3]) and (each[2] < y < each[2] + each [4]) :
                        abdb = p.addQuark(each)

                        paridentify = p.sorting_func(each)
                        
                        if paridentify == proton.quarkMakeup():
                            texttoprint = []
                            with open("Proton.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = proton.getName()
                                particleType = proton.getPartype()
                                particleCharge = proton.getCharge()
                                particleSpin = proton.getSpin()
                                particleStrangeness = proton.getStrangeness()
                    
                        
                        elif paridentify == antiproton.quarkMakeup():    
                            texttoprint = []                         
                            with open("Anti-Proton.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = antiproton.getName()
                                particleType = antiproton.getPartype()
                                particleCharge = antiproton.getCharge()
                                particleSpin = antiproton.getSpin()
                                particleStrangeness = antiproton.getStrangeness()
                            

                        elif paridentify == neutron.quarkMakeup():
                            texttoprint = []                         
                            with open("Neutron.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = neutron.getName()
                                particleType = neutron.getPartype()
                                particleCharge = neutron.getCharge()
                                particleSpin = neutron.getSpin()
                                particleStrangeness = neutron.getStrangeness()

                        elif paridentify == antineutron.quarkMakeup():
                            texttoprint = []                         
                            with open("Anti-Neutron.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = antineutron.getName()
                                particleType = antineutron.getPartype()
                                particleCharge = antineutron.getCharge()
                                particleSpin = antineutron.getSpin()
                                particleStrangeness = antineutron.getStrangeness()

                        elif paridentify == kaonkplus.quarkMakeup():
                            texttoprint = []                         
                            with open("KaonK+.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = kaonkplus.getName()
                                particleType = kaonkplus.getPartype()
                                particleCharge = kaonkplus.getCharge()
                                particleSpin = kaonkplus.getSpin()
                                particleStrangeness = kaonkplus.getStrangeness()

                        elif paridentify == kaonk0.quarkMakeup():
                            texttoprint = []                         
                            with open("KaonK0.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = kaonk0.getName()
                                particleType = kaonk0.getPartype()
                                particleCharge = kaonk0.getCharge()
                                particleSpin = kaonk0.getSpin()
                                particleStrangeness = kaonk0.getStrangeness()

                        elif paridentify == sigmaplus.quarkMakeup():
                            texttoprint = []                         
                            with open("SigmaPlus.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = sigmaplus.getName()
                                particleType = sigmaplus.getPartype()
                                particleCharge = sigmaplus.getCharge()
                                particleSpin = sigmaplus.getSpin()
                                particleStrangeness = sigmaplus.getStrangeness()
                                                    
                        elif paridentify == sigma0.quarkMakeup():
                            texttoprint = []                         
                            with open("Sigma0.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = sigma0.getName()
                                particleType = sigma0.getPartype()
                                particleCharge = sigma0.getCharge()
                                particleSpin = sigma0.getSpin()
                                particleStrangeness = sigma0.getStrangeness()
                                
                        elif paridentify == sigmaminus.quarkMakeup():
                            texttoprint = []                         
                            with open("SigmaMinus.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = sigmaminus.getName()
                                particleType = sigmaminus.getPartype()
                                particleCharge = sigmaminus.getCharge()
                                particleSpin = sigmaminus.getSpin()
                                particleStrangeness = sigmaminus.getStrangeness()

                        elif paridentify == pionplus.quarkMakeup():
                            texttoprint = []                         
                            with open("PionPlus.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = pionplus.getName()
                                particleType = pionplus.getPartype()
                                particleCharge = pionplus.getCharge()
                                particleSpin = pionplus.getSpin()
                                particleStrangeness = pionplus.getStrangeness()

                        elif paridentify == pionminus.quarkMakeup():
                            texttoprint = []                         
                            with open("PionMinus.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = pionminus.getName()
                                particleType = pionminus.getPartype()
                                particleCharge = pionminus.getCharge()
                                particleSpin = pionminus.getSpin()
                                particleStrangeness = pionminus.getStrangeness()

                        elif paridentify == pion01.quarkMakeup():
                            texttoprint = []                         
                            with open("Pion0.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = pion01.getName()
                                particleType = pion01.getPartype()
                                particleCharge = pion01.getCharge()
                                particleSpin = pion01.getSpin()
                                particleStrangeness = pion01.getStrangeness()

                        elif paridentify == pion02.quarkMakeup():
                            texttoprint = []                         
                            with open("Pion0.txt","r") as f:
                                for line in f:
                                    text.append(line + "\n")
                                    texttoprint.append("")
                            for i in range(len(text)):
                                filled = True
                                texttoprint[i] = text[i]
                                particleName = pion02.getName()
                                particleType = pion02.getPartype()
                                particleCharge = pion02.getCharge()
                                particleSpin = pion02.getSpin()
                                particleStrangeness = pion02.getStrangeness()
                
                        elif p.isSpace() == False:
                            filled = False
                            texttoprint = ["Quark Configuration does not exist"]
                            particleName = "N/A"
                            particleType = "N/A"
                            particleCharge = "N/A"
                            particleSpin = "N/A"
                            particleStrangeness = "N/A"
        for i in range(len(texttoprint)):
            TextSurf2, TextRect2 = text_objects(texttoprint[i], infoFont,black)
            screen.blit(TextSurf2, (820,73+i*20))
            particletext(particleName,particleType,particleCharge,particleSpin,particleStrangeness)
            filledparticle(filled)

        
        
        
        
        printquarks(p.quarkMakeup(), QUARKPOS)
        


        
        pygame.display.update()
        
        
    
main()


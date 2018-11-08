import sys
import pygame

pygame.init()
background_colour = (255,255,255)
#w = int(input("width of screen: "))
#h = int(input("height of screen: "))

#w = 1000
#h = 800
#size = w, h 


screen = pygame.display.set_mode((1000,800))

#Enables for an image to be importing into pygame
standardm = pygame.image.load("standardmodel.png")
a = int(input("width of image: "))
b = int(input("height of image: "))
picture = pygame.transform.scale(standardm, (a, b))

x = (w/2)-(b/2)
y = (h/2)-(a/2)
screen.blit(picture,(x,y))

#######edit this bit 
mouse = pygame.mouse.get_pos()
if 278+74 > mouse[0] > 352 and 246+114 > mouse[1] > 360:
    print("Pressed button")
#################################                
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        #x, y = pygame.mouse.get_pos()
        #print(x,y)
        if event.type == pygame.QUIT:
             pygame.quit(); sys.exit();
        if event.type == pygame.QUIT:
           running = False

       #if event.type == pygame.MOUSEBUTTONDOWN:
            
            

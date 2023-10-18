import pygame, random
import pygame, sys
pygame.init()
#r = int(input("Choose a number from 1-255"))
#g = int(input("Choose a number from 1-255"))
#b = int(input("Choose a number from 1-255"))
screen = pygame.display.set_mode((800,600))
gold=(255,215,0)
dgold=(255,215,50)
black=(0,0,0)
brown=(150,65,0)
dbrown=(145,65,0)
white=(255,255,255)
grey=(50,50,50)
#Pc = (r,g,b)
#screen.fill(Pc)
screen.fill(black)
pygame.draw.arc(screen, dbrown, (675,100,75,150),100, 250, 300)
pygame.draw.rect(screen, dbrown, (65,100,650,350))
pygame.draw.arc(screen, dbrown, (25,100,75,150),100, 250, 300)
pygame.draw.rect(screen,brown, (25,175,700,350))
pygame.draw.rect(screen, black, (20,170,775,5))
pygame.draw.rect(screen, brown, (100,175,650,350))
pygame.draw.rect(screen, grey, (355,175,50,50))
pygame.draw.rect(screen, black, (367,180,25,30))
pygame.draw.rect(screen, grey, (380,190,15,15))

pygame.draw.circle(screen, gold, (65,200),10)
pygame.draw.circle(screen, gold, (65,250),10)
pygame.draw.circle(screen, gold, (65,300),10)
pygame.draw.circle(screen, gold, (65,350),10)
pygame.draw.circle(screen, gold, (65,400),10)
pygame.draw.circle(screen, gold, (65,450),10)
pygame.draw.circle(screen, gold, (65,500),10)

pygame.draw.circle(screen, gold, (710,200),10)
pygame.draw.circle(screen, gold, (710,250),10)
pygame.draw.circle(screen, gold, (710,300),10)
pygame.draw.circle(screen, gold, (710,350),10)
pygame.draw.circle(screen, gold, (710,400),10)
pygame.draw.circle(screen, gold, (710,450),10)
pygame.draw.circle(screen, gold, (710,500),10)



#change

pygame.display.update()

while( True ):
    for event in pygame.event.get():
        #check if the user closed the window
        if(event.type== pygame.QUIT):
            #end the program
            pygame.quit()
            sys.exit()
randPoint = (random.randint(0,500), random.randint(0,400))
def drawScene(window):
    #load an image
    img = pygame.image.load("img.png")
    window.blit(img,50, 50)

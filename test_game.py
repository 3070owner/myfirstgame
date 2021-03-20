import pygame
import sys
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

blueScore=0
redScore=0
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
troll = (255,255,255)
kx=3
ky=3

greenSpeed=3.5

pygame.init()
pygame.display.set_caption("pygame")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_greenX = 350
pos_greenY = 330

pos_redX = 50
pos_redY = 50

pos_blueX = 750
pos_blueY = 700

pos_trollX = 250
pos_trollY = 650

pos_trollXmove=kx
pos_trollYmove=ky


def blueSpawn():
    global pos_blueX
    global pos_blueY
    pos_blueX = random.randint(30,750)
    pos_blueY = random.randint(30,750)
def redSpawn():
    global pos_redX
    global pos_redY
    pos_redX = random.randint(30,750)
    pos_redY = random.randint(30,750)
def greenSpawn():
    global pos_greenX
    global pos_greenY
    pos_greenX = random.randint(30,750)
    pos_greenY = random.randint(30,750)



clock=pygame.time.Clock()
while True:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
    pos_trollX=pos_trollX+pos_trollXmove
    pos_trollY=pos_trollY+pos_trollYmove
    if pos_trollX>700:
        if kx<23:
            kx+=1
        pos_trollXmove=-kx
        if pos_trollY>0:
            pos_trollY+=0.5
        else:
            pos_trollY-=0.5
    if pos_trollX<100:
        if kx<28:
            kx+=1
        if pos_trollY>0:
            pos_trollY+=0.5
        else:
            pos_trollY-=0.5
        pos_trollXmove=kx
    if pos_trollY>700:
        if ky<27:
            ky+=1
        pos_trollYmove=-ky
        if pos_trollX>0:
            pos_trollX+=0.5
        else:
            pos_trollX-=0.5
    if pos_trollY<100:
        if ky<25:
            ky+=1
        pos_trollYmove=ky
        if pos_trollX>0:
            pos_trollX+=0.5
        else:
            pos_trollX-=0.5



    key_event = pygame.key.get_pressed()

    
    if key_event[pygame.K_LEFT]:
        pos_blueX -= 3
        
    if key_event[pygame.K_RIGHT]:
        pos_blueX +=3
       
    if key_event[pygame.K_UP]:
        pos_blueY -=3
        
    if key_event[pygame.K_DOWN]:
        pos_blueY +=3
    
    if key_event[pygame.K_a]:
        pos_redX -= 3
        
    if key_event[pygame.K_d]:
        pos_redX +=3
        
    if key_event[pygame.K_w]:
        pos_redY -=3
        
    if key_event[pygame.K_s]:
        pos_redY +=3
    
    if key_event[pygame.K_h]:
        pos_greenX -= greenSpeed
                  

    if key_event[pygame.K_k]:
        pos_greenX +=greenSpeed

    if key_event[pygame.K_u]:
        pos_greenY -=greenSpeed

    if key_event[pygame.K_j]:
        pos_greenY +=greenSpeed       
            
    if pos_blueY>800 or pos_blueY<-10:
            blueScore-=1
            blueSpawn()
            print("blueScore:",blueScore)
    if pos_blueY>800 or pos_blueY<-10:
            blueScore-=1
            blueSpawn()
            print("blueScore:",blueScore)
    if abs(pos_greenX-pos_blueX)<=19 and abs(pos_greenY-pos_blueY)<=19:
            blueScore +=1
            print("blueScore:",blueScore)
            greenSpawn()
    if abs(pos_trollX-pos_blueX)<=19 and abs(pos_trollY-pos_blueY)<=19:
            blueScore-=1
            blueSpawn()
            print("blueScore:",blueScore)
    if pos_redX>800 or pos_redX<-10:
            redScore-=1
            redSpawn()
            print("redScore:",redScore)
    if pos_redY>800 or pos_redY<-10:
            redScore-=1
            redSpawn()
            print("redScore:",redScore)
    if abs(pos_greenX-pos_redX)<=19 and abs(pos_greenY-pos_redY)<=19:
            redScore +=1
            print("redScore:",redScore)
            greenSpawn()
    if abs(pos_trollX-pos_redX)<=19 and abs(pos_trollY-pos_redY)<=19:
            redScore-=1
            redSpawn()
            print("redScore:",redScore)
    if pos_greenX>800 or pos_greenX<-10:
            greenSpawn()
    if abs(pos_greenX-pos_blueX)<=19 and abs(pos_greenY-pos_blueY)<=19:
            blueScore +=1
            print("blueScore:",blueScore)
            greenSpawn()   
    if abs(pos_greenX-pos_redX)<=19 and abs(pos_greenY-pos_redY)<=19:
            redScore +=1
            print("redScore:",redScore)
            greenSpawn()
    if abs(pos_trollX-pos_greenX)<=19 and abs(pos_trollY-pos_greenY)<=19:
            pos_greenX=350
            pos_greenY=350
            if greenSpeed>2:
                greenSpeed-=0.1



    screen.fill(black)
    pygame.draw.rect(screen, troll,pygame.Rect(pos_trollX,pos_trollY,20,20))
    pygame.draw.rect(screen, red, pygame.Rect(pos_redX,pos_redY,20,20))
    pygame.draw.rect(screen, green, pygame.Rect(pos_greenX,pos_greenY,20,20))
    pygame.draw.rect(screen, blue, pygame.Rect(pos_blueX,pos_blueY,20,20))
    pygame.display.update()

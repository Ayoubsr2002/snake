
import pygame
import time
import random as r

pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill((0,255,0))

a=20
b=0
score=0

font= pygame.font.SysFont("calibri",20)
font1=pygame.font.SysFont("verdana",60)
text1=font1.render("Vous avez perdu",True,(0,0,0))
font2=pygame.font.SysFont("verdana",25)
texte3=font2.render("cliquez sur espace pour rejouer",True,(200,200,200))

texte4=font1.render("snake",True,(0,0,0))

texte5=font2.render("cliquez sur espace pour commencer le jeu",True,(250,250,250))

image1=pygame.image.load("pngwing.com (1).png")

class body:
    def __init__(self,posx,posy) :
        self.posx=posx
        self.posy=posy

L=[]
L.append(body(300,300))
L.append(body(280,300))



def mouvement() :
    global L ;
    n=len(L)
    e=0
    if n>1 :
        for i in range (n-1,0,-1):
            L[i].posx=L[i-1].posx
            L[i].posy=L[i-1].posy

    L[0].posx+=a
    L[0].posy+=b
    
    if L[0].posx >=600 :
        L[0].posx=20
    if L[0].posx<=0 :
        L[0].posx=600
    if L[0].posy >=600 :
        L[0].posy=20
    if L[0].posy<=0 :
        L[0].posy=600

    

def collision(x,y,T) :
    global L,score ;
    T=False
    if x==L[0].posx and y==L[0].posy :
        T=True
        px=L[-1].posx
        py=L[-1].posy
        mouvement()
        L.append(body(px,py))
        score+=5
    return T


def défaite(L):
    global game_over ;
    n=len(L)
    for i in range(1,n) :
            if  L[0].posx==L[i].posx and L[0].posy==L[i].posy :
                return 1











T=True
clock=pygame.time.Clock()
running=True
menu=True
game_over=False
c=None
while running :
    d=time.time()
    if menu :
        screen.fill((0,255,0)) # à ne pas oublier
        screen.blit(texte4,(220,250))
        screen.blit(image1,(200,10))
        screen.blit(texte5,(40,350))
        pygame.display.flip()
        for event in pygame.event.get() :
            if event.type== pygame.QUIT :
                running=False
                pygame.quit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    menu=False

    if menu==False :
        if not game_over :
            d=10+int(score/15)
            text=font.render("score :"+str(score),True,(0,0,0))
            clock.tick(d)
            screen.fill((0,255,0)) # à ne pas oublier
            screen.blit(text,(10,10))
            for i in range(0,len(L)) :
                pygame.draw.rect(screen,(0,128,0),[L[i].posx,L[i].posy,20,20])
            if c==None :
                if T==True :
                    x=r.randint(1,18)*20
                    y=r.randint(1,18)*20
                    T=False
                pygame.draw.rect(screen,(255,0,0),[x,y,20,20])

                T=collision(x,y,T)
                mouvement()
                pygame.display.flip()



                



                d=0
                for event in pygame.event.get() :
                    if event.type== pygame.QUIT :
                        running=False
                        pygame.quit()
                    if event.type == pygame.KEYDOWN :
                        if event.key == pygame.K_UP and b!=20:
                            b=-20
                            a=0
                        if  event.key == pygame.K_DOWN and b!=-20:
                            b=20
                            a=0
                        if event.key == pygame.K_RIGHT and a!=-20 :
                            b=0
                            a=20
                        if  event.key == pygame.K_LEFT and a!=20:
                            b=0
                            a=-20
                        mouvement()
                f=time.time()
            
                c=défaite(L)
            else :
                c+=1
                if c==11 :
                    c=None
                    game_over=True
                    score=0
        if  game_over :
            screen.fill((0,255,0)) # à ne pas oublier
            screen.blit(text1,(50,250))
            screen.blit(image1,(200,10))
            screen.blit(texte3,(115,350))
            pygame.display.flip()
            for event in pygame.event.get() :
                if event.type== pygame.QUIT :
                    running=False
                    pygame.quit()
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_SPACE:
                        game_over=False
                        L=[]
                        L.append(body(300,300))

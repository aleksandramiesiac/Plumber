import pygame, sys,os, math, random
from pygame.locals import *
from rura import pipe
import copy
#from plik import nazwa klasy
pygame.init()
# utworzenie okna
window = pygame.display.set_mode((1000, 600))
 
# ustawiamy etykietę
pygame.display.set_caption('Gra w pyGame')

# ładujemy plik graficzny
r_krzywa = pipe('r_krzywa')
r_prosta = pipe('r_prosta')
caly1 = pipe('caly')
caly = pygame.transform.scale(caly1.obj, (900,100))
cale = pygame.transform.scale(caly1.obj, (1000,600))

# pobieramy informacje o ekranie - tle
screen = pygame.display.get_surface()

#MUZYKA i DŹWIĘKI
winSound = pygame.mixer.Sound("wygrana.wav")
loseSound = pygame.mixer.Sound("przegrana.wav")
waterSound = pygame.mixer.music.load("woda.mp3")


rura = [r_prosta,r_krzywa]
x = []
f = open("level.txt","r")
ran=int(f.read())


f.close()
ran= (ran+1)%12+1
# 1,3,4,6,7,9,10,11,12
if ran ==2 or ran==5 or ran==10:
    ran+=1
random.seed(ran)


#inicjacja kolejności kafelek
for i in range(41):
    x.append(copy.copy(rura[random.randint(-1,1)]))
for i in range(10):
    x.append(copy.copy(caly1))
start = copy.copy(r_prosta)
start1 = start.rotacja().obj
koniec = copy.copy(r_prosta)
koniec = koniec.rotacja().obj

#ustawienia początkowe
def poczatek(x,start,caly,y,z,prostokacik,pXY,language):
    for i in range(40):
        if i%10==0:
            y+=100
            z = 0
        screen.blit(x[i].obj,(0+100*z,y))       
        z+=1
    screen.blit(caly, (100,0))
    screen.blit(start1,(0,0))
    screen.blit(caly, (0,500))
    screen.blit(koniec,(900,500))
    screen.blit(prostokacik,pXY)
    if language:
        pust=pygame.font.Font(None,35).render("Ustawienia",True,(255,125,255))
    else:
        pust=pygame.font.Font(None,35).render("Settings",True,(255,125,255))

    pustXY=pust.get_rect()
    pustXY.x=855
    pustXY.y=33
    screen.blit(pust,pustXY)
    

#Napisy aby zatrzymać grę i ją potem wnowić
czcionka = pygame.font.Font(None,100)
czcion=pygame.font.Font(None, 40)
stop = czcion.render("Pauza",True,(255,125,255))
stopp = czcion.render("Pause",True,(255,125,255))
start = czcion.render("Start", True,(255,125,255))
startxy=start.get_rect()
startxy.x=110
startxy.y=33

def nastepny(language):
    screen.blit(cale,(0,0))
    if language:
        nast = czcionka.render("Nastęna gra", True, (125,255,255))
    else:
        nast = czcionka.render("Next game",True,(125,255,255))
    nastXY=nast.get_rect()
    nastXY.center=(450,250)
    screen.blit(nast, nastXY)

#zmiana ustawien:
def settings(dzwiek,poz,language):
    screen.blit(cale,(0,0))
    if language:
        ustaw=czcionka.render("Ustawienia",True,(125,255,255))
    else:
        ustaw=czcionka.render("Settings",True,(125,255,255))
    ustawXY=ustaw.get_rect()
    ustawXY.center=(500,150)
    screen.blit(ustaw,ustawXY)
    if language:
        dzwieki = pygame.font.Font(None,50).render("Dźwięki",True,(255,255,255))
    else:
        dzwieki = pygame.font.Font(None,50).render("Sound",True,(255,255,255))
    dzXY = dzwieki.get_rect()
    dzXY.x=350
    dzXY.y=250
    screen.blit(dzwieki,dzXY)
    if language:
        poziom = pygame.font.Font(None,50).render("Poziom",True,(255,255,255))
    else:
        poziom = pygame.font.Font(None,50).render("Level",True,(255,255,255))
    poXY = poziom.get_rect()
    poXY.x=350
    poXY.y=300
    screen.blit(poziom,poXY)

    #zmienne dzwieki
    if language:
        if dzwiek == True:
            wlacz=pygame.font.Font(None,50).render("Włączone",True,(255,255,255))
        else:
            wlacz=pygame.font.Font(None,50).render("Wyłączone",True,(255,255,255))
    else:
        if dzwiek == True:
            wlacz=pygame.font.Font(None,50).render("On",True,(255,255,255))
        else:
            wlacz=pygame.font.Font(None,50).render("Off",True,(255,255,255))
    wlaXY=wlacz.get_rect()
    wlaXY.x=600
    wlaXY.y=250
    screen.blit(wlacz,wlaXY)

    sta= czcionka.render("Start",True,(125,255,255))
    staXY=sta.get_rect()
    staXY.center=(500,450)
    screen.blit(sta,staXY)
    #zmienny poziom
    if language:
        if poz==1:
            pocz=pygame.font.Font(None,50).render("Łatwy",True,(255,255,255))
        elif poz==2:
            pocz=pygame.font.Font(None,50).render("Średni",True,(255,255,255))
        else:
            pocz=pygame.font.Font(None,50).render("Trudny",True,(255,255,255))
    else:
        if poz==1:
            pocz=pygame.font.Font(None,50).render("Easy",True,(255,255,255))
        elif poz==2:
            pocz=pygame.font.Font(None,50).render("Medium",True,(255,255,255))
        else:
            pocz=pygame.font.Font(None,50).render("Hard",True,(255,255,255))
    poczXY=pocz.get_rect()
    poczXY.x=600
    poczXY.y=300
    screen.blit(pocz,poczXY)
    if language:
        lan = pygame.font.Font(None, 50). render("Język",True,(255,255,255))
        len = pygame.font.Font(None, 50). render("Polski",True,(255,255,255))
    else:
        lan = pygame.font.Font(None, 50). render("Language",True,(255,255,255))
        len = pygame.font.Font(None, 50). render("English",True,(255,255,255))

    lanXY=lan.get_rect()
    lanXY.x=350
    lanXY.y=200
    screen.blit(lan,lanXY)
    lenXY = len.get_rect()
    lenXY.x = 600
    lenXY.y=200
    screen.blit(len,lenXY)

def wypisz(napis,xy,color):
    napis = str(napis)
    cos = czcionka.render(napis,True,color)
    nxy = cos.get_rect()
    nxy = xy
    screen.blit(cos,nxy)

def pause(language):
    if language:
        pauza = czcionka.render("Pauza", True, (255,125,255))
    else:
        pauza = czcionka.render("pause", True, (255,125,255))
    pxy = pauza.get_rect()
    pxy.center = (500,300)
    screen.blit(cale,(0,0))
    screen.blit(pauza,pxy)
    if language:
        pust=pygame.font.Font(None,35).render("Ustawienia",True,(255,125,255))
    else:
        pust=pygame.font.Font(None,35).render("Settings",True,(255,125,255))
    pustXY=pust.get_rect()
    pustXY.x=855
    pustXY.y=33
    screen.blit(pust,pustXY)

#kwadrat jako woda i współrzędne na początku
kwad = pygame.Surface((34,34))
kwad.fill((0,0,250))
kwadXY = kwad.get_rect()
kwadXY.x = 33
kwadXY.y = 0

# prostokąt określający długość czasu
prostokacik = pygame.Surface((600,50))
prostokacik.fill((255,255,255))
pXY = prostokacik.get_rect()
pXY.x=250
pXY.y=25


#lecacy czas 
czas = pygame.Surface((2,50))
czas.fill((0,0,0))
czXY = czas.get_rect()
czXY.x=848
czXY.y=25

pygame.display.flip()

#zmienne określające szybkość pętli
fps = pygame.time.Clock()
clock= pygame.time.Clock()

# kursor myszki jest widoczny
pygame.mouse.set_visible(True) 

def woda(obr,x,y):
    k_obj= [copy.copy([x,y]),copy.copy([x,y]),copy.copy([x,y]),copy.copy([x,y])]
    for i in range (33):
        #idzie w lewo
        if k_obj[0][0]>(x-33):
            if  obr.wyjscia[3]==1:
                k_obj[0][0]-=1
                screen.blit(kwad,k_obj[0])
                
                
        #drugi idzie w dol
        if k_obj[1][1]<(y+33):
            if obr.wyjscia[2]==1:
                k_obj[1][1]+=1
                screen.blit(kwad,k_obj[1])
        # trzeci idzie w prawo
        if k_obj[2][0]<(x+33):
            if obr.wyjscia[1]==1:
                k_obj[2][0]+=1
                screen.blit(kwad,k_obj[2])
        # czwarty idzie w gore
        if k_obj[3][1]>(y-33):
            if obr.wyjscia[0]==1:
                k_obj[3][1]-=1
                screen.blit(kwad,k_obj[3])
#współrzędne pomocnicze do wypełniania wodą
kk=0
ll=0
oo=0
nn=0
def wypełnianie(obj,i,k,l,o,n):
    # z prawej
    if (i+1)%10!=0 and i<40:
        if obj[i+1].czy==0 and obj[i].wyjscia[1]==1:
            
            if obj[i+1].wyjscia[3]==1 and k<66:
                zx=100*(i%10)+66+k
                k+=1
                zy=33+10*(i-(i%10)+10)
                screen.blit(kwad,(zx,zy))
                
            elif obj[i+1].wyjscia[3]==1 and 66==k:
                zx=100*(i%10)+66+k
                zy=33+10*(i-(i%10)+10)
                
                woda(obj[i+1],zx,zy)
                obj[i].czy=1
            else:
                                   
                k=0
    # z dołu
    if (i+10)<40:
        if obj[i+10].czy==0 and obj[i].wyjscia[2]==1:
            if obj[i+10].wyjscia[0]==1 and o<66:
                mx=100*(i%10)+33
                my=10*(i-(i%10)+10)+66+o
                o+=1
                screen.blit(kwad,(mx,my))                
            elif obj[i+10].wyjscia[0]==1 and  66==o:
                
                mx=100*(i%10)+33
                my=10*(i-(i%10)+10)+66+o
                o+=1
                woda(obj[i+10],mx,my)
                obj[i].czy=1
            
            else:
                                   
                o=0
    #z góry 
    if (i-10)>0:
        if obj[i-10].czy==0 and obj[i].wyjscia[0]==1:
            if obj[i-10].wyjscia[2]==1 and l<66:
                lx=100*(i%10)+33
                ly=10*(i-(i%10)+10)-l
                l+=1
                screen.blit(kwad,(lx,ly))
            elif obj[i-10].wyjscia[2]==1 and 66==l:
                lx=100*(i%10)+33
                ly=10*(i-(i%10)+10)-l
                l+=1
                woda(obj[i-10],lx,ly)
                obj[i].czy=1
            else:
                                   
                l=0
    # z lewej
    if i%10!=0 and i-1>0:
        if obj[i-1].czy==0 and obj[i].wyjscia[3]==1:
            if obj[i-1].wyjscia[1]==1 and n<66:
                nx=100*(i%10)-n 
                ny = 10*(i-(i%10)+10)+33
                n+=1
                screen.blit(kwad,(nx,ny))
            elif obj[i-1].wyjscia[1]==1 and 66==n:
                nx=100*(i%10)-n 
                ny = 10*(i-(i%10)+10)+33
                n+=1
                woda(obj[i-1],nx,ny)
                obj[i].czy=1
            else:
                                   
                n=0
#parametr pomocniczy do chodzenia pomiędzy kafelkami
p=0    
i=0
j=0
w=0
#współrzędne lecącej wody - na końcu
kwXY=kwad.get_rect()
kwXY.x=933
kwXY.y=466
#parametr pomocniczy do pauza-start
licznik =0
param =1
#ustwienia przed grą
para=0
pocz=1
dzwiek=True
language = True
kon=0
while True:
    settings(dzwiek,pocz,language)
    for event in pygame.event.get():      
        m = pygame.mouse.get_pos() 
        if event.type == QUIT:
            sys.exit(0)
        if event.type == MOUSEBUTTONDOWN:
            if 595<=m[0] and m[0]<=775 and 245<=m[1] and m[1]<=300:
                dzwiek = (int(dzwiek)+1)%2
                dzwiek = bool(dzwiek)
            if 595<=m[0] and m[0]<=855 and 300<=m[1] and m[1]<=355:
                pocz=pocz%3+1
            if 595<=m[0] and m[0]<=775 and 195<=m[1] and m[1]<=245:
                language = (int(language)+1)%2
                language = bool(language)
            if 420<=m[0] and m[0]<=575 and 425<=m[1] and m[1]<=475:
                para+=1
    pygame.display.update()
    if para>0:
        break
licznik1=0        
#wyglad ekranu na początku        
poczatek(x,start,caly,0,0,prostokacik,pXY,language)
while True:
    if czXY.x >= 250:
        while czXY.x >= 250:
            if language:
                if param==1:
                    screen.blit(stop,startxy)
            else:
                if param==1:
                    screen.blit(stopp,startxy)
            if param==0 and licznik1!=1:
                screen.blit(start,startxy)
            czXY.x-=1*param
            screen.blit(czas,czXY)
            for event in pygame.event.get():
                m = pygame.mouse.get_pos() 
                if event.type == QUIT:
                    sys.exit(0)
                if event.type == MOUSEBUTTONDOWN:
                    if 0<=m[0] and m[0]<=1000 and 100<=m[1] and m[1]<=500 and param!=0:
                        a=math.floor(m[0]/100)
                        b=math.floor(m[1]/100)-1
                        screen.blit(x[10*b+a].rotacja().obj,(m[0]-m[0]%100,m[1]-m[1]%100))
                    if 100<=m[0] and m[0]<=200 and 25<=m[1] and m[1]<=70 and licznik1!=1:
                        licznik+=1
                        pause(language)
                        if licznik%2==1:
                            param = 0
                        else :
                            poczatek(x,start,caly,0,0,prostokacik,pXY,language)
                            param=1
                    if 850<=m[0] and m[0]<=975 and 30<=m[1] and m[1]<=60 and licznik1!=1:
                        licznik1=1
                        settings(dzwiek,pocz,language)
                        param=0
                    if  595<=m[0] and m[0]<=775 and 245<=m[1] and m[1]<=300 and licznik1==1 and param==0:
                        dzwiek = (int(dzwiek)+1)%2
                        dzwiek = bool(dzwiek)
                        settings(dzwiek,pocz,language)
                    if 595<=m[0] and m[0]<=855 and 300<=m[1] and m[1]<=355 and licznik1==1 and param==0:
                        pocz=pocz%3+1
                        settings(dzwiek,pocz,language)
                    if 595<=m[0] and m[0]<=775 and 195<=m[1] and m[1]<=245 and licznik1==1 and param==0:
                        language = (int(language)+1)%2
                        language = bool(language)
                        settings(dzwiek,pocz,language)
                    if 420<=m[0] and m[0]<=575 and 425<=m[1] and m[1]<=475 and licznik1==1 and param==0:
                        licznik1=0
                        param=1
                        poczatek(x,start,caly,0,0,prostokacik,pXY,language)
                        licznik=0
            pygame.display.update()
            fps.tick(15+15*pocz)                
    else:
        while True:
            #wylewa się woda jak skończy się czas
            if kwadXY.y==0 and dzwiek:
                pygame.mixer.music.play()
            if kwadXY.y<=66:
                kwadXY.y+=1
                screen.blit(kwad,kwadXY)
            elif kwadXY.y>66 and kwadXY.y<=133 and x[i].wyjscia[0]==1:
                kwadXY.y+=1
                screen.blit(kwad,kwadXY)
            elif x[0].wyjscia[0]==1:
                if i==0 and x[i].wyjscia[0]==1:
                    woda(x[i],kwadXY.x,kwadXY.y)
                    x[i].czy=1
                if i <39:
                    wypełnianie(x,i,kk,ll,oo,nn)
                    if kk==67 and ll==67 and oo==67 and nn==67:
                        kk=0
                        ll=0
                        oo=0
                        nn=0
                        if (i+1)%10!=0 and x[i].wyjscia[1]==1 and x[(i+1)].wyjscia[3]==1 and x[i+1].czy==0:
                            i+=1
                        elif x[i].wyjscia[2]==1 and x[i+10].wyjscia[0]==1 and x[i+10].czy==0:
                            i+=10
                        elif i%10!=0 and x[i].wyjscia[3]==1 and x[i-1].wyjscia[1]==1 and x[i-1].czy==0:
                            i-=1
                        elif x[i].wyjscia[0]==1 and x[i-10].wyjscia[2]==1 and x[i-10].czy==0:
                            i-=10
                        else: 
                            if language:
                                wypisz("Przegrana!",(350,250),(125,125,125))
                            else:
                                wypisz("Loooose!",(350,250),(125,125,125))
                            w+=1
                            if w==1 and dzwiek:
                                pygame.mixer.music.pause()
                                loseSound.play()
                    kk+=1
                    ll+=1
                    oo+=1
                    nn+=1       
                elif i==39 and x[i].wyjscia[2]==1 and kwXY.y<566:
                    kwXY.y+=1
                    screen.blit(kwad,kwXY)
                elif kwXY.y==566:
                    if language and kon==0:
                        wypisz("Wygrana!",(350,250),(125,125,125))
                    else:
                        if kon==0:
                            wypisz("Wiin!",(350,250),(125,125,125))
                    for event in pygame.event.get():
                        m=pygame.mouse.get_pos()
                        if event.type ==MOUSEBUTTONDOWN:
                            if kon==0:
                                nastepny(language)
                                kon+=1
                            elif 300<=m[0] and m[0]<=750 and 50<=m[1] and m[1]<=400 :
                                g = open("level.txt","w")
                                g.write(str(ran))
                                g.close()
                                sys.exit(0)
                            else:
                                nastepny(language)
                    i+=1
                    if i==40 and dzwiek:
                        pygame.mixer.music.pause()
                        winSound.play()
                else:
                    w+=1
                    if language:
                        wypisz("Przegrana!",(350,250),(125,125,125))
                    else:
                        wypisz("Loooose!",(350,250),(125,125,125))
                    if w==1 and dzwiek:
                        pygame.mixer.music.pause()
                        loseSound.play()
            else:
                    w+=1
                    if language:
                        wypisz("Przegrana!",(350,250),(125,125,125))
                    else:
                        wypisz("Loooose!",(350,250),(125,125,125))
                    if w==1 and dzwiek:
                        pygame.mixer.music.pause()
                        loseSound.play()
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
            pygame.display.update()
            clock.tick(140)

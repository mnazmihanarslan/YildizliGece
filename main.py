import pygame
import math
import os
import random
import sys
import time
from pygame import mixer

pygame.init()
genislik,yukseklik = 1920,1080
pencere = pygame.display.set_mode((genislik,yukseklik))
FPS = 60
clock = pygame.time.Clock()
pygame.display.set_caption("Yildizli Gece")
ANAMENU = mixer.Sound(os.path.join("sounds","anamenu.wav"))
YILDIZSESI = mixer.Sound(os.path.join("sounds","yildizSesi.wav"))
MUZIK = mixer.Sound(os.path.join("sounds","muzik.wav"))
HASAR = mixer.Sound(os.path.join("sounds","hasar.wav"))
rashfordFont = pygame.font.Font(os.path.join("fonts","Rashford.ttf"),90)
rashfordFontKucuk = pygame.font.Font(os.path.join("fonts","Rashford.ttf"),72)
rashfordSkorFont = pygame.font.Font(os.path.join("fonts","Rashford.ttf"),72)
rashfordSkorFontBuyuk = pygame.font.Font(os.path.join("fonts","Rashford.ttf"),450)
rashfordSkorFontOrta = pygame.font.Font(os.path.join("fonts","Rashford.ttf"),350)
MENU = pygame.image.load(os.path.join("assets","anaMenu.png"))
MENU1 = pygame.image.load(os.path.join("assets","anaMenu1.png"))
MENU2 = pygame.image.load(os.path.join("assets","anaMenu2.png"))
SKORBOARD = pygame.image.load(os.path.join("assets","skorBoard.png"))
SKORBOARD1 = pygame.image.load(os.path.join("assets","skorBoard1.png"))
ARKAPLAN = pygame.image.load(os.path.join("assets","arkaPlan.png"))
CERCEVE = pygame.image.load(os.path.join("assets","cerceve.png"))
VANGOGH = pygame.image.load(os.path.join("assets","vanGogh.png"))
FIRCA = pygame.image.load(os.path.join("assets","firca.png"))
YILDIZ1 = pygame.image.load(os.path.join("assets","yildiz1.png"))
YILDIZ2 = pygame.image.load(os.path.join("assets","yildiz2.png"))
YILDIZ3 = pygame.image.load(os.path.join("assets","yildiz3.png"))
CAN5 = pygame.image.load(os.path.join("assets","kalp1.png"))
CAN4 = pygame.image.load(os.path.join("assets","kalp2.png"))
CAN3 = pygame.image.load(os.path.join("assets","kalp3.png"))
CAN2 = pygame.image.load(os.path.join("assets","kalp4.png"))
CAN1 = pygame.image.load(os.path.join("assets","kalp5.png"))

menuCalisiyor = False
def menu():
    menuCalisiyor = True
    menuTiklama = False
    ANAMENU.play(-1)

    while menuCalisiyor:
        butonOyna = pygame.Rect(78,238,497,236)
        butonCikis = pygame.Rect(78,599,497,236)
        pencere.blit(MENU,(0,0))
        mouseX,mouseY = pygame.mouse.get_pos()
        if butonOyna.collidepoint((mouseX,mouseY)):
            pencere.blit(MENU1,(0,0))
            if menuTiklama:
                ANAMENU.stop()
                menuTiklama = False
                oyun()
        if butonCikis.collidepoint((mouseX,mouseY)):
            pencere.blit(MENU2,(0,0))
            if menuTiklama:
                menuTiklama = False
                pygame.quit()
                sys.exit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menuTiklama = True
        pygame.display.update()
        clock.tick(FPS)

yildiz1Skor = 0
yildiz2Skor = 0
yildiz3Skor = 0
oyunCalisiyor = False
def oyun():
    global yildiz1Skor
    global yildiz2Skor
    global yildiz3Skor
    oyunCalisiyor = True
    fircaSagaGidiyor = True
    fircaSolaGidiyor = False
    yildizKaydi = False
    secimYapildi = False
    vanGoghX,vanGoghY = 670,835
    FircaX,FircaY = 593,-2
    vanGoghHiz = 15
    FircaHiz = 15
    can = 5
    yildiz1Skor = 0
    yildiz2Skor = 0
    yildiz3Skor = 0
    yildizListesi = ["Yildiz 1","Yildiz 2","Yildiz 3"]
    yildizX,yildizY = FircaX+30,FircaY + 100
    MUZIK.play(-1)

    def carpismaFonk(vanGoghX,vanGoghY,yaldizX,yaldizY):
        mesafe = math.sqrt((math.pow(vanGoghX-yaldizX,2)) + (math.pow(vanGoghY-yaldizY,2)))
        if mesafe < 27:
            return True
        else:
            return False

    while oyunCalisiyor:
        pencere.blit(ARKAPLAN,(0,0))
        pencere.blit(VANGOGH,(vanGoghX,vanGoghY))
        pencere.blit(FIRCA,(FircaX,FircaY))
        pencere.blit(CERCEVE,(0,0))

        yildiz1SkorYazi = rashfordFont.render(str(yildiz1Skor),1,(42,21,1))
        yildiz2SkorYazi = rashfordFont.render(str(yildiz2Skor),1,(42,21,1))
        yildiz3SkorYazi = rashfordFont.render(str(yildiz3Skor),1,(42,21,1))
        pencere.blit(yildiz1SkorYazi,(1514,1200))
        pencere.blit(yildiz2SkorYazi,(1645,1200))
        pencere.blit(yildiz3SkorYazi,(1777,1200))

        if can >= 5:
            pencere.blit(CAN5,(1769,150))
        if can >= 4:
            pencere.blit(CAN4,(1696,150))
        if can >= 3:
            pencere.blit(CAN3,(1621,150))
        if can >= 2:
            pencere.blit(CAN2,(1545,150))
        if can >= 1:
            pencere.blit(CAN1,(1472,150))

        if secimYapildi == False:
            yildizSecim = random.choice(yildizListesi)
            secimYapildi = True
                
        if yildizSecim == "Yildiz 1":
            yildizResim = YILDIZ1
        if yildizSecim == "Yildiz 2":
            yildizResim = YILDIZ2
        if yildizSecim == "Yildiz 3":
            yildizResim = YILDIZ3

        if secimYapildi:
            pencere.blit(yildizResim,(yildizX,yildizY))
            yildizY += 13
            yildizKaydi = True

        carpisma = carpismaFonk(vanGoghX,vanGoghY,yildizX,yildizY)
        if carpisma:
            yildizY = FircaY + 100
            yildizX = FircaX + 65
            yildizKaydi = False
            secimYapildi = False
            if yildizSecim == "Yildiz 1":
                YILDIZSESI.play()
                yildiz1Skor += 1
            elif yildizSecim == "Yildiz 2":
                YILDIZSESI.play()
                yildiz2Skor += 1
            elif yildizSecim == "Yildiz 3":
                YILDIZSESI.play()
                yildiz3Skor += 1

        if yildizY >= 900 and carpisma == False:
            yildizY = FircaY + 100
            yildizX = FircaX + 65
            yildizKaydi = False
            secimYapildi = False
            if yildizSecim == "Yildiz 1":
                HASAR.play()
                can -= 1
            elif yildizSecim == "Yildiz 2":
                HASAR.play()
                can -= 1
            elif yildizSecim == "Yildiz 3":
                HASAR.play()
                can -= 1

        if fircaSagaGidiyor:
            FircaX += FircaHiz
            if FircaX > 1104:
                fircaSagaGidiyor = False
                fircaSolaGidiyor = True
                FircaX = 1104

        if fircaSolaGidiyor:
            FircaX -= FircaHiz
            if FircaX < 60:
                fircaSolaGidiyor = False
                fircaSagaGidiyor = True
                FircaX = 60

        tusBasildi = pygame.key.get_pressed()
        for event in pygame.event.get():           
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if tusBasildi[pygame.K_LEFT]:
            vanGoghX -= vanGoghHiz
        if tusBasildi[pygame.K_RIGHT]:
            vanGoghX += vanGoghHiz

        if vanGoghX <= 100:
            vanGoghX = 100
        elif vanGoghX >= 1204:
            vanGoghX = 1204
 
        if can <= 0:
            MUZIK.stop()
            oyunCalisiyor = False
            skorBoard()

        pygame.display.update()
        clock.tick(FPS)

skorBoardCalisiyor = False
def skorBoard():
    global yildiz1Skor
    global yildiz2Skor
    global yildiz3Skor
    skorBoardCalisiyor = True
    skorBoardTiklama = False
    while skorBoardCalisiyor:
        butonMenu = pygame.Rect(1696,976,224,103)
        pencere.blit(SKORBOARD,(0,0))
        yildiz1SkorYazi = rashfordSkorFontBuyuk.render(str(yildiz1Skor),1,(230,199,115))
        yildiz2SkorYazi = rashfordSkorFontBuyuk.render(str(yildiz2Skor),1,(230,199,115))
        yildiz3SkorYazi = rashfordSkorFontBuyuk.render(str(yildiz3Skor),1,(230,199,115))
        toplamSkorYazi = rashfordSkorFontOrta.render(str((yildiz1Skor + yildiz2Skor + yildiz3Skor) * 5),1,(242,151,20))
        pencere.blit(yildiz1SkorYazi,(573,-73))
        pencere.blit(yildiz2SkorYazi,(564,282))
        pencere.blit(yildiz3SkorYazi,(544,638))
        pencere.blit(toplamSkorYazi,(1282,602)) 
        mouseX,mouseY = pygame.mouse.get_pos()
        if butonMenu.collidepoint((mouseX,mouseY)):
            pencere.blit(SKORBOARD1,(0,0))
            if skorBoardTiklama:
                skorBoardTiklama = False
                menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    skorBoardTiklama = True
        pygame.display.update()
        clock.tick(FPS)

menu()
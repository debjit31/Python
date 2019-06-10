import pygame, sys, random
from pygame.locals import *

BLUE = (0, 0, 255)
GREEN= (0, 128, 0)
PURPLE= (128, 0, 128)
RED= (255, 0, 0)
YELLOW= (255, 255, 0)
NAVYBLUE= (0, 0, 128)
WHITE= (255, 255, 255)
BLACK= (0, 0, 0)
ORANGE= (255, 128, 0)
CREAM = (255, 255, 204)

def createDeck(fileName):
    myF=open(fileName,'r')
    shoe =[ln.strip() for ln in myF]
    random.shuffle(shoe)
    return shoe

def dealCards(shoe):
    player = []
    dealer = []
    while len(dealer) < 2:
        player.append(shoe[0])
        player.pop(0)
        dealer.append(shoe[0])
        shoe.pop(0)
    return player, dealer

def findSum(hand):
    hardsum = 0
    softsum = 0
    for card in hand:
        if card[-1].isdigit() and int(card[-1]) != 10:
            hardsum += int(card[-1])
            softsum += int(card[-1])
        if card[-1] in 'JQK' or card[-2:].isdigit():
            hardsum += 10
            softsum += 10
        if card[-1] == 'A':
            hardsum += 11
            softsum += 1
        if softsum == 2:
            hardsum = 12
        return hardsum, softsum

def dealCard(hand, shoe):
    hand.append(shoe[0])
    shoe.pop(0)

def drawText(text, font, surface,x,y):
    textobj = font.render(text,1,BLACK)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrext)

def playGame():
    pygame.init()
    gamex,gamey=(1000,600)
    DISPLAYSURF = pygame.display.set_mode((gamex,gamey))
    DISPLAYSURF.fill(CREAM)
    pygame.display.set_caption('Black Jack')
    banner = pygame.image.load('images/banner.png')
    playButton = pygame.image.load('images/play_button.gif')
    playRect = playButton.get_rect()
    playRect.topleft = (680,350)
    FPS = 15
    fpsClock = pygame.time.Clock()
    catIndex=0
    catx,caty=(0,0)
    cupx,cupy = (100,0)
    
                




















    






    

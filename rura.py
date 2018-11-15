import pygame, sys,os, math, random
from pygame.locals import *
pygame.init()

class pipe:
    """
    Klasa reprezentująca zdjęcie rurki
    """
    def __init__(self ,nazwa):
        """
        konstruktor - metoda wywoływana automatycznie podczas tworzenia obiektów klasy
        """
        #self.obiekt = pygame.image.load("nazwa").convert()
        self.obj = pygame.transform.scale(pygame.image.load(nazwa+".png").convert() , (100,100))
        self.czy = 0
        if nazwa == "r_trzy" :
            #wyjscia (up, right, down, left)
            self.wyjscia = [1,1,0,1]
        elif nazwa == "r_cztery":
            self.wyjscia = [1,1,1,1]
        elif "r_krzywa"==nazwa:
            self.wyjscia=[1,1,0,0]
        elif "r_prosta" == nazwa:
            self.wyjscia=[0,1,0,1]
        elif nazwa == "caly":
            self.wyjscia= [0,0,0,0]
        else:
            raise Exception("błędna nazwa obrazka !")
    
    def rotacja(self):
        self.obj = pygame.transform.rotate(self.obj,270)
        self.wyjscia = [self.wyjscia[-1]]+self.wyjscia[:-1]
        return self


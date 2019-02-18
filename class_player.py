import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):

    def __init__(self, spriteRight, spriteLeft, initial_x, initial_y, screen_size, health, playerName):
        # Définit le sprite du stuff:
        pygame.sprite.Sprite.__init__(self)

        # Sprites allant à droite ou à gauche
        self.spriteRight = spriteRight
        self.spriteLeft = spriteLeft

        # Définit les frames:
        self.totalFrames = len(spriteRight)
        self.frame = -1
        self.displayNumber = 0

        # Définit le sprite initial:
        self.image = self.spriteRight[0]
        self.rect = self.image.get_rect()

        # Définit la position initiale:
        self.rect.x = initial_x
        self.rect.y = initial_y

        # Paramètres de spawn:
        self.standing = False
        self.gravity = 4 # Pas mettre plus que 4 sinon le personnage "saute" sur place
        self.timer = 0

        # Définit la taille de l'écran:
        self.screen_width, self.screen_height = screen_size

        # Attributs du jeu:
        self.originalHealth = health
        self.health = health
        self.name = playerName
        self.movements = 0

    def move(self, direction):
        if self.rect.x > 0 and self.rect.x < 1260:
            if direction == "right" and self.movements < 30:
                self.rect.x += 5
    
                if self.frame in range(1, 4):
                    self.displayNumber = 0
    
                elif self.frame in range(4, 7):
                    self.displayNumber = 1
    
                elif self.frame in range(7, 10):
                    self.displayNumber = 2
    
                elif self.frame in range(10, 13):
                    self.displayNumber = 3
    
                if self.frame > 12:
                    self.frame = -1
    
                self.frame += 1
    
                self.image = self.spriteRight[self.displayNumber]
                
                self.movements += 1
    
            if direction == "left" and self.movements < 30:
                self.rect.x -= 5
    
                if self.frame in range(1, 4):
                    self.displayNumber = 0
    
                elif self.frame in range(4, 7):
                    self.displayNumber = 1
    
                elif self.frame in range(7, 10):
                    self.displayNumber = 2
    
                elif self.frame in range(10, 13):
                    self.displayNumber = 3
    
                if self.frame > 12:
                    self.frame = -1
    
                self.frame += 1
    
                self.image = self.spriteLeft[self.displayNumber]
                
                self.movements += 1
        else:
            if self.rect.x <= 0:
                self.rect.x += 1
            else:
                self.rect.x -= 1

    def gravityFall(self):
        if self.standing == False:
            self.rect.y += self.gravity

    def resetPlayer(self):
        self.health = self.originalHealth
        self.movements = 0

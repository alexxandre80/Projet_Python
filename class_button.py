import pygame
from pygame.locals import *


class Button(pygame.sprite.Sprite):
    def __init__(self, imageFile, screen_size, buttonScale, position):
        # Définit le sprite du stuff:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()

        # Mise à l'échelle du sprite:
        self.new_scale = (round(self.rect.width * buttonScale),
                          round(self.rect.height * buttonScale))
        self.image = pygame.transform.scale(self.image, self.new_scale)
        self.rect = self.image.get_rect()

        # Obtient des dimensions de l'écran:
        screen_width, screen_height = screen_size

        # Vérifie la position pour afficher le bouton:
        if position != "":
            if position == "screen_center":
                # Place le texte au centre de l'écran:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 - self.rect.height/2)
            if position == "center_top":
                # Place le texte au centre de l'écran:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 - self.rect.height)
            if position == "center_top2":
                # Place le texte au centre de l'écran:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 - self.rect.height*2)
            if position == "center_top3":
                # Place le texte au centre de l'écran:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 - self.rect.height*3)
            if position == "center_top4":
                # Place le texte au centre de l'écran:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 - self.rect.height*4)
            if position == "center_top5":
                # Place le texte au centre de l'écran:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 + self.rect.height*5)
            if position == "center_bottom":
                # Place le texte au centre de l'écran:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2)
            if position == "center_bottom2":
                # Place le texte au centre de l'écran:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 + self.rect.height)
            if position == "center_bottom3":
                # Place le texte au centre de l'écran:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 + self.rect.height*2)
            if position == "center_bottom4":
                # Place le texte au centre de l'écran:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 + self.rect.height*3)
            if position == "center_bottom5":
                # Place le texte au centre de l'écran:
                buttonPosition = (screen_width/2 - self.rect.width/2,
                                  screen_height/2 + self.rect.height*4)

        self.buttonPosition = buttonPosition
        self.rect.x, self.rect.y = buttonPosition

    def setPosition(self, position):
        self.rect.x, self.rect.y = position

    def buttonClick(self):
        # Obtient la position de la souris:
        mousePosition = pygame.mouse.get_pos()

        # Vérifie si la souris est dans la zone des boutons:
        if mousePosition[0] >= self.rect.x and mousePosition[0] <= self.rect.x + self.rect.width:
            if mousePosition[1] >= self.rect.y and mousePosition[1] <= self.rect.y + self.rect.height:

                return True

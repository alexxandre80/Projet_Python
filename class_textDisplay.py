import pygame
from pygame.locals import *


class TextDisplay():

    def __init__(self):
        # Initialise le style:
        pygame.font.init()

        # Déclare la police à utiliser par le texte:
        self.font_56 = pygame.font.SysFont("None", 56)
        self.font_46 = pygame.font.SysFont("None", 46)
        self.font_36 = pygame.font.SysFont("None", 36)
        self.font_26 = pygame.font.SysFont("None", 26)
        self.font_16 = pygame.font.SysFont("None", 16)

    def setPosition(self, position, screen_size, text):
        # Obtient les dimensions de l'écran:
        screen_width, screen_height = screen_size

        # Obtient les dimensions du texte:
        text_posX, text_posY, text_lenght, text_height = text.get_rect()

        # Vérifie la position pour afficher le texte:
        if type(position) is str:
            if position != "":
                if position == "screen_center":
                    # Place le texte au centre de l'écran:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 - text_height/2)
                elif position == "center_top":
                    # Place le texte au centre de l'écran:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 - text_height)
                elif position == "center_top2":
                    # Place le texte au centre de l'écran:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 - text_height*2)
                    print("help")
                elif position == "center_top3":
                    # Place le texte au centre de l'écran:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 - text_height*3)
                elif position == "center_bottom":
                    # Place le texte au centre de l'écran:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2)
                elif position == "center_bottom2":
                    # Place le texte au centre de l'écran:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 + text_height*2)
                elif position == "center_bottom3":
                    # Place le texte au centre de l'écran:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 + text_height*3)
                elif position == "center_bottom4":
                    # Place le texte au centre de l'écran:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 + text_height*4)
                elif position == "center_bottom5":
                    # Place le texte au centre de l'écran:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    screen_height/2 + text_height*5)
                elif position == "top_center":
                    # Place le texte centré en haut de l'écran:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    0)
                elif position == "top_center2":
                    # Place le texte centré en haut de l'écran:
                    textPosition = (screen_width/2 - text_lenght/2,
                                    text_height)

        elif type(position) is tuple:
            textPosition = position

        return textPosition

    def displayTextMainMenu(self, text, COLOR, screen, screen_size, position):
        # Ajoute le style au texte:
        text = self.font_56.render(text, True, COLOR)

        # Définit la position du texte:
        textPosition = self.setPosition(position, screen_size, text)

        # Colle le texte à l'écran:
        screen.blit(text, textPosition)

    def displayHealthAndName(self, COLOR, player, screen, screen_size):
        # Obtient les dimensions de l'écran:
        screen_width, screen_height = screen_size

        name = "{0}".format(player.name)
        health = "PV: {0}".format(player.health)

        # Ajoute le style au texte:
        health = self.font_26.render(health, True, COLOR)
        # Obtient les dimensions du texte:
        health_posX, health_posY, health_lenght, health_height = health.get_rect()
        healthPosition = (player.rect.centerx - health_lenght/2,
                          player.rect.centery - health_height*2 - 10)

        # Ajoute le style au texte:
        name = self.font_26.render(name, True, (255, 255, 255))
        # Obtient les dimensions du texte:
        name_posX, name_posY, name_lenght, name_height = name.get_rect()
        namePosition = (player.rect.centerx - name_lenght/2,
                        player.rect.centery - name_height*3 - 10)

        # Ecrit le nom du joueur à l'écran:
        screen.blit(name, namePosition)
        # Ecrit les point de vie à l'écran:
        screen.blit(health, healthPosition)

    def displayTextNameScreen(self, text, COLOR, screen, screen_size, position):
        # Ajoute le style au texte:
        text = self.font_36.render(text, True, COLOR)

        # Définit la position du texte:
        textPosition = self.setPosition(position, screen_size, text)

        # Sticks the text to the screen:
        screen.blit(text, textPosition)

    def displayTextWinnerScreen(self, text, COLOR, screen, screen_size, position):
        # Ajoute le style au texte:
        text = self.font_36.render(text, True, COLOR)

        # Définit la position du texte:
        textPosition = self.setPosition(position, screen_size, text)

        # Colle le texte à l'écran:
        screen.blit(text, textPosition)

    def displayWhoWon(self, COLOR, winner, loser, screen, screen_size, position):
        # Crée la chaîne de caractere:
        text = "{0} a vaincu {1}! Appuyez sur Entrée pour relancer !".format(winner, loser)

        # Ajoute le style au texte:
        text = self.font_36.render(text, True, COLOR)

        # Définit la position du texte:
        textPosition = self.setPosition(position, screen_size, text)

        # Ajoute le texte à l'écran:
        screen.blit(text, textPosition)
        
    def displayDistance(self, COLOR, screen, distance, angle, mouse_position):
        # Crée la chaîne de caractere:
        text = "Distance: {0}".format(distance)
        text2 = "Angle: {0}".format(angle)
        
        # Deplacement du texte avec la souris
        text = self.font_26.render(text, True, COLOR)
        text2 = self.font_26.render(text2, True, COLOR)
        text_2_x = mouse_position[0]
        text_2_y = mouse_position[1] + text2.get_rect()[3]
        text_2_pos = (text_2_x, text_2_y)
        
        # Ajoute le texte à la position:
        screen.blit(text, mouse_position)
        screen.blit(text2, text_2_pos)
        
    def displayMovementsLeft(self, COLOR, screen, movements_left):
        # Crée la chaîne de texte:
        text = "Déplacement: {0}".format(movements_left)
        
        # Ajoute le style au texte:
        text = self.font_26.render(text, True, COLOR)
        
        # Recupere la position:
        textPosition = (0, 0)
        
        # Ajoute le texte à la position:
        screen.blit(text, textPosition)
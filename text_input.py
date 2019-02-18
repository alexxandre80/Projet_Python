import pygame
import string
from pygame.locals import *

ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "


def textInputBox(name, COLOR, screen, screen_size, events, font, max_lenght=15):
    # Obtient la taille de l'écran, afin que
    #nous puissions avoir les dimensions de la fenêtre:
    screen_lenght, screen_height = screen_size

    # Obtenir le nom du joueur:
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return name
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif event.unicode in ACCEPTED:
                if len(name) < max_lenght:
                    name += event.unicode

    # Rendre le nom du joueur et obtenir ses dimensions:
    player_name = font.render(name, True, COLOR)
    name_posX, name_posY, name_lenght, name_height = player_name.get_rect()
    namePosition = (screen_lenght/2 - name_lenght/2,
                    screen_height/2 - name_height)

    # combinées le nom du joueur avec la postion
    screen.blit(player_name, namePosition)

    return name

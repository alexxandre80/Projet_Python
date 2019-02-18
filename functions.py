import pygame
import math
from pygame.locals import *


def get_angle(origin, destination, type):
    if type == "degrés":
        # Trouve l'angle entre deux points:
        x_dist = destination[0] - origin[0]
        y_dist = destination[1] - origin[1]

        angle = math.atan2(-y_dist, x_dist) % (2 * math.pi)

        return math.degrees(angle)
    else:
        # Trouve l'angle entre deux points:
        x_dist = destination[0] - origin[0]
        y_dist = destination[1] - origin[1]

        angle = math.atan2(-y_dist, x_dist) % (2 * math.pi)

        return angle


def get_distance(origin, destination):
    # Vérifie si x2> x1:
    if destination[0] >= origin[0]:
        # Théorème de Pythagore pour trouver 
        # la distance entre deux points:
        x_dist = destination[0] - origin[0]
        y_dist = destination[1] - origin[1]
        distance = ((x_dist)**2 + (y_dist)**2)**(1/2)
        return distance/2

    # Vérifie si x2 <x1:
    elif destination[0] <= origin[0]:
        # Théorème de Pythagore pour trouver 
        # la distance entre deux points:
        x_dist = origin[0] - destination[0]
        y_dist = origin[1] - destination[1]
        distance = ((x_dist)**2 + (y_dist)**2)**(1/2)
        return distance/2


def reset_bomb(group, default_bomb):
    # Définit la "bombe" sur la bombe par défaut:
    bomb = default_bomb
    # Efface le groupe de la bombe:
    group.empty()
    # Ajoute la bombe par défaut au groupe:
    group.add(default_bomb)

    return group, bomb

def getBombStats(bomb, player, mousePosition):
    # Définit la position de départ de la bombe comme centre du joueur:
    bomb.rect.x, bomb.rect.y = player.rect.center
    bomb.startx, bomb.starty = player.rect.center

    # Obtient un angle entre le centre du sprite du joueur et la position de la souris:
    bomb.angle = get_angle(player.rect.center, mousePosition, "degrés")

    # Obtient la distance entre le centre du sprite du joueur et la position de la souris:
    bomb.speed = get_distance(player.rect.center, mousePosition)

    # Vérifie si la vitesse est supérieure 
    # à la limite de vitesse de la bombe:
    if bomb.speed > bomb.maxSpeed:
        bomb.speed = bomb.maxSpeed

    # Définit la bombe comme étant en mouvement:
    bomb.moving = True
import pygame
import math
from pygame.locals import *


class Bomb(pygame.sprite.Sprite):

    def __init__(self, screen_size, imageFile, scale, name, posx, posy, damage, max_speed):
        # Définit les éléments de sprite:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()

        # Mise à l'échelle du sprite:
        self.new_scale = (round(self.rect.width * scale * 1.09),
                          round(self.rect.height * scale * 1.09))
        self.image = pygame.transform.scale(self.image, self.new_scale)
        self.rect = self.image.get_rect()

        # Nom du Projectile:
        self.name = name

        # Taille de l'écran:
        self.screen_w, self.screen_h = screen_size

        # Définit la position initiale:
        self.rect.x = posx
        self.rect.y = posy

        # Définit la vitesse initiale et l'angle, startx et starty:
        self.speed = 0
        self.angle = 0
        self.startx = 0
        self.starty = 0

        # Définit le mouvement:
        self.moving = False

        # Définit le temps:
        self.time = 0

        # Définit les dégâts:
        self.damage = damage

        # Définit la vitesse maximale du projectile
        self.maxSpeed = max_speed

    def move(self):
        # Calcule Vx:
        velocity_x = math.cos(math.radians(self.angle)) * self.speed
        # Calcule Vy
        velocity_y = math.sin(math.radians(self.angle)) * self.speed

        # Calcule la distance totale parcourue sur l'axe X:
        distance_x = velocity_x * self.time
        # Calcule la distance totale parcourue sur l'axe Y:
        distance_y = (velocity_y * self.time) + ((-9.81 * (self.time ** 2)) / 2)

        # Calcule la nouvelle coordonnée sur l’axe X:
        new_x = round(self.startx + distance_x)
        # Calcule la nouvelle coordonnée sur l’axe Y:
        new_y = round(self.starty - distance_y)

        # Ajoute à la durée d'objet:
        self.time += 0.1

        # Vérifie si l'image de l'objet est au-dessus du bas de la fenêtre, le cas échéant:
        if new_y <= self.screen_h - self.rect.height\
                and new_x >= 0\
                and new_x <= self.screen_w - self.rect.width:
            self.rect.x = new_x
            self.rect.y = new_y
        else:
            self.moving = False
            self.time = 0
            self.rotate_angle = 0
            self.rect.y = self.screen_h - self.rect.height

    def stop_movement(self):
        # Arrête le mouvement du sprite et réinitialise ses attributs:
        self.moving = False
        self.time = 0
        self.rotate_angle = 0
        self.rect.y = self.screen_h - self.rect.height

    def reset_stats(self):
        # Arrête le mouvement du sprite et réinitialise ses attributs:
        self.moving = False
        self.time = 0
        self.rotate_angle = 0
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        if self.moving == True:  # Vérifie si la balle est en mouvement, si oui:
            self.move()  # Déplace la balle une fois

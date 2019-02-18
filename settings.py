import pygame
from pygame.locals import *

# Nom de la fenetre:
windowTitle = "Worms Python"

# Parametre de la taille de l'écran:
screen_width, screen_height = 1260, 640
screen_size = (screen_width, screen_height)

# FPS du jeu:
framesPerSecond = 90

# Parametre des couleurs:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (64, 64, 64)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
PINK = (255, 0, 255)
INFINANCE = (172, 58, 56)

# Parametre du joueur:
playerScale = 1
playerTurn = "1"

# Parametre du Terrain:
terrainCollision = True
blockScale = 0.15
terrainPreset = 1
terrainGenRandom = True
minTerrainHeight = 1
maxTerrainHeight = 40
smooth_factor = 5

# Parametre de la bar:
showBombSelector = True

actionBarScale = 1.5
actionBarPosition = "top_center"

iconBombScale = 0.20
iconRoquetteScale = 0.3

# Parametre du jeu:
done = None
winner = None
loser = None

# Parametre des bombes:
lastBombPosition = (0, 0)
bombHit = False

# Parametre de l'explosion:
explosionScale = 1

# Main Screen:
game_screen = "Main Screen"

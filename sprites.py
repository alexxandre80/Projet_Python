import pygame
from settings import *
from pygame.locals import *
import class_bomb as bomb
import class_player as player
import class_button as button
import class_terrain as terrain
import class_actionBar as actionBar
import class_explosion as explosion
import class_background as background
import class_bombDisplay as bombDisplay

# Paramètrage du Background:
background = background.Background("Sprites/BG_StarryNight_1280x640.png", 0, 0)

# Parametre des Joueurs:
player1Right = []
for counter in range(1, 5):
    imagePath = 'Sprites/Player1/Player1_Right.png'
    image = pygame.image.load(imagePath)
    rect = image.get_rect()
    new_scale = (rect.width * playerScale, rect.height * playerScale)

    image = pygame.transform.scale(image, new_scale)
    player1Right.append(image)

player1Left = []
for counter in range(1, 5):
    imagePath = 'Sprites/Player1/Player1_Left.png'
    image = pygame.image.load(imagePath)
    rect = image.get_rect()
    new_scale = (rect.width * playerScale, rect.height * playerScale)

    image = pygame.transform.scale(image, new_scale)
    player1Left.append(image)

player_1 = player.Player(player1Right, player1Left,
                         0, 0,
                         screen_size,
                         100,
                         "Joueur 1")


player2Right = []
for counter in range(1, 5):
    imagePath = 'Sprites/Player2/Player2_Right.png'
    image = pygame.image.load(imagePath)
    rect = image.get_rect()
    new_scale = (rect.width * playerScale, rect.height * playerScale)

    image = pygame.transform.scale(image, new_scale)
    player2Right.append(image)

player2Left = []
for counter in range(1, 5):
    imagePath = 'Sprites/Player2/Player2_Left.png'
    image = pygame.image.load(imagePath)
    rect = image.get_rect()
    new_scale = (rect.width * playerScale, rect.height * playerScale)

    image = pygame.transform.scale(image, new_scale)
    player2Left.append(image)

player_2 = player.Player(player2Right, player2Left,
                         600, 0,
                         screen_size,
                         100,
                         "Joueur 2")

players_group = pygame.sprite.Group()
players_group.add(player_1)
players_group.add(player_2)

# Bar des projectiles:
actionBar = actionBar.ActionBar("Sprites/ActionBar5_210x41.png", screen_size,
                                actionBarScale, actionBarPosition)
actionBar_group = pygame.sprite.Group()
actionBar_group.add(actionBar)

# Bombe 1:
iconRoquette = bombDisplay.BombDisplay("Sprites/roquette.png", iconRoquetteScale)
iconRoquette.rect.center = actionBar.slot1

actionBar_group.add(iconRoquette)

# Bombe 2:
iconBomb = bombDisplay.BombDisplay("Sprites/bomba_crash.png", iconBombScale)
iconBomb.rect.center = actionBar.slot2

actionBar_group.add(iconBomb)

# Terrain:
terrain = terrain.Terrain("Sprites/DirtBlock_70x70.png", blockScale, screen_size, smooth_factor)
if terrainGenRandom == True:
    terrain.generateHeightsRandom(minTerrainHeight, maxTerrainHeight)
else:
    terrain.generateHeightsPreset(terrainPreset)

# Boutons:
button_group = pygame.sprite.Group()

start_button = button.Button("Sprites/Buttons/Start_Button.png", screen_size, 1, "center_top3")
button_group.add(start_button)

exit_button = button.Button("Sprites/Buttons/Exit_Button.png", screen_size, 1, "center_bottom2")
button_group.add(exit_button)

# Paramètrage des projectiles:
roquette = bomb.Bomb(screen_size,
                       "Sprites/roquette.png",
                       0.1,
                       "crash",
                       0, 0,
                       5,
                       200)

bomb_neutron = bomb.Bomb(screen_size,
                         "Sprites/bomba_crash.png",
                         0.06,
                         "neutron",
                         0, 0,
                         25,
                         75)

bomb_group = pygame.sprite.Group()
bomb_group.add(roquette)

# Animation de l'explosion:
explosionFrames = []
for counter in range(1, 14):
    imagePath = 'Sprites/Explosion/Explosion_' + str(counter) + '.png'
    image = pygame.image.load(imagePath)
    rect = image.get_rect()
    new_scale = (rect.width * explosionScale, rect.height * explosionScale)

    image = pygame.transform.scale(image, new_scale)
    explosionFrames.append(image)

explosion = explosion.Explosion(explosionFrames)
explosion_group = pygame.sprite.Group()
explosion_group.add(explosion)

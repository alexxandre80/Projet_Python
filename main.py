import pygame
import text_input as ti
from sprites import *
from settings import *
from functions import *
from pygame.locals import *

import class_textDisplay as textDisplay
text = textDisplay.TextDisplay()

# Importation nécessaire pour centrer la fenêtre de PyGame
import os
# Code pour centrer la fenêtre PyGame sur l'écran
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Initialisation
# ==============================================================================
# Initialisation PyGame:
pygame.init()
pygame.display.set_caption(windowTitle)

# Paramètres de l'écran:
screen = pygame.display.set_mode(screen_size, 0, 32)

# Mise en place des FPS:
clock = pygame.time.Clock()

# Réglage de la marche du joueur:
spriteCount = 0

# Réglages de la bombe:
bomb = roquette

# BOUCLE PRINCIPALE
# ==============================================================================
running = True
while running:

    clock.tick(framesPerSecond)

    # Ecran du menu:
    if game_screen == "Main Screen":
        # Boucle des événements du jeu:
        for event in pygame.event.get():
            # Si l'événement est QUIT fermer la fenêtre 
            if event.type == QUIT:
                # Définit l'état de lecture sur false,
                # quittant ainsi la boucle principale:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.buttonClick():
                    game_screen = "Player 1 Name"

                if exit_button.buttonClick():
                    running = False

        # Dessine le background:
        screen.fill(GRAY)
        button_group.draw(screen)

        text.displayTextMainMenu("Worms Python", WHITE, screen, screen_size, "top_center2")

        # Mises à jour stuff:
        pygame.display.update()

    # Écran du nom du joueur 1:
    elif game_screen == "Player 1 Name":

        # Obtenir des événements du jeux:
        events = pygame.event.get()
        # Boucle à travers les événements du jeux:
        for event in events:
            # Si l'événement est QUIT
            if event.type == QUIT:
                # Définit l'état de lecture sur false, quittant ainsi la boucle principale:
                running = False

            # Vérifie s'il y a eu une pression sur une touche:
            if event.type == pygame.KEYDOWN:
                # Vérifie si la touche appuyée était la touche ENTER:
                if event.key == pygame.K_RETURN:
                    # Ne se lance que si le joueur a appuyer sur la touche:
                    if len(player_1.name) != 0:
                        # Changment d'écran:
                        game_screen = "Player 2 Name"

        # Dessine le background:
        screen.fill(GRAY)

        # Affichage du texte:
        text.displayTextNameScreen("Veuillez saisir le nom du joueur 1 (appuyez sur ENTER lorsque vous êtes prêt):",
                                   WHITE, screen, screen_size, "center_top3")

        # Afficher et obtenir le nom du joueur:
        player_1.name = ti.textInputBox(player_1.name, WHITE,
                                        screen, screen_size, events, text.font_36)

        pygame.display.update()

    # Écran du nom du joueur 2:
    elif game_screen == "Player 2 Name":

        # Obtenir des événements du jeux:
        events = pygame.event.get()
        # Boucle à travers les événements du jeux:
        for event in events:
            # Si l'événement est QUIT
            if event.type == QUIT:
                # Définit l'état de lecture sur false, quittant ainsi la boucle principale:
                running = False

            # Vérifie s'il y a eu une pression sur une touche:
            if event.type == pygame.KEYDOWN:
                # Vérifie si la touche appuyée était la touche ENTER:
                if event.key == pygame.K_RETURN:
                    # Ne se lance que si le joueur a appuyer sur la touche:
                    if len(player_2.name) != 0:
                        # Changment d'écran:
                        game_screen = "Playing"

        # Dessine le background:
        screen.fill(GRAY)

        # Afficher et obtenir le nom du joueur:
        text.displayTextNameScreen("Veuillez saisir le nom du joueur 2 (appuyez sur ENTER lorsque vous êtes prêt):",
                                   WHITE, screen, screen_size, "center_top3")

        # Afficher et obtenir le nom du joueur:
        player_2.name = ti.textInputBox(player_2.name, WHITE,
                                        screen, screen_size, events, text.font_36)

        pygame.display.update()

    # Ecran de jeu:
    elif game_screen == "Playing":

        # Vérification des collisions avec le terrain:
        if terrainCollision == True:
            if pygame.sprite.spritecollide(player_1, terrain.terrain_group, False):
                player_1.rect.y -= 4
                player_1.standing = True

            else:
                player_1.standing = False

            if pygame.sprite.spritecollide(player_2, terrain.terrain_group, False):
                player_2.rect.y -= 4
                player_2.standing = True

            else:
                player_2.standing = False

            if pygame.sprite.spritecollide(bomb, terrain.terrain_group, True):
                bomb.rect.y += 10
                if pygame.sprite.spritecollide(bomb, terrain.terrain_group, True):
                    lastBombPosition = bomb.rect.center
                    bombHit = True
                    bomb.stop_movement()

        # Obtient la position de la souris:
        mousePosition = pygame.mouse.get_pos()

        # Vérification des touches enfoncées:
        pressed_keys = pygame.key.get_pressed()

        # Boucle à travers les événements de jeu
        for event in pygame.event.get():
            # Si l'événement est QUIT 
            if event.type == QUIT:
                # Définit l'état de lecture sur false, quittant ainsi la boucle principale:
                running = False

            # Vérifie s'il y a eu un appui sur le bouton de la souris:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bomb.moving == False:
                    if playerTurn == "1":
                        # Obtient les statistiques de la bombe et la lance:
                        getBombStats(bomb, player_1, mousePosition)
                        done = False

                    elif playerTurn == "2":
                        # Obtient les statistiques de la bombe et la lance:
                        getBombStats(bomb, player_2, mousePosition)
                        done = False

            # Vérifie s'il y a eu une pression sur une touche:
            if event.type == pygame.KEYDOWN:
                # Vérifie si la touche appuyée était le numéro 1:
                if event.key == pygame.K_1:
                    if bomb.moving == False:
                        bomb = roquette
                        bomb_group.empty()
                        bomb_group.add(roquette)

                # Vérifie si la touche appuyée était le numéro 2:
                if event.key == pygame.K_2:
                    if bomb.moving == False:
                        bomb = bomb_neutron
                        bomb_group.empty()
                        bomb_group.add(bomb_neutron)

        # Tour des joueurs:
        if playerTurn == "1":
            # Si la touche appuyée est D:
            if pressed_keys[K_d] and not bomb.moving:
                player_1.move("right")
            # Si la touche appuyée est A:
            if pressed_keys[K_a] and not bomb.moving:
                player_1.move("left")

            # Tracer la ligne entre le joueur et la position de la souris:
            get_distance(player_1.rect.center, mousePosition)
            pygame.draw.line(screen, INFINANCE, player_1.rect.center, mousePosition, 5)

            # Contrôles de collision, s'il y en a,on arrête le mouvement de la bombe et
            # on fait les dégats à l'ennemi:
            if pygame.sprite.collide_rect(bomb, player_2):
                lastBombPosition = bomb.rect.center
                bombHit = True
                bomb.stop_movement()
                player_2.health -= bomb.damage
                # Vérifie s'il y a un gagnant
                if player_2.health <= 0:
                    player_2.health = 0
                    winner = player_1.name
                    loser = player_2.name
                    game_screen = "Winner Screen"

            if done == False:
                if bomb.moving == False:
                    bomb.reset_stats()
                    bomb_group, bomb = reset_bomb(bomb_group, roquette)
                    playerTurn = "2"
                    done = True
                    player_1.movements = 0

        elif playerTurn == "2":
            # Si la touche enfoncée, est flèche vers la droite:
            if pressed_keys[K_RIGHT] and not bomb.moving:
                player_2.move("right")
            # Si la touche enfoncée, est flèche vers la gauche:
            if pressed_keys[K_LEFT] and not bomb.moving:
                player_2.move("left")

            # Tracer la ligne entre le joueur et la position de la souris:
            get_distance(player_1.rect.center, mousePosition)
            pygame.draw.line(screen, INFINANCE, player_2.rect.center, mousePosition, 5)

            # Contrôles de collision, s'il y en a,on arrête le mouvement de la bombe et
            # on fait les dégats à l'ennemi:
            if pygame.sprite.collide_rect(bomb, player_1):
                lastBombPosition = bomb.rect.center
                bombHit = True
                bomb.stop_movement()
                player_1.health -= bomb.damage
                # Vérifie s'il y a un gagnant
                if player_1.health <= 0:
                    player_1.health = 0
                    winner = player_2.name
                    loser = player_1.name
                    game_screen = "Winner Screen"

            if done == False:
                if bomb.moving == False:
                    bomb.reset_stats()
                    bomb_group, bomb = reset_bomb(bomb_group, roquette)
                    playerTurn = "1"
                    done = True
                    player_2.movements = 0

        # Dessine le background:
        screen.blit(background.image, (0, 0))

        # Dessine le terrain:
        terrain.terrain_group.draw(screen)

        # Dessine la bar d'armes:
        actionBar_group.draw(screen)

        # Dessine l'indicateur de sélection de bombe:
        if showBombSelector == True:
            if bomb.name == "crash":
                selectorPos = (round(actionBar.slot1[0]), round(actionBar.slot1[1]))
                selectorRadius = round(actionBar.rect.height/2.5)
                pygame.draw.circle(screen, BLUE, selectorPos, selectorRadius, 2)


            elif bomb.name == "neutron":
                selectorPos = (round(actionBar.slot2[0]), round(actionBar.slot2[1]))
                selectorRadius = round(actionBar.rect.height/2.5)
                pygame.draw.circle(screen, BLUE, selectorPos, selectorRadius, 2)

        # Dessine les joueurs::
        players_group.draw(screen)

        # Dessine la bombe:
        if bomb.moving == True:
            bomb_group.draw(screen)

        # Dessine l'explosion:
        if bombHit == True:
            explosion.animate(lastBombPosition)
            if explosion.displayNumber == 12:
                bombHit = False
        explosion_group.draw(screen)

        # Affichage des noms et des points de vie:
        text.displayHealthAndName(WHITE, player_1, screen, screen_size)
        text.displayHealthAndName(WHITE, player_2, screen, screen_size)

        # Affichage des mouvements à gauche:
        if playerTurn == "1":
            text.displayMovementsLeft(WHITE, screen, 30 - player_1.movements)
        elif playerTurn == "2":
            text.displayMovementsLeft(WHITE, screen, 30 - player_2.movements)

        # Affichage de la vitesse et de l'angle de la bombe:
        if playerTurn == "1":
            speed = round(get_distance(player_1.rect.center, mousePosition), 2)
            if speed > bomb.maxSpeed:
                speed = bomb.maxSpeed
            angle = round(get_angle(player_1.rect.center, mousePosition, "degrees"), 2)
            text.displayDistance(WHITE, screen, speed, angle, mousePosition)
        elif playerTurn == "2":
            speed = round(get_distance(player_2.rect.center, mousePosition), 2)
            if speed > bomb.maxSpeed:
                speed = bomb.maxSpeed
            angle = round(get_angle(player_2.rect.center, mousePosition, "degrees"), 2)
            text.displayDistance(WHITE, screen, speed, angle, mousePosition)

        bomb.update()
        player_1.gravityFall()
        player_2.gravityFall()
        pygame.display.update()

    # Ecran de victoire:
    elif game_screen == "Winner Screen":
        # Boucle à travers les événements de jeu
        for event in pygame.event.get():
                # Si l'événement est QUIT 
            if event.type == QUIT:
                    # Définit l'état de lecture sur false, quittant ainsi la boucle principale:
                running = False

            # Vérifie s'il y a eu une pression sur une touche:
            if event.type == pygame.KEYDOWN:
                # Vérifie si la touche appuyée était la touche ENTER:
                if event.key == pygame.K_RETURN:
                    # Réinitialise les points de vie des joueurs:
                    player_1.resetPlayer()
                    player_2.resetPlayer()

                    # Changement d'écran:
                    game_screen = "Main Screen"

        # Dessine le background:
        screen.fill(GRAY)

        # Affichage du texte:
        text.displayTextWinnerScreen("Toutes nos félicitations!",
                                     WHITE, screen, screen_size, "center_top3")
        # Afficher qui a gagné:
        text.displayWhoWon(GREEN, winner, loser, screen, screen_size,
                           "center_top")
        
        pygame.display.update()


# Quitte le jeu:
pygame.display.quit()

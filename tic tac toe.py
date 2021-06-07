import pygame
from bouton import Bouton, Start, Restart, Quit
from fonctions import GrillePleine, JeuGagne

pygame.init()

#générer la fenetre du jeu et le nom de la fenetre
screen = pygame.display.set_mode((1080,720))
pygame.display.set_caption("jeu")

joueur = False
realiser = True
launched = True
white_color=(255,255,255)
black_color=(0, 0, 0)
green_color=(4, 146,0)
demarre = False
restart = False

a1="-"
a2="-"
a3="-"
b1="-"
b2="-"
b3="-"
c1="-"
c2="-"
c3="-"
grille=False
gagne=False
arial_font = pygame.font.SysFont("arial", 40, True, True)
texte_joueur = arial_font.render("Joueur", True, white_color)
texte_grille = arial_font.render("La grille est pleine, le jeu est fini, bien joué!", True, green_color)
texte_gagne = arial_font.render("Le Joueur    à gagné!", True, green_color)
texte_bienvenue = arial_font.render("Bienvenue dans le jeu du morpion à 2 joueurs!",False, white_color)


#crée un objet type bouton
bouton=Bouton(400,200,60,60)
bouton1=Bouton(400,300,60,60)
bouton2=Bouton(400,400,60,60)

bouton3=Bouton(500, 200, 60, 60)
bouton4=Bouton(500, 300, 60, 60)
bouton5=Bouton(500, 400, 60, 60)

bouton6=Bouton(600, 200, 60, 60)
bouton7=Bouton(600, 300, 60, 60)
bouton8=Bouton(600, 400, 60, 60)

start_button = Start()
quit_button = Quit()
restart_button = Restart()

while launched==True:
    screen.blit(start_button.image, start_button.rect)
    screen.blit(texte_bienvenue, [100,30])

    while demarre==True:

        screen.fill(black_color, pygame.Rect(100, 25, 900, 60))

        screen.blit(bouton.image, bouton.rect)
        screen.blit(bouton1.image, bouton1.rect)
        screen.blit(bouton2.image, bouton2.rect)
        screen.blit(bouton3.image, bouton3.rect)
        screen.blit(bouton4.image, bouton4.rect)
        screen.blit(bouton5.image, bouton5.rect)
        screen.blit(bouton6.image, bouton6.rect)
        screen.blit(bouton7.image, bouton7.rect)
        screen.blit(bouton8.image, bouton8.rect)




        while JeuGagne(a1,a2,a3,b1,b2,b3,c1,c2,c3)==False:

            # appliquer l'image du bouton
            screen.blit(bouton.image, bouton.rect)
            screen.blit(bouton1.image, bouton1.rect)
            screen.blit(bouton2.image, bouton2.rect)

            screen.blit(bouton3.image, bouton3.rect)
            screen.blit(bouton4.image, bouton4.rect)
            screen.blit(bouton5.image, bouton5.rect)

            screen.blit(bouton6.image, bouton6.rect)
            screen.blit(bouton7.image, bouton7.rect)
            screen.blit(bouton8.image, bouton8.rect)

            grille = GrillePleine(a1, a2, a3, b1, b2, b3, c1, c2, c3)

            if grille == True:
                screen.blit(texte_grille, [140, 500])
                screen.blit(quit_button.image, quit_button.rect)
                screen.blit(restart_button.image, restart_button.rect)
                break


            if joueur==True:
                screen.fill(black_color, pygame.Rect(190,100,40,60))
                texte_quel_joueur = arial_font.render("2", True, white_color)
            elif joueur==False:
                screen.fill(black_color, pygame.Rect(190,100,40,60))
                texte_quel_joueur = arial_font.render("1", True, white_color)


            screen.blit(texte_joueur, [50,100])
            screen.blit(texte_quel_joueur, [190, 100])


            # met à jour l'écran
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False
                    pygame.quit()
                    print("fermeture du jeu")
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if bouton.clickable_area.collidepoint(event.pos):
                        realiser = bouton.clique(joueur)
                        if joueur == False and realiser == True:
                            a1 = "X"
                            joueur = True
                        elif joueur == True and realiser == True:
                            a1 = "O"
                            joueur = False

                    if bouton1.clickable_area.collidepoint(event.pos):
                        realiser = bouton1.clique(joueur)
                        if joueur == False and realiser == True:
                            a2 = "X"
                            joueur = True
                        elif joueur == True and realiser == True:
                            a2 = "O"
                            joueur = False

                    if bouton2.clickable_area.collidepoint(event.pos):
                        realiser = bouton2.clique(joueur)
                        if joueur == False and realiser == True:
                            a3 = "X"
                            joueur = True
                        elif joueur == True and realiser == True:
                            a3 = "O"
                            joueur = False

                    if bouton3.clickable_area.collidepoint(event.pos):
                        realiser = bouton3.clique(joueur)
                        if joueur == False and realiser == True:
                            b1 = "X"
                            joueur = True
                        elif joueur == True and realiser == True:
                            b1 = "O"
                            joueur = False

                    if bouton4.clickable_area.collidepoint(event.pos):
                        realiser = bouton4.clique(joueur)
                        if joueur == False and realiser == True:
                            b2 = "X"
                            joueur = True
                        elif joueur == True and realiser == True:
                            b2 = "O"
                            joueur = False

                    if bouton5.clickable_area.collidepoint(event.pos):
                        realiser = bouton5.clique(joueur)
                        if joueur == False and realiser == True:
                            b3 = "X"
                            joueur = True
                        elif joueur == True and realiser == True:
                            b3 = "O"
                            joueur = False

                    if bouton6.clickable_area.collidepoint(event.pos):
                        realiser = bouton6.clique(joueur)
                        if joueur == False and realiser == True:
                            c1 = "X"
                            joueur = True
                        elif joueur == True and realiser == True:
                            c1 = "O"
                            joueur = False

                    if bouton7.clickable_area.collidepoint(event.pos):
                        realiser = bouton7.clique(joueur)
                        if joueur == False and realiser == True:
                            c2 = "X"
                            joueur = True
                        elif joueur == True and realiser == True:
                            c2 = "O"
                            joueur = False

                    if bouton8.clickable_area.collidepoint(event.pos):
                        realiser = bouton8.clique(joueur)
                        if joueur == False and realiser == True:
                            c3 = "X"
                            joueur = True
                        elif joueur == True and realiser == True:
                            c3 = "O"
                            joueur = False


                    elif event.type == pygame.MOUSEMOTION:
                        print(event.pos)


        gagne = JeuGagne(a1, a2, a3, b1, b2, b3, c1, c2, c3)

        if gagne == True:
            screen.blit(texte_gagne, [330, 500])
            screen.blit(texte_joueur, [380, 500])
            screen.blit(quit_button.image, quit_button.rect)
            screen.blit(restart_button.image, restart_button.rect)
            if joueur == True:
                texte_quel_joueur = arial_font.render("1", True, green_color)
            elif joueur == False:
                texte_quel_joueur = arial_font.render("2", True, green_color)
            screen.blit(texte_quel_joueur, [530, 500])




        pygame.display.flip()


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                launched=False
                pygame.quit()
                print("fermeture du jeu")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.clickable_area.collidepoint(event.pos):
                    quit_button.clique()
                if restart_button.clickable_area.collidepoint(event.pos):
                    restart=restart_button.clique()

        while restart==True:
            print("True")
            joueur = False
            realiser = True

            a1 = "-"
            a2 = "-"
            a3 = "-"
            b1 = "-"
            b2 = "-"
            b3 = "-"
            c1 = "-"
            c2 = "-"
            c3 = "-"
            grille = False
            gagne = False
            a=False

            screen.fill(black_color)

            # crée un objet type bouton
            bouton9 = Bouton(400, 200, 60, 60)
            bouton10 = Bouton(400, 300, 60, 60)
            bouton11 = Bouton(400, 400, 60, 60)

            bouton12 = Bouton(500, 200, 60, 60)
            bouton13 = Bouton(500, 300, 60, 60)
            bouton14 = Bouton(500, 400, 60, 60)

            bouton15 = Bouton(600, 200, 60, 60)
            bouton16 = Bouton(600, 300, 60, 60)
            bouton17 = Bouton(600, 400, 60, 60)

            screen.blit(bouton9.image, bouton9.rect)
            screen.blit(bouton10.image, bouton10.rect)
            screen.blit(bouton11.image, bouton11.rect)
            screen.blit(bouton12.image, bouton12.rect)
            screen.blit(bouton13.image, bouton13.rect)
            screen.blit(bouton14.image, bouton14.rect)
            screen.blit(bouton15.image, bouton15.rect)
            screen.blit(bouton16.image, bouton16.rect)
            screen.blit(bouton17.image, bouton17.rect)

            while JeuGagne(a1, a2, a3, b1, b2, b3, c1, c2, c3) == False:

                # appliquer l'image du bouton
                screen.blit(bouton9.image, bouton9.rect)
                screen.blit(bouton10.image, bouton10.rect)
                screen.blit(bouton11.image, bouton11.rect)
                screen.blit(bouton12.image, bouton12.rect)
                screen.blit(bouton13.image, bouton13.rect)
                screen.blit(bouton14.image, bouton14.rect)
                screen.blit(bouton15.image, bouton15.rect)
                screen.blit(bouton16.image, bouton16.rect)
                screen.blit(bouton17.image, bouton17.rect)

                grille = GrillePleine(a1, a2, a3, b1, b2, b3, c1, c2, c3)

                if grille == True:
                    screen.blit(texte_grille, [140, 500])
                    screen.blit(quit_button.image, quit_button.rect)
                    screen.blit(restart_button.image, restart_button.rect)
                    break

                if joueur == True:
                    screen.fill(black_color, pygame.Rect(190, 100, 40, 60))
                    texte_quel_joueur = arial_font.render("2", True, white_color)
                elif joueur == False:
                    screen.fill(black_color, pygame.Rect(190, 100, 40, 60))
                    texte_quel_joueur = arial_font.render("1", True, white_color)

                screen.blit(texte_joueur, [50, 100])
                screen.blit(texte_quel_joueur, [190, 100])

                # met à jour l'écran
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        launched = False
                        pygame.quit()
                        print("fermeture du jeu")
                    elif event.type == pygame.MOUSEBUTTONDOWN:

                        if bouton9.clickable_area.collidepoint(event.pos):
                            realiser = bouton9.clique(joueur)
                            if joueur == False and realiser == True:
                                a1 = "X"
                                joueur = True
                            elif joueur == True and realiser == True:
                                a1 = "O"
                                joueur = False

                        if bouton10.clickable_area.collidepoint(event.pos):
                            realiser = bouton10.clique(joueur)
                            if joueur == False and realiser == True:
                                a2 = "X"
                                joueur = True
                            elif joueur == True and realiser == True:
                                a2 = "O"
                                joueur = False

                        if bouton11.clickable_area.collidepoint(event.pos):
                            realiser = bouton11.clique(joueur)
                            if joueur == False and realiser == True:
                                a3 = "X"
                                joueur = True
                            elif joueur == True and realiser == True:
                                a3 = "O"
                                joueur = False

                        if bouton12.clickable_area.collidepoint(event.pos):
                            realiser = bouton12.clique(joueur)
                            if joueur == False and realiser == True:
                                b1 = "X"
                                joueur = True
                            elif joueur == True and realiser == True:
                                b1 = "O"
                                joueur = False

                        if bouton13.clickable_area.collidepoint(event.pos):
                            realiser = bouton13.clique(joueur)
                            if joueur == False and realiser == True:
                                b2 = "X"
                                joueur = True
                            elif joueur == True and realiser == True:
                                b2 = "O"
                                joueur = False

                        if bouton14.clickable_area.collidepoint(event.pos):
                            realiser = bouton14.clique(joueur)
                            if joueur == False and realiser == True:
                                b3 = "X"
                                joueur = True
                            elif joueur == True and realiser == True:
                                b3 = "O"
                                joueur = False

                        if bouton15.clickable_area.collidepoint(event.pos):
                            realiser = bouton15.clique(joueur)
                            if joueur == False and realiser == True:
                                c1 = "X"
                                joueur = True
                            elif joueur == True and realiser == True:
                                c1 = "O"
                                joueur = False

                        if bouton16.clickable_area.collidepoint(event.pos):
                            realiser = bouton16.clique(joueur)
                            if joueur == False and realiser == True:
                                c2 = "X"
                                joueur = True
                            elif joueur == True and realiser == True:
                                c2 = "O"
                                joueur = False

                        if bouton17.clickable_area.collidepoint(event.pos):
                            realiser = bouton17.clique(joueur)
                            if joueur == False and realiser == True:
                                c3 = "X"
                                joueur = True
                            elif joueur == True and realiser == True:
                                c3 = "O"
                                joueur = False


            screen.blit(bouton9.image, bouton9.rect)
            screen.blit(bouton10.image, bouton10.rect)
            screen.blit(bouton11.image, bouton11.rect)
            screen.blit(bouton12.image, bouton12.rect)
            screen.blit(bouton13.image, bouton13.rect)
            screen.blit(bouton14.image, bouton14.rect)
            screen.blit(bouton15.image, bouton15.rect)
            screen.blit(bouton16.image, bouton16.rect)
            screen.blit(bouton17.image, bouton17.rect)

            gagne = JeuGagne(a1, a2, a3, b1, b2, b3, c1, c2, c3)

            if gagne == True:
                screen.blit(texte_gagne, [330, 500])
                screen.blit(texte_joueur, [380, 500])
                screen.blit(quit_button.image, quit_button.rect)
                screen.blit(restart_button.image, restart_button.rect)
                if joueur == True:
                    texte_quel_joueur = arial_font.render("1", True, green_color)
                elif joueur == False:
                    texte_quel_joueur = arial_font.render("2", True, green_color)
                screen.blit(texte_quel_joueur, [530, 500])

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    launched = False
                    pygame.quit()
                    print("fermeture du jeu")

            while a==False:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        launched = False
                        pygame.quit()
                        print("fermeture du jeu")

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if quit_button.clickable_area.collidepoint(event.pos):
                            quit_button.clique()
                        if restart_button.clickable_area.collidepoint(event.pos):
                            restart = restart_button.clique()
                            a=True



    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            pygame.quit()
            print("fermeture du jeu")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.clickable_area.collidepoint(event.pos) and start_button.start == False:
                demarre = start_button.clique()
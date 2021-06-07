import pygame

class Bouton(pygame.sprite.Sprite):

    def __init__(self, x, y, largeur, longueur):
        super().__init__()
        self.image = pygame.image.load('images/bouton.png')
        self.image = pygame.transform.scale(self.image, (largeur, longueur))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position = (x, y)
        self.clickable_area = pygame.Rect((self.position), (largeur,longueur))
        self.image_change = False

    def clique(self, joueur):
        if joueur == False and self.image_change==False:
            self.image = pygame.image.load('images/boutonJ1.png')
            self.image = pygame.transform.scale(self.image, (60, 60))
            self.image_change=True
            return True


        elif joueur == True and self.image_change==False:
            self.image = pygame.image.load('images/boutonJ2.png')
            self.image = pygame.transform.scale(self.image, (60, 60))
            self.image_change=True
            return True

class Start(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/start.png')
        self.rect = self.image.get_rect()
        self.rect.x = 315
        self.rect.y = 240
        self.clickable_area = pygame.Rect((373,289), (340,210))
        self.start=False

    def clique(self):
        self.image=pygame.image.load('images/black.png')
        self.start=True
        return True

class Restart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/restart.png')
        self.rect = self.image.get_rect()

        self.rect.x = 700
        self.rect.y = 550
        self.clickable_area = pygame.Rect((700,550), (355,155))
        self.restart = False

    def clique(self):
        self.restart = True
        return True


class Quit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/quit.png')
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 550
        self.clickable_area = pygame.Rect((50, 550), (355, 160))

    def clique(self):
        pygame.quit()
import pygame


class Boutons():
    def __init__(self, x, y, image, taille):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * taille), int(height * taille)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def placer(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

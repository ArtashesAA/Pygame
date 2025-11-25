import random
import pygame

size_x = 626
size_y = 832

accidentado_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

class Accidentado(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Cargamos la imagen
        self.image = pygame.image.load("coche-roto.png").convert_alpha()

        # Limita tamaño
        self.image = pygame.transform.scale(self.image, (120, 160))

        # Posicionamiento sprite
        self.rect = self.image.get_rect()

        # Velocidad de bajada
        self.speed_y = 2

    def update(self):
        self.rect.y += self.speed_y

        if self.rect.top > size_y:
            # Obtener el grupo REAL del sprite
            grupo_acc = self.groups()[0]
            self.reset_posicion(grupo_acc)

    def colocado_principal(self, grupo):
        colocado = False
    
        while not colocado:
            self.rect.x = random.randrange(0, size_x - self.rect.width)
            self.rect.y = random.randrange(0, 250)

            # Evitar solapar accidentados
            if not pygame.sprite.spritecollideany(self, grupo):
                colocado = True

    # Regenerar accidentados
    def reset_posicion(self, grupo):
        colocado = False
        while not colocado:
            self.rect.x = random.randrange(0, size_x - self.rect.width)
            self.rect.y = random.randrange(-200, -50)

            # Comprobar colisión con otros del grupo
            if not pygame.sprite.spritecollideany(self, grupo):
                colocado = True

        # Velocidad de bajada
        self.speed_y = 2
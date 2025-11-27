import random
import pygame
import utils

size_x = 626
size_y = 832

accidentado_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

class Accidentado(pygame.sprite.Sprite):
    def __init__(self, grupo_acc, velocidad):
        super().__init__()

        # Cargamos la imagen
        self.image = pygame.image.load(utils.ruta_relativa("img/coche-roto.png")).convert_alpha()

        # Limita tamaño
        self.image = pygame.transform.scale(self.image, (75, 115))

        # Posicionamiento sprite
        self.rect = self.image.get_rect()

        # Velocidad de bajada
        self.speed_y = velocidad

        self.grupo_acc = grupo_acc

        # Máscara para que no tome el cuadrado completo de la imagen coche-roto.png
        self.mask = pygame.mask.from_surface(self.image)

    # Actualizar accidentados
    def update(self):
        self.rect.y += self.speed_y

        # Una vez se salen de pantalla, se borran y se crean nuevos
        if self.rect.top > size_y:
            self.kill()

    # Crear accidentados
    def crearAccidentados(self, grupo):
        colocado = False
        while not colocado:
            self.rect.x = random.randrange(0, size_x - self.rect.width)
            self.rect.y = random.randrange(-200, -50)

            # Comprobar colisión con otros del grupo
            if not pygame.sprite.spritecollideany(self, grupo):
                colocado = True
import pygame

size_x = 626
size_y = 832

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.velocidad_coche = 2.5

        # Cargamos la imagen
        self.image = pygame.image.load("coche.png").convert_alpha()

        # Limita tamaño
        self.image = pygame.transform.scale(self.image, (75, 115))

        # Posicionamiento sprite
        self.rect = self.image.get_rect()

        # Centrar el coche
        self.rect.centerx = size_x // 2
        self.rect.bottom = size_y - 50

        # Velocidad inicial
        self.speed_x = 0

        # Máscara para que no tome el cuadrado completo de la imagen coche.png
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # Aplicar velocidad horizontal
        self.rect.x += self.speed_x

        # Limitar movimiento dentro de la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > size_x:
            self.rect.right = size_x

    # Movimiento de coche jugador
    def movimiento(self, event):
        # Al presionar botón
        if event.type == pygame.KEYDOWN:
            # Presionar izquierda
            if event.key == pygame.K_LEFT:
                self.speed_x = -self.velocidad_coche
             # Presionar derecha
            if event.key == pygame.K_RIGHT:
                self.speed_x = self.velocidad_coche

        # Al levantar botón
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.speed_x = 0
            if event.key == pygame.K_RIGHT:
                self.speed_x = 0

    # Choque entre jugador y coche accidentado
    def choque(self, accidentados):
        return pygame.sprite.spritecollide(self, accidentados, False, pygame.sprite.collide_mask)

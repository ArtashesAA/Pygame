import random
import pygame, sys
import accidentado, jugador

class Juego:
    def __init__(self):
        pygame.init()

        # Tamaño ventana
        size_x = 626
        size_y = 832
        size = (size_x, size_y)

        # Crear ventana
        self.screen = pygame.display.set_mode(size)

        # Reloj / FPS
        self.clock = pygame.time.Clock()

        # Fondo de pantalla
        self.fondo = pygame.image.load("carretera.jpg").convert()

        # Grupos correctos
        self.all_sprite_list = pygame.sprite.Group()
        self.accidentado_list = pygame.sprite.Group()

        # Crear accidentados sin solaparse
        for i in range(4):
            acc = accidentado.Accidentado()

            # Colocado principal
            acc.colocado_principal(self.accidentado_list)

            self.accidentado_list.add(acc)
            self.all_sprite_list.add(acc)

        self.jgd = jugador.Jugador()
        self.all_sprite_list.add(jgd)

        self.done = False

    def run(self):
        while not self.done:
            self.loop()

        pygame.quit()

    def loop(self):
        for event in pygame.event.get():
            # Salir
            if event.type == pygame.QUIT:
                self.done = True

            self.jgd.movimiento(event)

        # Dibujar fondo
        self.screen.blit(self.fondo, [0, 0])

        # Update + dibujar
        self.all_sprite_list.update()
        self.all_sprite_list.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)
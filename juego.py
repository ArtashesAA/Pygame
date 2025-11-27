import pygame
import accidentado, jugador

class Juego:
    def __init__(self):
        pygame.init()

        # Cantidad de accidentados que se generan a la vez
        self.accidentados_generados = 4

        # Tamaño ventana
        size_x = 626
        size_y = 832
        size = (size_x, size_y)

        # Velocidad bajada coches accidentados
        self.velocidad_accidentados = 2

        # Aceleración bajada coches accidentados
        self.aceleracion_accidentados = 0.15

        # Crear ventana
        self.screen = pygame.display.set_mode(size)

        # Reloj / FPS
        self.clock = pygame.time.Clock()

        # Fondo de pantalla
        self.fondo = pygame.image.load("carretera.jpg").convert()

        # Grupos
        self.all_sprite_list = pygame.sprite.Group()
        self.accidentado_list = pygame.sprite.Group()

        # Crear accidentados sin solaparse
        for i in range(self.accidentados_generados):
            acc = accidentado.Accidentado(self.accidentado_list, self.velocidad_accidentados)

            # Colocado principal
            acc.colocado_principal(self.accidentado_list)

            # Sprites
            self.accidentado_list.add(acc)
            self.all_sprite_list.add(acc)

        self.jgd = jugador.Jugador()
        self.all_sprite_list.add(self.jgd)

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

        # Crear nuevos accidentados cuando bajan del todo
        if len(self.accidentado_list) < self.accidentados_generados:
            # Subir velocidad a nuevos accidentados
            self.velocidad_accidentados += self.aceleracion_accidentados
            acc = accidentado.Accidentado(self.accidentado_list, self.velocidad_accidentados)

            # Creación accidentados
            acc.crearAccidentados(self.accidentado_list)
            self.accidentado_list.add(acc)
            self.all_sprite_list.add(acc)

        # Si se produce un choque
        if self.jgd.choque(self.accidentado_list):
            print("💥 CHOQUE!")
            self.done = True 

        self.all_sprite_list.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)
import pygame
import accidentado, jugador

class Juego:
    def __init__(self):
        self.iniciar_juego()

    # Ejecución y salida de juego 
    def run(self):
        while not self.done:
            self.loop()

        pygame.quit()

    def loop(self):
        for event in pygame.event.get():
            # Salir
            if event.type == pygame.QUIT:
                self.done = True

            # Estado normal del juego
            if self.estado == "jugando":
                self.jgd.movimiento(event)

            # Si el jugador se choca, se reiniciar el juego
            if self.estado == "chocado":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:   # Reiniciar al pulsar ESPACIO
                        self.iniciar_juego()

        # Si no se ha chocado
        if self.estado == "jugando":
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
                self.estado = "chocado" 
                return

            # Pintar sprites en pantalla
            self.all_sprite_list.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)
        
        # Si se ha chocado, se puede volver a jugar
        elif self.estado == "chocado":
            self.all_sprite_list.draw(self.screen)

            # Mensaje chocado
            font = pygame.font.SysFont("Arial", 30)
            texto1 = font.render("Has chocado", True, (255, 0, 0))
            texto2 = font.render("Pulsa \"ESPACIO\" para reintentar", True, (255, 255, 255))

            self.screen.blit(texto1, (self.size_x//2 - texto1.get_width()//2, 300))
            self.screen.blit(texto2, (self.size_x//2 - texto2.get_width()//2, 380))

            pygame.display.flip()
            self.clock.tick(60) 

    # Iniciar el juego
    def iniciar_juego(self):
        pygame.init()

        # Estado inicial
        self.estado = "jugando"

        # Cantidad de accidentados que se generan a la vez
        self.accidentados_generados = 4

        # Tamaño ventana
        self.size_x = 626
        self.size_y = 832
        size = (self.size_x, self.size_y)

        # Velocidad bajada coches accidentados
        self.velocidad_accidentados = 2

        # Aceleración bajada coches accidentados
        self.aceleracion_accidentados = 0.15

        # Crear ventana
        self.screen = pygame.display.set_mode(size)

        # Reloj / FPS
        self.clock = pygame.time.Clock()

        # Fondo de pantalla
        self.fondo = pygame.image.load("img/carretera.jpg").convert()

        # Grupos
        self.all_sprite_list = pygame.sprite.Group()
        self.accidentado_list = pygame.sprite.Group()

        # Crear accidentados sin solaparse
        for i in range(self.accidentados_generados):
            acc = accidentado.Accidentado(self.accidentado_list, self.velocidad_accidentados)
            acc.crearAccidentados(self.accidentado_list)

            self.accidentado_list.add(acc)
            self.all_sprite_list.add(acc)

        # Añadir jugador
        self.jgd = jugador.Jugador()
        self.all_sprite_list.add(self.jgd)

        # Control bucle principal
        self.done = False
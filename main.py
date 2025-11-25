import random
import pygame, sys
import accidentado, jugador

pygame.init()

# Tamaño ventana
size_x = 626
size_y = 832
size = (size_x, size_y)

# Crear ventana
screen = pygame.display.set_mode(size)

# Reloj / FPS
clock = pygame.time.Clock()

# Fondo de pantalla
fondo = pygame.image.load("carretera.jpg").convert()

# Grupos correctos
all_sprite_list = pygame.sprite.Group()
accidentado_list = pygame.sprite.Group()

# Crear accidentados sin solaparse
for i in range(4):
    acc = accidentado.Accidentado()

    # Colocado principal
    acc.colocado_principal(accidentado_list)

    accidentado_list.add(acc)
    all_sprite_list.add(acc)

jgd = jugador.Jugador()
all_sprite_list.add(jgd)

done = False

while not done:
    for event in pygame.event.get():
        # Salir del programa
        if event.type == pygame.QUIT:
            done = True

        jgd.movimiento(event)

    screen.blit(fondo, [0,0])

    all_sprite_list.update()
    all_sprite_list.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

    # Reloj
    clock.tick(60)

pygame.quit()
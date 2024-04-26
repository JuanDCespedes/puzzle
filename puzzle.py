import pygame
import sys
import random
from pygame.locals import *
pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Taquin")
num_images = [pygame.image.load(f"imagenes/{i}.png") for i in range(1, 9)]
empty_image = pygame.image.load("imagenes/negro.jpg")
square_size = 200
padding = 10
def shuffle_board():
    global board_state
    while True:
        random.shuffle(board_state)
        inversions = sum(board_state[i] > board_state[j] for i in range(len(board_state)) for j in range(i + 1, len(board_state)) if board_state[i] != 0 and board_state[j] != 0)
        if inversions % 2 == 0:
            break
def is_board_complete():
    return board_state == list(range(1, 9)) + [0]

# Función para dibujar la cuadrícula
def draw_grid():
    for i in range(3):
        for j in range(3):
            num = board_state[i * 3 + j]
            if num != 0:
                screen.blit(num_images[num - 1], (j * (square_size + padding), i * (square_size + padding)))
            else:
                screen.blit(empty_image, (j * (square_size + padding), i * (square_size + padding)))

# Función para intercambiar la posición de dos elementos en el tablero
def swap_positions(pos1, pos2):
    board_state[pos1], board_state[pos2] = board_state[pos2], board_state[pos1]

# Función para manejar los eventos del juego
def handle_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            empty_pos = board_state.index(0)
            if event.key == K_UP and empty_pos + 3 < 9:
                swap_positions(empty_pos, empty_pos + 3)
            elif event.key == K_DOWN and empty_pos - 3 >= 0:
                swap_positions(empty_pos, empty_pos - 3)
            elif event.key == K_LEFT and empty_pos % 3 != 2:
                swap_positions(empty_pos, empty_pos + 1)
            elif event.key == K_RIGHT and empty_pos % 3 != 0:
                swap_positions(empty_pos, empty_pos - 1)

# Función principal
def main():
    global board_state
    while True:
        # Crear un nuevo tablero
        board_state = list(range(1, 9)) + [0]  # Usamos 0 para representar el espacio vacío
        shuffle_board()

        while True:
            handle_events()

            # Limpiar la pantalla
            screen.fill((0, 0, 0))

            # Dibujar la cuadrícula
            draw_grid()

            # Verificar si el tablero está completo
            if is_board_complete():
                font = pygame.font.Font(None, 36)
                text = font.render("¡Completado!", True, (255, 255, 255))
                text_rect = text.get_rect(center=(width // 2, height // 2))
                screen.blit(text, text_rect)

            # Actualizar la pantalla
            pygame.display.flip()

            # Salir del bucle si el tablero está completo
            if is_board_complete():
                pygame.time.delay(2000)  # Esperar 2 segundos
                break

if __name__ == "__main__":
    main()
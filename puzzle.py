import pygame
import sys
import random
from pygame.locals import *
pygame.init()
size = width, height = 600, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Taquin")
num_images = [pygame.image.load(f"imagenes/{i}.png") for i in range(1, 9)]
image = pygame.image.load("imagenes/negro.jpg")
square_size = 200
padding = 10
def board():
    global board_state
    while True:
        random.shuffle(board_state)
        inversions = sum(board_state[i] > board_state[j] for i in range(len(board_state)) for j in range(i + 1, len(board_state)) if board_state[i] != 0 and board_state[j] != 0)
        if inversions % 2 == 0:
            break
def ganar():
    return board_state == list(range(1, 9)) + [0]
def fichas():
    for i in range(3):
        for j in range(3):
            num = board_state[i * 3 + j]
            if num != 0:
                screen.blit(num_images[num - 1], (j * (square_size + padding), i * (square_size + padding)))
            else:
                screen.blit(image, (j * (square_size + padding), i * (square_size + padding)))
def positions(pos1, pos2):
    board_state[pos1], board_state[pos2] = board_state[pos2], board_state[pos1]
def handle_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            empty_pos = board_state.index(0)
            if event.key == K_UP and empty_pos + 3 < 9:
                positions(empty_pos, empty_pos + 3)
            elif event.key == K_DOWN and empty_pos - 3 >= 0:
                positions(empty_pos, empty_pos - 3)
            elif event.key == K_LEFT and empty_pos % 3 != 2:
                positions(empty_pos, empty_pos + 1)
            elif event.key == K_RIGHT and empty_pos % 3 != 0:
                positions(empty_pos, empty_pos - 1)
def main():
    global board_state
    while True:
        board_state = list(range(1, 9)) + [0] 
        board()
        while True:
            handle_events()
            screen.fill((0, 0, 0))
            fichas()
            if ganar():
                font = pygame.font.Font(None, 36)
                text = font.render("¡Completado!", True, (255, 255, 255))
                text_rect = text.get_rect(center=(width // 2, height // 2))
                screen.blit(text, text_rect)
            pygame.display.flip()
            if ganar():
                pygame.time.delay(2000) 
                break
if __name__ == "__main__":
    main()
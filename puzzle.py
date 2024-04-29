import pygame
import sys
import random
from pygame.locals import *

class jueguito:
    def __init__(self):
        self.game = TaquinGame()

    def start(self):
        while True:
            self.game.setup()
            self.run_game()

    def run_game(self):
        while True:
            self.game.jugabilidad()
            self.game.screen.fill((0, 0, 0))
            self.game.draw_tiles()
            if self.game.ganar():
                font = pygame.font.Font(None, 36)
                text = font.render("¡Completado!", True, (255, 255, 255))
                text_rect = text.get_rect(center=(self.game.width // 2, self.game.height // 2))
                self.game.screen.blit(text, text_rect)
            pygame.display.flip()
            if self.game.ganar():
                pygame.time.delay(2000)
                break

class TaquinGame(jueguito):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.size = self.width, self.height = 600, 600
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Taquin")
        self.num_images = [pygame.image.load(f"imagenes/{i}.png") for i in range(1, 9)]
        self.image = pygame.image.load("imagenes/negro.jpg")
        self.square_size = 200
        self.padding = 10
        self.board_state = []

    def setup(self):
        self.board_state = list(range(1, 9)) + [0]
        self.shuffle_board()

    def shuffle_board(self):
        while True:
            random.shuffle(self.board_state)
            inversions = sum(
                self.board_state[i] > self.board_state[j]
                for i in range(len(self.board_state))
                for j in range(i + 1, len(self.board_state))
                if self.board_state[i] != 0 and self.board_state[j] != 0
            )
            if inversions % 2 == 0:
                break

    def ganar(self):
        return self.board_state == list(range(1, 9)) + [0]

    def draw(self):
        for i in range(3):
            for j in range(3):
                num = self.board_state[i * 3 + j]
                if num != 0:
                    self.screen.blit(
                        self.num_images[num - 1],
                        (j * (self.square_size + self.padding), i * (self.square_size + self.padding)),
                    )
                else:
                    self.screen.blit(
                        self.image,
                        (j * (self.square_size + self.padding), i * (self.square_size + self.padding)),
                    )

    def move_tile(self, empty_pos, target_pos):
        self.board_state[empty_pos], self.board_state[target_pos] = self.board_state[target_pos], self.board_state[
            empty_pos]

    def jugabilidad(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                empty_pos = self.board_state.index(0)
                if event.key == K_UP and empty_pos + 3 < 9:
                    self.move_tile(empty_pos, empty_pos + 3)
                elif event.key == K_DOWN and empty_pos - 3 >= 0:
                    self.move_tile(empty_pos, empty_pos - 3)
                elif event.key == K_LEFT and empty_pos % 3 != 2:
                    self.move_tile(empty_pos, empty_pos + 1)
                elif event.key == K_RIGHT and empty_pos % 3 != 0:
                    self.move_tile(empty_pos, empty_pos - 1)

if __name__ == "__main__":
    game_manager = TaquinGame()
    game_manager.start()
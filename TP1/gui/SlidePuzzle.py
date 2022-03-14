import math

import numpy as np
import pygame

from TP1.data_structs.EightState import EightState


class SlidePuzzle:
    def __init__(self, grid_size, tile_size, margin_size, matrix):
        self.grid_size, self.tile_size, self.margin_size = grid_size, tile_size, margin_size
        self.is_thinking = False
        self.tiles_len = grid_size[0] * grid_size[1] - 1
        self.tiles = [(x, y) for y in range(grid_size[1]) for x in range(grid_size[0])]
        self.tile_pos = [(x * (tile_size + margin_size) + margin_size, y * (tile_size + margin_size) + margin_size) for
                         y in range(grid_size[1]) for x in range(grid_size[0])]
        self.font = pygame.font.Font(None, 120)
        self.images = []
        self.repeat = True

        for i in range(self.tiles_len):
            image = pygame.Surface((tile_size, tile_size));
            image.fill((110, 130, 255))
            text = self.font.render(str(i + 1), 2, (0, 0, 0));
            w, h = text.get_size()
            image.blit(text, ((tile_size - w) / 2, (tile_size - h) / 2))
            self.images += [image]
        self.state = EightState(np.matrix(matrix, dtype=int))
        self.saved_state = self.state

    def handle_click(self, pos):
        x_idx = math.floor((pos[0] - self.margin_size) / (self.tile_size + self.margin_size))
        y_idx = math.floor((pos[1] - self.margin_size) / (self.tile_size + self.margin_size))
        if x_idx >= 3 or y_idx >= 3 or x_idx < 0 or y_idx < 0:
            return
        if self.is_clickable(y_idx, x_idx):
            new_coords = (y_idx, x_idx)
            new_board = np.matrix(self.state.board)
            new_board[self.state.blank_cell], new_board[new_coords] = \
                self.state.board[new_coords], self.state.board[self.state.blank_cell]
            self.state = EightState(new_board, new_coords)

    def is_clickable(self, x, y):
        blank_cell = self.state.blank_cell
        return (x + 1, y) == blank_cell or (x - 1, y) == blank_cell or (x, y + 1) == blank_cell or (
            x, y - 1) == blank_cell

    def update(self, dt):
        pass

    def reset_to_save_state(self):
        self.state = self.saved_state

    def save_state(self):
        self.saved_state = self.state

    def draw(self, screen):
        if self.is_thinking:
            text = self.font.render("thinking...", 2, (255, 255, 255));
            screen.blit(text, (100, 100))
        else:
            for i in range(self.tiles_len + 1):
                number = self.state.board[i // 3, i % 3]
                if number > 0:
                    screen.blit(self.images[number - 1], (self.tile_pos[i][0], self.tile_pos[i][1]))
# Simple pygame program

# Import and initialize the pygame library
import math
import os
import sys
import json

import numpy as np
import pygame

from TP1.data_structs.EightState import EightState
from TP1.main import main
from TP1.searchers.informed.ponderated.AStarSearcher import AStarSearcher
from TP1.utils.heuristics import fat_heuristic

class TileNumber:
    def __init__(self, number, tile_pos, image):
        self.number = number
        self.tile_pos = tile_pos
        self.image = image

    def swap_number(self, other_tile):
        self.number = other_tile.number
        self.image = other_tile.image

    def __str__(self) -> str:
        return "TileNumber: " + str(self.number) + ", " + str(self.tile_pos)


class SlidePuzzle:
    def __init__(self, grid_size, tile_size, margin_size):
        self.grid_size, self.tile_size, self.margin_size = grid_size, tile_size, margin_size

        self.tiles_len = grid_size[0]*grid_size[1]-1
        self.tiles = [ (x,y) for y in range(grid_size[1]) for x in range(grid_size[0]) ]

        self.tile_pos = [(x * (tile_size + margin_size) + margin_size, y * (tile_size + margin_size) + margin_size) for y in range(grid_size[1]) for x in range(grid_size[0])]

        self.font = pygame.font.Font(None, 120)

        self.images = []
        for i in range(self.tiles_len):
            image = pygame.Surface((tile_size,tile_size)); image.fill((0,255,0))
            text = self.font.render(str(i+1),2,(0,0,0)); w,h = text.get_size()
            image.blit(text, ((tile_size-w)/2,(tile_size-h)/2))
            self.images += [image]

        self.tiles_class = []

        self.state = EightState(np.matrix([[1,2,0],[4,5,6],[7,8,3]], dtype=int))

    def handle_click(self,pos):
        x_idx = math.floor((pos[0]-self.margin_size)/(self.tile_size+self.margin_size)) % 3
        y_idx = math.floor((pos[1]-self.margin_size)/(self.tile_size+self.margin_size)) % 3
        if self.is_clickable(y_idx,x_idx):
            new_coords = (y_idx,x_idx)
            self.state.board[self.state.blank_cell], self.state.board[new_coords]  =self.state.board[new_coords], self.state.board[self.state.blank_cell]
            self.state.blank_cell = new_coords

    def is_clickable(self,x,y):
        blank_cell = self.state.blank_cell
        return (x+1,y) == blank_cell or (x-1,y) == blank_cell or (x,y+1) == blank_cell or (x,y-1) == blank_cell

    def update(self, dt):
        pass

    def switch(self, tile):
        n = self.tiles.index(tile)
        print(self.tiles)
        print(n)
        self.tiles[n],self.opentile = self.opentile, self.tiles[n]

    def draw(self, screen):
        for i in range(self.tiles_len+1):
            number = self.state.board[i  // 3, i % 3]
            if number > 0:
                pygame.draw.rect(screen, (0, 255, 0), (self.tile_pos[i][0], self.tile_pos[i][1], self.tile_size, self.tile_size))
                screen.blit(self.images[number-1], (self.tile_pos[i][0], self.tile_pos[i][1]))

        # self.switch((0, 0))

def main_gui():
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption('8 Number Puzzel - SIA')
    screen = pygame.display.set_mode((800,600))
    fpaclock = pygame.time.Clock()
    program = SlidePuzzle((3,3), 160, 5)

    #
    # input_file = open('input.json')
    # data = json.load(input_file)
    # matrix_from_json = [data['start_state']['0'], data['start_state']['1'], data['start_state']['2']]
    # # matrix = [[6, 8, 4], [3, 5, 7], [0, 1, 2]]
    # matrix = matrix_from_json
    # if not EightState.is_matrix_solvable(matrix):
    #     print("This matrix does not correspond to a valid state in the game")
    #     return
    # board = EightState(np.matrix(matrix, dtype=int))
    # searcher = AStarSearcher(fat_heuristic)
    # searcher.solve(board)
    #

    # result_path = searcher.analytics.get_path()
    # state_boards_array = []
    # for node in result_path:
    #     state_boards_array.append(node.state.board)
    #
    # for state in state_boards_array:
    #     print(state)

    while True:
        dt = fpaclock.tick()/1000

        screen.fill((0,0,0))
        program.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            program.handle_click(pos)

        program.update(dt)

if __name__ == '__main__':
    main_gui()
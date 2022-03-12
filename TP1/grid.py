# Simple pygame program

# Import and initialize the pygame library
import math
import os
import sys
import json
import time

import numpy as np
import pygame
import pygame_gui

from TP1.data_structs.EightState import EightState
from TP1.main import main
from TP1.utils.heuristics import deep_heuristic, basic_heuristic, fat_heuristic
from TP1.utils.searcher_picker import searcher_picker

heuristics_functions = {'basic': basic_heuristic, 'deep': deep_heuristic, 'fat': fat_heuristic}

SCREEN_SIZE = (800,600)
pygame.init()
BASIC_FONT = pygame.font.Font(None, 120)

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.display.set_caption('8 Number Puzzel - SIA')
screen = pygame.display.set_mode(SCREEN_SIZE)
manager = pygame_gui.UIManager(SCREEN_SIZE)

class SlidePuzzle:
    def __init__(self, grid_size, tile_size, margin_size):
        self.grid_size, self.tile_size, self.margin_size = grid_size, tile_size, margin_size
        self.is_thinking = False
        self.tiles_len = grid_size[0]*grid_size[1]-1
        self.tiles = [ (x,y) for y in range(grid_size[1]) for x in range(grid_size[0]) ]

        self.tile_pos = [(x * (tile_size + margin_size) + margin_size, y * (tile_size + margin_size) + margin_size) for y in range(grid_size[1]) for x in range(grid_size[0])]

        self.font = pygame.font.Font(None, 120)

        self.images = []
        for i in range(self.tiles_len):
            image = pygame.Surface((tile_size,tile_size)); image.fill((110,130,255))
            text = self.font.render(str(i+1),2,(0,0,0)); w,h = text.get_size()
            image.blit(text, ((tile_size-w)/2,(tile_size-h)/2))
            self.images += [image]

        self.tiles_class = []

        self.state = EightState(np.matrix([[7,2,4],[5,0,6],[8,3,1]], dtype=int))

    def handle_click(self,pos):
        x_idx = math.floor((pos[0]-self.margin_size)/(self.tile_size+self.margin_size))
        y_idx = math.floor((pos[1]-self.margin_size)/(self.tile_size+self.margin_size))
        if x_idx >= 3 or y_idx >= 3 or x_idx < 0 or y_idx < 0:
            return
        if self.is_clickable(y_idx,x_idx):
            new_coords = (y_idx,x_idx)
            self.state.board[self.state.blank_cell], self.state.board[new_coords]  =self.state.board[new_coords], self.state.board[self.state.blank_cell]
            self.state.blank_cell = new_coords

    def is_clickable(self,x,y):
        blank_cell = self.state.blank_cell
        return (x+1,y) == blank_cell or (x-1,y) == blank_cell or (x,y+1) == blank_cell or (x,y-1) == blank_cell

    def update(self, dt):
        pass

    def draw(self, screen):
        if self.is_thinking:
            text =self.font.render("thinking...",2,(255,255,255));
            screen.blit(text, (100,100))
        else:
            for i in range(self.tiles_len+1):
                number = self.state.board[i  // 3, i % 3]
                if number > 0:
                    screen.blit(self.images[number-1], (self.tile_pos[i][0], self.tile_pos[i][1]))


### algorithmOptions DropDown
dropdown_layout_rect = pygame.Rect((510, 50), (280, 35))
algorithmOptions = ["BPA", "BPP", "BPPV", "A*", "Heuristica Local"]
algorithmDropDown = pygame_gui.elements.UIDropDownMenu(options_list=algorithmOptions,
                                                       starting_option=algorithmOptions[0],
                                                       relative_rect=dropdown_layout_rect,
                                                       manager=manager)

### Algorithm label
pygame_gui.elements.ui_label.UILabel(parent_element=algorithmDropDown,
                                     manager=manager,
                                     text="Algoritmo:",
                                     relative_rect=pygame.Rect((470, 25), (170, 30)))

### heuristicOptions DropDown
dropdown_layout_rect_heuristic = pygame.Rect((510, 120), (280, 35))
heuristicOptions = ["Basic", "Deep", "Fat"]
heuristicDropDown = pygame_gui.elements.UIDropDownMenu(options_list=heuristicOptions,
                                                       starting_option=heuristicOptions[0],
                                                       relative_rect=dropdown_layout_rect_heuristic,
                                                       manager=manager)

### Algorithm label
pygame_gui.elements.ui_label.UILabel(parent_element=heuristicDropDown,
                                     manager=manager,
                                     text="Heuristica:",
                                     relative_rect=pygame.Rect((470, 95), (170, 30)))

def main_gui():
    algorithm = "BPA"
    heuristic = "Basic"
    fpaclock = pygame.time.Clock()
    program = SlidePuzzle((3,3), 160, 5)

    while True:
        dt = fpaclock.tick()/1000

        screen.fill((0,0,0))
        program.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()

            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == algorithmDropDown:
                    algorithm = event.text

            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == heuristicDropDown:
                    algorithm = event.text

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:

                    if algorithm == "BPA":
                        searcher = searcher_picker('bpa', None)
                    elif algorithm == "BPP":
                        searcher = searcher_picker('bpp', None)
                    elif algorithm == "BPPV":
                        searcher = searcher_picker('bppv', None)
                    elif algorithm == "A*":
                        if heuristic == 'Basic':
                            searcher = searcher_picker('a_star', heuristics_functions['basic'])
                        elif heuristic == 'Deep':
                            searcher = searcher_picker('a_star', heuristics_functions['deep'])
                        elif heuristic == 'Fat':
                            searcher = searcher_picker('a_star', heuristics_functions['fat'])
                    elif algorithm == "Heuristica Local":
                        if heuristic == 'Basic':
                            searcher = searcher_picker('local_heuristic', heuristics_functions['basic'])
                        elif heuristic == 'Deep':
                            searcher = searcher_picker('local_heuristic', heuristics_functions['deep'])
                        elif heuristic == 'Fat':
                            searcher = searcher_picker('local_heuristic', heuristics_functions['fat'])

                    searcher.solve(program.state)
                    result_path = searcher.analytics.get_path()
                    for node in result_path:
                        program.state = node.state
                        screen.fill((0, 0, 0))
                        program.draw(screen)
                        manager.update(dt)
                        manager.draw_ui(screen)
                        program.update(dt)
                        pygame.display.update()
                        time.sleep(0.2)
                        print(node.state)

                    print(searcher.analytics)


            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print(pos)
                program.handle_click(pos)

            manager.process_events(event)

        manager.update(dt)
        manager.draw_ui(screen)
        program.update(dt)
        pygame.display.update()

if __name__ == '__main__':
    main_gui()
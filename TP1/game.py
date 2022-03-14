# Simple pygame program

# Import and initialize the pygame library
import os
import sys
import time

import pygame
import pygame_gui
print(sys.path)

from TP1.gui.SlidePuzzle import SlidePuzzle
from TP1.utils.heuristics import deep_heuristic, basic_heuristic, fat_heuristic
from TP1.utils.json_validator import json_validator, file_validator
from TP1.utils.searcher_picker import searcher_picker

heuristics_functions = {'basic': basic_heuristic, 'deep': deep_heuristic, 'fat': fat_heuristic}
SCREEN_SIZE = (800, 500)
pygame.init()
BASIC_FONT = pygame.font.Font(None, 120)

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.display.set_caption('8 Number Puzzle - SIA')
screen = pygame.display.set_mode(SCREEN_SIZE)
manager = pygame_gui.UIManager(SCREEN_SIZE)

### algorithmOptions DropDown
dropdown_layout_rect = pygame.Rect((510, 50), (280, 35))
algorithmOptions = ["bpa", "bpp", "bppv", "a_star", "local_heuristic", "global_heuristic"]
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
heuristicOptions = ["basic", "deep", "fat"]
heuristicDropDown = pygame_gui.elements.UIDropDownMenu(options_list=heuristicOptions,
                                                       starting_option=heuristicOptions[0],
                                                       relative_rect=dropdown_layout_rect_heuristic,
                                                       manager=manager)

### Algorithm label
pygame_gui.elements.ui_label.UILabel(parent_element=heuristicDropDown,
                                     manager=manager,
                                     text="Heuristica:",
                                     relative_rect=pygame.Rect((470, 95), (170, 30)))

### HotKeys label
hot_keys_text = "Teclas:"
pygame_gui.elements.ui_label.UILabel(manager=manager,
                                     text=hot_keys_text,
                                     relative_rect=pygame.Rect((510, 200), (170, 30)))

### HotKeys label
hot_keys_text = "s: Resolver"
pygame_gui.elements.ui_label.UILabel(manager=manager,
                                     text=hot_keys_text,
                                     relative_rect=pygame.Rect((211, 220), (700, 30)))

### HotKeys label
hot_keys_text = "d: hab/deshab solucion en tablero"
pygame_gui.elements.ui_label.UILabel(manager=manager,
                                     text=hot_keys_text,
                                     relative_rect=pygame.Rect((300, 240), (700, 30)))

### HotKeys label restart
hot_keys_text = "r: Resetear"
pygame_gui.elements.ui_label.UILabel(manager=manager,
                              text=hot_keys_text,
                              relative_rect=pygame.Rect((510, 260), (170, 30)))

### HotKeys label save
hot_keys_text = "g: Guardar"
pygame_gui.elements.ui_label.UILabel(manager=manager,
                              text=hot_keys_text,
                              relative_rect=pygame.Rect((510, 280), (170, 30)))


def refresh_all_gui(program, curr_manager, screen, dt):
    screen.fill((0, 0, 0))
    program.draw(screen)
    program.update(dt)
    curr_manager.update(dt)
    curr_manager.draw_ui(screen)
    pygame.display.update()


def main_gui(matrix=None):
    if len(sys.argv) != 2:
        print("Invalid usage: game.py <config.json>")
        quit(1)

    json_information = file_validator(sys.argv[1])
    matrix = json_information['matrix']
    algorithm = 'bpa'
    heuristic = 'basic'
    fpaclock = pygame.time.Clock()
    program = SlidePuzzle((3, 3), 160, 5, matrix)

    while True:
        dt = fpaclock.tick() / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()

            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == algorithmDropDown:
                    algorithm = event.text
                elif event.ui_element == heuristicDropDown:
                    heuristic = event.text

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    program.last_start_state = program.state
                    searcher = searcher_picker(algorithm, heuristics_functions[heuristic])
                    searcher.solve(program.state)
                    if program.repeat:
                        for node in searcher.analytics.get_path():
                            program.state = node.state
                            refresh_all_gui(program, manager, screen, dt)
                            time.sleep(0.2)
                    analytics = "<p>Algoritmo: {algo}</p><p>Tiempo: {time:.4f}segs</p>"
                    if searcher.analytics.success:
                        analytics = analytics + "<p>Profundidad: {depth}</p><p>Costo: {cost}</p><p>Nodos expandidos: {expanded_count}</p><p>Nodos frontera: {frontier_count}</p>"
                    if algorithm not in ["bpa", "bpp", "bppv"]:
                        analytics = "<p>Heuristica: {heu}</p>" + analytics
                    analytics = "<p>Resultado: {success}</p>" + analytics
                    pygame_gui.windows.ui_confirmation_dialog.UIConfirmationDialog(
                        rect=pygame.Rect((0, 0), (300, 300)),
                        manager=manager,
                        blocking=False,
                        action_long_desc=analytics.format(heu=heuristic,
                                                          algo=algorithm,
                                                          depth=searcher.analytics.end_node and searcher.analytics.end_node.depth,
                                                          cost=searcher.analytics.end_node and searcher.analytics.end_node.cost,
                                                          time=searcher.analytics.time,
                                                          expanded_count=searcher.analytics.expanded_count,
                                                          frontier_count=searcher.analytics.frontier_count,
                                                          success="Exito" if searcher.analytics.success else "No encontrado"),
                        window_title='Analytics',
                    )
                if event.key == pygame.K_d:
                    program.repeat = not program.repeat

                if event.key == pygame.K_r:
                    program.reset_to_save_state()
                    refresh_all_gui(program, manager, screen, dt)
                if event.key == pygame.K_g:
                    program.save_state()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                program.handle_click(pos)

            manager.process_events(event)

        refresh_all_gui(program, manager, screen, dt)


if __name__ == '__main__':
    main_gui()

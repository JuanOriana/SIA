import numpy as np
from TP1.data_structs.Searchable import Searchable

SIDE_SIZE = 3


class EightState(Searchable):
    width, height = SIDE_SIZE, SIDE_SIZE
    blank_cell = (0, 0)

    def __init__(self, board, blank_cell=(0, 0), parent=None):
        (board_w, board_h) = np.shape(board)
        assert board_w == self.width and board_h == self.height
        # Only calculate blank cell if not given or given incorrectly
        if board[blank_cell] != 0:
            print("RECALCULATING!\n")
            coord_x, coord_y = -1, -1
            for x in range(self.width):
                for y in range(self.height):
                    if board[x, y] == 0:
                        coord_x, coord_y = x, y
                        break
                if coord_x != -1:
                    break
            assert coord_x != -1 and coord_y != -1
            blank_cell = (coord_x, coord_y)

        self.board = board
        self.blank_cell = blank_cell
        self.parent = parent

    def possible_moves(self) -> []:
        all_possible_moves = []
        coord_x, coord_y = self.blank_cell
        if coord_x > 0:
            new_board = self.board.copy()
            new_board[coord_x - 1, coord_y], new_board[coord_x, coord_y] = new_board[coord_x, coord_y], new_board[
                coord_x - 1, coord_y]
            all_possible_moves.append(EightState(new_board, (coord_x - 1, coord_y), self))
        if coord_x < self.width - 1:
            new_board = self.board.copy()
            new_board[coord_x + 1, coord_y], new_board[coord_x, coord_y] = new_board[coord_x, coord_y], new_board[
                coord_x + 1, coord_y]
            all_possible_moves.append(EightState(new_board, (coord_x + 1, coord_y), self))
        if coord_y > 0:
            new_board = self.board.copy()
            new_board[coord_x, coord_y - 1], new_board[coord_x, coord_y] = new_board[coord_x, coord_y], new_board[
                coord_x, coord_y - 1]
            all_possible_moves.append(EightState(new_board, (coord_x, coord_y - 1), self))
        if coord_y < self.height - 1:
            new_board = self.board.copy()
            new_board[coord_x, coord_y + 1], new_board[coord_x, coord_y] = new_board[coord_x, coord_y], new_board[
                coord_x, coord_y + 1]
            all_possible_moves.append(EightState(new_board, (coord_x, coord_y + 1), self))

        return all_possible_moves

    def is_solved(self) -> bool:
        to_find = 1
        for x in range(self.width):
            for y in range(self.height):
                if to_find == 9 and self.board[x, y] == 0:
                    return True
                elif self.board[x, y] == to_find:
                    to_find += 1
                else:
                    return False
        return False

    def __str__(self):
        return '\n'.join([str(self.board[0][:3]),
                          str(self.board[1][:3]),
                          str(self.board[2][:3])]).replace('[', '').replace(']', '').replace(',', '').replace('0', 'x') + '\n'

    def __cmp__(self, other):
        return np.array_equal(self.board,other.board)

    def __eq__(self, other):
        return self.__cmp__(other)

    def __ne__(self, other):
        return not self.__cmp__(other)

    def __hash__(self):
        return hash(str(self.board))

import numpy as np
SIDE_SIZE = 3


class EightState:
    width, height = SIDE_SIZE,SIDE_SIZE
    blank_cell = (0,0)

    def __init__(self, board):
        (board_w,board_h) = np.shape(board)
        assert board_w == self.width and board_h == self.height
        self.board = board

        coord_x, coord_y = -1, -1
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y,x] == 0:
                    coord_x, coord_y = x, y
                    break
            if coord_x != -1:
                break

        assert coord_x != -1 and  coord_y != -1
        self.blank_cell = (coord_x,coord_y)

    def possible_moves(self):
        all_possible_moves = []
        coord_x, coord_y = self.blank_cell
        if coord_x > 0:
            new_board = self.board.copy()
            new_board[coord_y,coord_x-1], new_board[coord_y,coord_x] = new_board[coord_y,coord_x], new_board[coord_y,coord_x-1]
            self.blank_cell = (coord_x-1,coord_y)
            all_possible_moves.append(EightState(new_board))
        if coord_x < self.width - 1:
            new_board = self.board.copy()
            new_board[coord_y,coord_x+1], new_board[coord_y,coord_x] = new_board[coord_y,coord_x], new_board[coord_y,coord_x+1]
            self.blank_cell = (coord_x+1,coord_y)
            all_possible_moves.append(EightState(new_board))
        if coord_y > 0:
            new_board = self.board.copy()
            new_board[coord_y-1,coord_x], new_board[coord_y,coord_x] = new_board[coord_y,coord_x], new_board[coord_y-1,coord_x]
            self.blank_cell = (coord_x,coord_y-1)
            all_possible_moves.append(EightState(new_board))
        if coord_y < self.height - 1:
            new_board = self.board.copy()
            new_board[coord_y+1,coord_x], new_board[coord_y,coord_x] = new_board[coord_y,coord_x], new_board[coord_y+1,coord_x]
            self.blank_cell = (coord_x, coord_y + 1)
            all_possible_moves.append(EightState(new_board))

        return all_possible_moves

    def is_winning(self):
        to_find = 1
        for x in range(self.width):
            for y in range(self.height):
                if to_find == 9 and self.board[x][y] == 0:
                    return True
                elif self.board[x][y] == to_find:
                    to_find += 1
                else:
                    return False
        return False

    def __str__(self):
        return '\n'.join([str(self.board[0][:3]),
                          str(self.board[1][:3]),
                          str(self.board[2][:3])]).replace('[', '').replace(']', '').replace(',', '').replace('0', 'x')

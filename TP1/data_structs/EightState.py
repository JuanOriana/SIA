import numpy as np
SIDE_SIZE = 3


class EightState:
    width, height = SIDE_SIZE,SIDE_SIZE

    def __init__(self, board):
        (board_w,board_h) = np.shape(board)
        assert board_w == self.width and board_h == self.height
        self.board = board
    def possible_moves(self):
        all_possible_moves = []
        coordX, coordY = -1, -1
        for x in range(self.width):
            for y in range(self.height):
                if self.board[x][y] == 0:
                    coordX, coordY = x, y
                    break
            if coordX != -1:
                break

        if x > 0:
            new_board = self.board.copy()
            new_board[x - 1][y], new_board[x][y] = new_board[x][y], new_board[x - 1][y]
            all_possible_moves.append(EightState(new_board))
        if x < self.width - 1:
            new_board = self.board.copy()
            new_board[x + 1][y], new_board[x][y] = new_board[x][y], new_board[x + 1][y]
            all_possible_moves.append(EightState(new_board))
        if y > 0:
            new_board = self.board.copy()
            new_board[x][y - 1], new_board[x][y] = new_board[x][y - 1], new_board[x][y]
            all_possible_moves.append(EightState(new_board))
        if y > self.height - 1:
            new_board = self.board.copy()
            new_board[x][y + 1], new_board[x][y] = new_board[x][y + 1], new_board[x][y]
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

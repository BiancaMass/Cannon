# This file handles the game:
# whose turn is it, what piece is selected, what moves are allowed etc...

import pygame

from .board import Board
from .constants import BLACK, RED, BLUE, GRID_SPACING, MARGIN
from .piece import Piece


# from .piece import Piece


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = BLACK
        self.valid_moves = {}  # stores the current valid moves for the selected player
        self.black_cannons = []  # empty list to contain red cannons
        self.red_cannons = []  # empty list to contain red cannons
        self.edibles = []  # stores the edibles items

    def winner(self):
        return self.board.winner()

    # if we want to reset the game
    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:  # if we select something then we actually move it
            result = self._move(row, col)
            if not result:  # otherwise if selection was not successful
                self.selected = None  # set selected to None
                self.select(row, col)  # try to select a different piece

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn and piece.town == False:
            self.selected = piece
            self.valid_moves, self.edibles = self.board.get_valid_moves(piece)
            return True

        return False

    def create_black_town(self, row, col):
        if self.board.black_town < 1:
            valid_pos = self.board.valid_town_pos(BLACK)
            if [row, col] in valid_pos:
                self.board.board[row][col] = Piece(row, col, BLACK)
                piece = self.board.get_piece(row, col)
                piece.make_town()
                self.board.black_town += 1
                return True
        else:
            return False

    def create_red_town(self, row, col):
        if self.board.red_town < 1:
            valid_pos = self.board.valid_town_pos(RED)
            if [row, col] in valid_pos:
                self.board.board[row][col] = Piece(row, col, RED)
                piece = self.board.get_piece(row, col)
                piece.make_town()
                self.board.red_town += 1
                return True
        else:
            return False

    def _move(self, row, col):  # row, col of the destination
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)  # move the selected piece to the row and col that was passed here
            self.change_turn()
        if self.selected and piece != 0 and (row, col) in self.valid_moves and [row, col] in self.edibles:
            pieces = [piece]
            self.board.remove(pieces)  # delete one piece (remove)
            self.board.move(self.selected, row, col)  # move the selected piece to the row and col that was passed here
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:  # looping through the keys of the dictionary
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * GRID_SPACING + MARGIN, row * GRID_SPACING + MARGIN), 10)

    def change_turn(self):
        self.valid_moves = {}
        self.edibles = []
        if self.turn == BLACK:
            self.turn = RED
        else:
            self.turn = BLACK

    def get_board(self):
        """Gets the current board matrix (list of list)"""
        return self.board

    def ai_move(self, board):
        """Change turn after the agent has decided its move and we have updated the board accordingly"""
        self.board = board
        self.change_turn()

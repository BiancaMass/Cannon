# In this file is:
# board set up
# pieces description
# pieces features (moves allowed, deletion,...)

import pygame
from cannon.constants import WHITE, BLACK, GREY, DARK_GREY, RED, BEIGE, ROWS, COLS, GRID_SPACING, HEIGHT, WIDTH, MARGIN, \
    PIECE_RADIUS, PAGODA, MYFONT, LETTERS_TEXT, TEXTRECT_UPPER_LETTERS, TEXTRECT_LOWER_LETTERS
from .piece import Piece


class Board:
    def __init__(self):
        # Create an internal representation of the board. A 2 dimensional list (a sublist for each row,
        # with 10 elements in it). elements can be:
        # 0 = no piece in that position
        # BLACK = black piece in that position
        # RED = red piece in that position e.g.
        # [[BLACK, 0, BLACK...], [RED, 0, RED...]...]
        self.board = []
        self.red_left = self.black_left = 15  # number of pieces (decreases if a piece gets eaten)
        self.red_town = self.black_town = 0  # number of towns
        # self.red_cannons = self.black_cannons = 0  # number of cannons on board
        self.create_pieces()

    # draw the grid lines
    def draw_grid(self, win):
        """ INPUT: window
        OUTPUT: draws a grid on window, and the letter labels"""
        win.fill(BEIGE)  # draw the background in white
        win.blit(LETTERS_TEXT, TEXTRECT_UPPER_LETTERS)
        win.blit(LETTERS_TEXT, TEXTRECT_LOWER_LETTERS)
        for row in range(ROWS):
            pygame.draw.line(win, GREY, (MARGIN, row * GRID_SPACING + MARGIN),
                             (WIDTH - MARGIN, row * GRID_SPACING + MARGIN))
        for col in range(COLS):
            pygame.draw.line(win, GREY, (col * GRID_SPACING + MARGIN, MARGIN),
                             (col * GRID_SPACING + MARGIN, HEIGHT - MARGIN))


    def negamax_evaluate(self, color):
        """Evaluation function for the negamax algorithm
        color: BLACK or RED, who you want the maximizing player to be"""
        # TODO: improve the evaluation function to include things like cannons, moves available... see slides
        tb = self.black_town
        tr = self.red_town
        value = self.black_left - self.red_left + (10 * tb - 10 * tr)
        if color == BLACK:
            return value
        else:
            return -value

    def get_all_pieces(self, color):
        """Gets all pieces that exist on the board, given a color (team)"""
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def move(self, piece, row, col):
        """INPUT: piece to be moved, the row and column we are moving it to"""
        # Swap the objects in the position we are coming from and the position we are moving to.
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_pieces(self):
        """INPUT: self (board).
            Draws the pieces in the starting position."""
        for row in range(ROWS):
            self.board.append([])  # interior list for each row
            for col in range(COLS):
                if col % 2 == 0:
                    if 6 <= row <= 8:
                        self.board[row].append(Piece(row, col, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    if 1 <= row <= 3:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)

    def draw(self, win):
        self.draw_grid(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_piece(win)
                    piece.cannon = False

        cannons = self.scan_for_cannons()
        for cannon in cannons:
            for pc in cannon:
                pc.cannon = True

    def remove(self, pieces):
        """ Remove a piece of the board when captured """
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.town:
                    if piece.color == RED:
                        self.red_town -= 1
                    else:
                        self.black_town -= 1
                else:
                    if piece.color == RED:
                        self.red_left -= 1
                    else:
                        self.black_left -= 1


    def winner(self):
        # TODO: change the winning conditions to include: a player has no moves
        if self.red_left <= 0:
            return BLACK
        elif self.black_left <= 0:
            return RED
        elif self.red_town <= 0:
            return BLACK
        elif self.black_town <= 0:
            return RED

        return None

    def valid_town_pos(self, color):
        """ Defines valid positions for red and black towns. Used during placement."""
        valid_positions = []
        if color == RED:
            rw = 0
            cls = list(range(1, 9))
            for c in cls:
                valid_positions.append([rw, c])
        else:
            rw = 9
            cls = list(range(1, 9))
            for c in cls:
                valid_positions.append([rw, c])

        return valid_positions

    def scan_for_cannons(self):
        """Scans the board looking for cannons.
         INPUT: self (board)
         OUTPUT: list of lists. Each sublist is a cannon.
         Note: currently only works for vertical and horizontal cannons"""
        cannons = []
        # Scan horizontally:
        for row in range(0, ROWS):
            temp_list = []
            for col in range(0, COLS):
                current_piece = self.board[row][col]
                if len(temp_list) == 0:
                    if current_piece != 0:
                        if current_piece.town:
                            temp_list = []
                        else:
                            current_color = current_piece.color
                            temp_list.append(current_piece)
                            previous_color = current_color
                    else:
                        temp_list = []
                else:
                    if current_piece != 0:
                        if current_piece.town:
                            temp_list = []
                        else:
                            current_color = current_piece.color
                            if current_color == previous_color:
                                temp_list.append(current_piece)
                            else:
                                temp_list = [current_piece]
                                previous_color = current_color
                    else:
                        temp_list = []

                if len(temp_list) >= 3:
                    cannons.append(temp_list)

        # Scan vertically
        for col in range(0, COLS):
            temp_list = []
            for row in range(0, ROWS):
                current_piece = self.board[row][col]
                if len(temp_list) == 0:
                    if current_piece != 0:
                        if current_piece.town:
                            temp_list = []
                        else:
                            current_color = current_piece.color
                            temp_list.append(current_piece)
                            previous_color = current_color
                    else:
                        temp_list = []
                else:
                    if current_piece != 0:
                        if current_piece.town:
                            temp_list = []
                        else:
                            current_color = current_piece.color
                            if current_color == previous_color:
                                temp_list.append(current_piece)
                            else:
                                temp_list = [current_piece]
                                previous_color = current_color
                    else:
                        temp_list = []

                if len(temp_list) >= 3:
                    cannons.append(temp_list)

        return cannons

    def get_valid_moves(self, piece):
        moves = {}  # store the dest. as the key and the start as the corresponding element e.g. (4,5): [(3,4)]
        edible = []
        row = piece.row
        col = piece.col

        if piece.town:
            pass  # no valid moves
        else:
            output = self._move_capture(row, col, piece.color, edible)
            moves.update(output[0])
            edible = output[1]
            moves.update(self._move_retreat(row, col, piece.color))

        return moves, edible

    def _move_capture(self, start_row, start_col, color, edible):  # edibles: empty list to be filled
        moves = {}
        edible = []
        left_col = start_col - 1
        right_col = start_col + 1

        if color == RED:
            rows_of_moves = [start_row, start_row + 1]  # downwards direction
        else:
            rows_of_moves = [start_row, start_row - 1]  # upwards direction

        for r in rows_of_moves:
            # same row as selected object, can only capture
            if r == rows_of_moves[0]:
                if left_col < 0:
                    pass
                else:
                    left_same = self.board[r][left_col]  # left of the piece (same row difference)
                    if left_same != 0:  # capture
                        if (self.board[r][left_col]).color != color:
                            moves[(r, left_col)] = [[start_row, start_col]]
                            edible.append([r, left_col])

                if right_col > 9:
                    pass
                else:
                    right_same = self.board[r][right_col]  # left of the piece (same row difference)
                    if right_same != 0:  # capture
                        if (self.board[r][right_col]).color != color:
                            moves[(r, right_col)] = [[start_row, start_col]]
                            edible.append([r, right_col])
            # row above (black) / below (red) selected object, can move or capture
            if r == rows_of_moves[1]:  # one step ahead of the staring row (up for black, down for red)
                if 0 <= r <= 9:
                    diff = self.board[r][start_col]  # straight up or down the piece
                    # move up:
                    if diff == 0:
                        moves[(r, start_col)] = [[start_row, start_col]]
                    else:
                        if (self.board[r][start_col]).color != color:
                            moves[(r, start_col)] = [[start_row, start_col]]
                            edible.append([r, start_col])

                    # move left
                    if left_col < 0:
                        pass
                    else:
                        left_diff = self.board[r][left_col]  # left of the piece (one row difference)
                        if left_diff == 0:  # move
                            moves[(r, left_col)] = [[start_row, start_col]]
                        else:  # capture
                            if (self.board[r][left_col]).color != color:
                                moves[(r, left_col)] = [[start_row, start_col]]
                                edible.append([r, left_col])

                    # move right
                    if right_col > 9:
                        pass
                    else:
                        right_diff = self.board[r][right_col]  # right of the piece (one row difference)
                        if right_diff == 0:
                            moves[(r, right_col)] = [[start_row, start_col]]
                        else:  # capture
                            if (self.board[r][right_col]).color != color:
                                moves[(r, right_col)] = [[start_row, start_col]]
                                edible.append([r, right_col])

        return moves, edible

    def _move_retreat(self, start_row, start_col, color):
        moves = {}
        col_l = start_col - 1
        col_ll = start_col - 2
        col_r = start_col + 1
        col_rr = start_col + 2
        if color == RED:
            row_of_clearance = start_row - 1  # upwards direction
            row_of_retreat = start_row - 2
        else:
            row_of_clearance = start_row + 1  # downwards direction
            row_of_retreat = start_row + 2

        # check for adjacency:
        adjacent_positions = []  # a list that will store all the objects that are adjacent to our object
        adjacent_rows = list(range((start_row - 1), (start_row + 2)))
        adjacent_cols = list(range((start_col - 1), (start_col + 2)))
        for r in adjacent_rows:
            for c in adjacent_cols:
                if r == start_row and c == start_col:  # do not consider the starting position
                    pass
                elif r < 0 or r > 9:
                    pass
                elif c < 0 or c > 9:
                    pass
                else:
                    adjacent_positions.append([r, c])

        for neighbor in adjacent_positions:
            # check if a neighbor is an enemy:
            piece = self.get_piece(neighbor[0], neighbor[1])
            if piece != 0:
                if piece.town:  # you don't retreat if you're adjacent to a town
                    pass
                else:
                    if self.board[neighbor[0]][neighbor[1]] != 0 and self.board[neighbor[0]][
                        neighbor[1]].color != color:
                        if 0 < row_of_retreat < 9:
                            # retreat to the left:
                            if col_ll > 0:
                                diff_left = self.board[row_of_clearance][
                                    col_l]  # left of the piece (one row difference)
                                diff_diff_left = self.board[row_of_retreat][col_ll]
                                if diff_left == 0 and diff_diff_left == 0:  # clear trajectory
                                    moves[(row_of_retreat, col_ll)] = [[start_row, start_col]]

                            # retreat to the right
                            if col_rr < 9:
                                diff_right = self.board[row_of_clearance][col_r]
                                diff_diff_right = self.board[row_of_retreat][col_rr]
                                if diff_right == 0 and diff_diff_right == 0:
                                    moves[(row_of_retreat, col_rr)] = [[start_row, start_col]]

                            # retreat backwards
                            diff_straight = self.board[row_of_clearance][start_col]
                            diff_diff_straight = self.board[row_of_retreat][start_col]
                            if diff_straight == 0 and diff_diff_straight == 0:
                                moves[(row_of_retreat, start_col)] = [[start_row, start_col]]

                            break

        return moves

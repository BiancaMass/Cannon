from .constants import BLACK, RED, DARK_GREY, GRID_SPACING, PIECE_RADIUS, MARGIN, PAGODA, CANNON
import pygame


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.town = False
        self.cannon = False
        self.x = 0  # initiate
        self.y = 0  # initiate
        self.calc_pos()

    # calculate our position based on the position on grid
    def calc_pos(self):
        self.x = GRID_SPACING * self.col + MARGIN
        self.y = GRID_SPACING * self.row + MARGIN

    # create a function for the town
    def make_town(self):
        self.town = True

    def make_cannon(self):
        self.cannon = True

    # draw circle pieces
    def draw_piece(self, win):
        pygame.draw.circle(win, DARK_GREY, (self.x, self.y), PIECE_RADIUS + 2)
        pygame.draw.circle(win, self.color, (self.x, self.y), PIECE_RADIUS)
        if self.town:
            # blit = put image on screen
            win.blit(PAGODA, (self.x - PAGODA.get_width() // 2, self.y - PAGODA.get_height() // 2))

        if self.cannon:
            win.blit(CANNON, (self.x - CANNON.get_width() // 2, self.y - CANNON.get_height() // 2))

    def move(self, row, col):
        self.row = row  # self.row becomes the new (input) col
        self.col = col  # self.col becomes the new (input) col
        self.calc_pos()  # recalculate the position after the move

    # for debugging: returns internal representation of object
    def __repr__(self):
        return str(self.color)

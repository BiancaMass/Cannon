# Bianca Massacci - i6261625
# Maastricht University
# Department of Data Science and Knowledge Engineering

# SOURCES
# "Python/Pygame Checkers Tutorial" by Tech With Tim (Tim Ruscica).
# https://www.youtube.com/watch?v=vnd3RfeG3NM
# https://www.youtube.com/watch?v=LSYj8GZMjWY
# https://www.youtube.com/watch?v=_kOXGzkbnps
# And Python Checkers AI Tutorial Part 2 - Implementation & Visualization (Minimax):
# https://www.youtube.com/watch?v=mYbrH1Cl3nw
# https://github.com/techwithtim/Python-Checkers-AI (GitHub)


import pygame
from cannon.constants import WIDTH, HEIGHT, GRID_SPACING, MARGIN, BLACK, GREY, BEIGE, COLS, RED
# from cannon.board import Board
from cannon.game import Game
from minimax.algorithm import negamax

FPS = 60
# Create a window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.font.init()
# Create a caption
pygame.display.set_caption("Bianca - Cannon - Minimax")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // GRID_SPACING
    col = x // GRID_SPACING
    return row, col


# The function that will start_row the game
def main():
    run = True
    black_town_placed = False
    red_town_placed = False
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if black_town_placed and red_town_placed:
            if game.winner() != None:
                print("The winner is:", game.winner())
                run = False

        # Negamax for black player. Uncomment the next 3 lines if you want the Ai to play black.
        if game.turn == BLACK and black_town_placed and red_town_placed:
            value, new_board = negamax(game.get_board(), 2, BLACK, game)
            game.ai_move(new_board)

        # Negamax for red player. Uncomment the next 3 lines if you want the Ai to play red.
        # if game.turn == RED and black_town_placed and red_town_placed:
        #     value, new_board = negamax(game.get_board(), 2, RED, game)
        #     game.ai_move(new_board)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and not black_town_placed:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                black_town_placed = game.create_black_town(row, col)

            elif event.type == pygame.MOUSEBUTTONDOWN and not red_town_placed:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                red_town_placed = game.create_red_town(row, col)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


# Call the function
main()

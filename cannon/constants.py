import pygame

WIDTH, HEIGHT = 500, 500
ROWS, COLS = 10, 10
GRID_SPACING = WIDTH // COLS
MARGIN = GRID_SPACING // 2

# colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
BROWN = (165, 42, 42)
DARK_GREY = (60, 60, 60)
BEIGE = (227, 197, 175)

# fonts
pygame.font.init()
size = 12
MYFONT = pygame.font.Font("assets/Arial.ttf", size)
LETTERS_TEXT = MYFONT.render('A            B              C              D              E              F'
                             '              G              H              I              J', True, BLACK, BEIGE)
TEXTRECT_UPPER_LETTERS = LETTERS_TEXT.get_rect()
TEXTRECT_UPPER_LETTERS.center = (WIDTH // 2, 10)

TEXTRECT_LOWER_LETTERS = LETTERS_TEXT.get_rect()
TEXTRECT_LOWER_LETTERS.center = (WIDTH // 2, HEIGHT - 10)


# piece features
PADDING = 10
PIECE_RADIUS = (GRID_SPACING - PADDING*2) // 2
PAGODA = pygame.transform.scale(pygame.image.load('assets/pagoda.png'), (20, 20))
CANNON = pygame.transform.scale(pygame.image.load('assets/cannon.png'), (20, 20))
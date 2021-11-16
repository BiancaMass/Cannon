from copy import deepcopy
# Deepcopy is used to make a copy of an object with the goal
# of being able to modify the copied object without affecting the original
# Useful when evaluating each branching node (each is a different board, a copied version
# of the parent node with one edit made to it).
from cannon.constants import RED, BLACK


def negamax(position, depth, player, game):
    """
    Runs the negamax algorithm
    INPUTS:
    position: current board (containing pieces positions)
    depth = desired search depth
    player: BLACK or RED
    game: current game Class (from game.py).
    """

    if depth == 0 or position.winner() != None:
        return position.negamax_evaluate(player), position

    max_eval = float('-inf')
    if player == BLACK:
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = -negamax(move, depth - 1, RED, game)[0]
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move

        return max_eval, best_move

    if player == RED:
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = -negamax(move, depth - 1, BLACK, game)[0]
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move

        return max_eval, best_move


def simulate_move(piece, move, board, eaten):
    if eaten:
        board.remove(eaten)
    board.move(piece, move[0], move[1])

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves, edible = board.get_valid_moves(piece)
        for move in valid_moves:
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            if temp_piece != 0:
                # move = (row, col)
                if [move[0], move[1]] in edible:
                    eaten = temp_board.get_piece(move[0], move[1])
                    new_board = simulate_move(temp_piece, move, temp_board, [eaten])
                    moves.append(new_board)
                else:
                    new_board = simulate_move(temp_piece, move, temp_board, False)
                    moves.append(new_board)

    return moves

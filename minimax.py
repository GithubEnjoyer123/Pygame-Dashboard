from copy import deepcopy
import pygame

X = 'x_clicked'
O = 'o_clicked'

def minimax(position, depth, isMaximizing, game):
  if depth == 0 or checkWin(position) != None:
    return position.evaluate(), position


def guess_move(piece, move, board, game, skip):
  board.move(piece, move[0], move[1] )
  if skip:
    board.remove(skip)
    return board


def get_possible_move(board, piece, game):
  moves = []
  for piece in board.get_all_pieces(piece):
    validmoves = board.get_valid_moves(piece)
    for move, skip in validmoves.items():
      old_board = deepcopy(board)
      old_piece = old_board.get_piece(piece.row, piece.col)
      new_board = guess_move(old_piece, move, old_board, game, skip)
      moves.append(new_board)
      
      
  return moves



if isMaximizing:
  max_evaluate = float('-inf')
  best_move = None
    for move in get_possible_moves(position, X, game):
      evaluate = minimax(move, depth - 1, False, game)[0]
      max_eval = max(max_eval, evaluate)
      if max_eval == evaluate:
        best_move = move
    return max_eval, best_move
    
else:
    min_evaluate = float('inf')
    best_move = None
    for move in get_possible_moves(position, O, game):
      evaluate = minimax(move, depth - 1, True, game)[0]
      min_eval = min(min_eval, evaluate)
      if min_eval == evaluate:
        best_move = move
    return min_eval, best_move






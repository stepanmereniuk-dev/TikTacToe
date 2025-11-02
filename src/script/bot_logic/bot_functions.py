import random
from ..matrix_operation.matrix_operation import check_diagonals,check_rows_and_columns

matrix_board = [["-","-","-"],
                ["-","-","-"],
                ["-","-","-"]]

def try_to_win(board, sign):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = sign
                if check_diagonals(board) or check_rows_and_columns(board):
                    return True
                board[i][j] = "-"
    return False

def try_to_prevent(board, opponent_sign):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                board[i][j] = opponent_sign
                if check_diagonals(board) or check_rows_and_columns(board):
                    board[i][j] = "X" if opponent_sign == "O" else "O"
                    return True
                board[i][j] = "-"
    return False

def ia(board, sign):
    opponent_sign = "O" if sign == "X" else "X"

    if try_to_win(board, sign):
        return True

    if try_to_prevent(board, opponent_sign):
        return True

    empty_spots = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
                empty_spots.append((i, j))

    if empty_spots:
        spot = random.choice(empty_spots)
        board[spot[0]][spot[1]] = sign
        return True

    return False
#TEST
#matrix_board = [["-","-","-"],
#               ["-","x","-"],
#               ["-","-","-"]]
#print(ia(matrix_board,"O"))
#TEST 2
#matrix_board = [["-","-","-"],
#               ["-","x","-"],
#               ["-","-","-"]]
#print(ia(matrix_board,"O"))
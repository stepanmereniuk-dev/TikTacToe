import sys 
import os
from script.matrix_operation.matrix_operation import check_diagonals,check_rows_and_columns

i = 2
player = False
win = False
matrix_board = [["-","-","-"],
                ["-","-","-"],
                ["-","-","-"]]

def make_turn(player,board):
    coordinate1 = int(input("Plz write first coordinate: (_,y):")) 
    coordinate2 = int(input("Plz write second coordinate: (x,_):"))
    if board[coordinate1][coordinate2]=="-":
        if player:
            board[coordinate1][coordinate2] = "x"
            if check_rows_and_columns(board) or check_diagonals(board):
                print("Player 1 win")
                return True
        else:
            board[coordinate1][coordinate2] = "O"
            if check_rows_and_columns(board) or check_diagonals(board):
                print("Player 2 win")
                return True
    else:
        print("Wrong coordinate or already filed by another player")

def print_board(matrix):
    for i in matrix:
        print(i,"\n")

while True:
    if i % 2 == 0:
        print("--------X player start X------")
        print_board(matrix_board)
        player = True
    else:
        print("--------O player start O------")
        player = False
        print_board(matrix_board)
    win = make_turn(player,matrix_board)
    print_board(matrix_board)
    if win == True:
        break
    i += 1
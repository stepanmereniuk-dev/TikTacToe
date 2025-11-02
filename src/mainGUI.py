
import pygame
import sys
import time
import random

from script import Button, TextLabel
from script.matrix_operation.matrix_operation import check_diagonals, check_rows_and_columns
from script.bot_logic.bot_functions import ia

pygame.init()
screenProperty = (1200, 680)
screen = pygame.display.set_mode(screenProperty)

matrix_board = [["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]]

all_button = []
all_labels = []
tile_button = []
pre_build_completed = False
turn_of_player_1 = True
game_over = False
win_time = 0
mode = None

def save_and_verify():
    pass

def set_mode(value):
    global mode
    mode = value
    text_label.set_text(value)

def pre_build():
    global text_label
    text_label = TextLabel("Unknown choice", 250, 50, (500, 20))
    all_labels.append(text_label)

    button_pvp = Button("Player vs Player", 240, 40, (900, 200), passed_value="Player vs Player", callback_func=set_mode)
    all_button.append(button_pvp)

    button_pvai = Button("Player vs AI", 240, 40, (900, 250), passed_value="Player vs AI", callback_func=set_mode)
    all_button.append(button_pvai)

def desk_build():
    for i in range(3):
        for b in range(3):
            x = 100 + (100 * b + 100)
            y = 100 + (100 * i + 100)
            button = Button(" - ", 100, 100, (x, y), passed_value="-")
            tile_button.append(button)

def update_tiles_from_board():
    for idx, btn in enumerate(tile_button):
        i = idx // 3
        j = idx % 3
        mark = matrix_board[i][j]
        new_text = " " + mark + " " if mark != "-" else " - "
        btn.set_text(new_text)

def is_board_full():
    return all(matrix_board[i][j] != "-" for i in range(3) for j in range(3))

def check_for_win_or_tie(mark):
    global game_over, win_time
    if check_diagonals(matrix_board) or check_rows_and_columns(matrix_board):
        if not game_over:
            game_over = True
            win_player = mark
            win_time = time.time()
            text_win = TextLabel(f"Player {win_player} wins!", 300, 50, (450, 300))
            all_labels.append(text_win)
            return True
    elif is_board_full():
        if not game_over:
            game_over = True
            win_time = time.time()
            text_tie = TextLabel("It's a tie!", 300, 50, (450, 300))
            all_labels.append(text_tie)
            return True
    return False

pre_build()
desk_build()
while True:
    screen.fill((230, 230, 230))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        for but in all_button:
            but._check_click(event)

        if mode is not None:
            for btn in tile_button:
                if btn._check_click(event):
                    if not game_over and btn.text == " - ":
                        mark = "X" if turn_of_player_1 else "O"
                        if mode == "Player vs AI" and not turn_of_player_1:
                            continue
                        btn.set_text(" " + mark + " ")

                        idx = tile_button.index(btn)
                        i = idx // 3
                        j = idx % 3
                        matrix_board[i][j] = mark

                        check_for_win_or_tie(mark)

                        turn_of_player_1 = not turn_of_player_1

    if mode == "Player vs AI" and not turn_of_player_1 and not game_over:
        time.sleep(0.5)
        ai_moved = ia(matrix_board, "O")
        if ai_moved:
            update_tiles_from_board()
            check_for_win_or_tie("O")
            turn_of_player_1 = not turn_of_player_1

    for but in all_button + tile_button:
        but._check_hover(screen)

    for lb in all_labels:
        lb._draw(screen)

    if game_over and time.time() - win_time > 3:
        for i in range(3):
            for j in range(3):
                matrix_board[i][j] = "-"
        for btn in tile_button:
            btn.set_text(" - ")
        turn_of_player_1 = True
        game_over = False
        all_labels.pop()

    pygame.display.flip()
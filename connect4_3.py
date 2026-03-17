import turtle
import time
import random


ROW_COUNT = 6
COLUMN_COUNT = 7

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 650
SQUARE_SIZE = 100
DISC_RADIUS = 40


screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Connect4")
screen.tracer(0)

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.speed(0)

message_turtle = turtle.Turtle()
message_turtle.hideturtle()
message_turtle.penup()
message_turtle.goto(0, 350)

def create_board():
    return [[EMPTY for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == EMPTY


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == EMPTY:
            return r
    return -1


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


def draw_board_turtle(board):
    drawer.clear()
    start_x = -SCREEN_WIDTH / 2 + 50
    start_y = -SCREEN_HEIGHT / 2 + 50
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            drawer.color("green");
            drawer.penup()
            drawer.goto(start_x + c * SQUARE_SIZE, start_y + r * SQUARE_SIZE)
            drawer.pendown();
            drawer.begin_fill()
            for _ in range(4):
                drawer.forward(SQUARE_SIZE);
                drawer.left(90)
            drawer.end_fill()

            center_x = start_x + c * SQUARE_SIZE + SQUARE_SIZE / 2
            center_y = start_y + r * SQUARE_SIZE + DISC_RADIUS

            color = "red" if board[r][c] == PLAYER_PIECE else ("yellow" if board[r][c] == AI_PIECE else "white")

            drawer.penup()
            drawer.goto(center_x, center_y - DISC_RADIUS)
            drawer.fillcolor(color)
            drawer.pendown();
            drawer.begin_fill()
            drawer.circle(DISC_RADIUS);
            drawer.end_fill()
    screen.update()


def check_winning_move(board, piece):
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if all(board[r][c + i] == piece for i in range(4)): return True
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if all(board[r + i][c] == piece for i in range(4)): return True
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if all(board[r + i][c + i] == piece for i in range(4)): return True
            if all(board[r + 3 - i][c + i] == piece for i in range(4)): return True
    return False


def get_simple_ai_move(board):

    valid_locations = get_valid_locations(board)

    for col in valid_locations:
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, AI_PIECE)

        if check_winning_move(board, AI_PIECE):
            drop_piece(board, row, col, EMPTY)
            return col

        drop_piece(board, row, col, EMPTY)

    for col in valid_locations:
        row = get_next_open_row(board, col)
        drop_piece(board, row, col, PLAYER_PIECE)

        if check_winning_move(board, PLAYER_PIECE):
            drop_piece(board, row, col, EMPTY)
            return col

        drop_piece(board, row, col, EMPTY)

    center_cols = [3, 2, 4, 1, 5, 0, 6]
    for col in center_cols:
        if col in valid_locations:
            return col

    return random.choice(valid_locations)



current_board = create_board()
game_over = False
current_turn = 0


def handle_click(x, y):
    global current_turn, game_over, current_board

    if game_over or current_turn != 0:
        return

    start_x = -SCREEN_WIDTH / 2 + 50
    col = int((x - start_x) // SQUARE_SIZE)

    if 0 <= col < COLUMN_COUNT and is_valid_location(current_board, col):
        row = get_next_open_row(current_board, col)
        drop_piece(current_board, row, col, PLAYER_PIECE)

        draw_board_turtle(current_board)

        if check_winning_move(current_board, PLAYER_PIECE):
            message_turtle.clear()
            message_turtle.write("YOU WON!", align="center", font=("Arial", 24, "normal"))
            game_over = True
            screen.onclick(None)
            return

        current_turn = 1
        screen.update()

        screen.ontimer(ai_move_handler, 500)


def ai_move_handler():
    global current_turn, game_over, current_board

    if game_over:
        return

    message_turtle.clear()
    message_turtle.write("AI IS THINKING...", align="center", font=("Arial", 20, "normal"))
    screen.update()

    ai_col = get_simple_ai_move(current_board)

    if ai_col is not None and is_valid_location(current_board, ai_col):
        row = get_next_open_row(current_board, ai_col)
        drop_piece(current_board, row, ai_col, AI_PIECE)

        draw_board_turtle(current_board)

        if check_winning_move(current_board, AI_PIECE):
            message_turtle.clear()
            message_turtle.write("AI WON!", align="center", font=("Arial", 24, "normal"))
            game_over = True
            screen.onclick(None)
        else:
            current_turn = 0

    message_turtle.clear()

    if not game_over and not get_valid_locations(current_board):
        message_turtle.write("DRAW!", align="center", font=("Arial", 24, "normal"))
        game_over = True
        screen.onclick(None)

    if not game_over and current_turn == 0:
        message_turtle.write("Your turn. Click!", align="center", font=("Arial", 20, "normal"))


def main():
    draw_board_turtle(current_board)
    message_turtle.write("Your turn. Click!", align="center", font=("Arial", 20, "normal"))
    screen.onclick(handle_click)
    screen.mainloop()


if __name__ == "__main__":
    main()
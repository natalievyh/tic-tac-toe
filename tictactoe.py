import pygame, sys
import numpy as np

pygame.init()

WIDTH = 625
HEIGHT = WIDTH
LINE_WIDTH = 15
BG_COLOR = 200, 150, 150
LINE_COLOR = 185, 90, 90
WHITE = 225, 225, 225
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 45
CIRCLE_WIDTH = 10
SPACE = 65
game_over = False
player = 1

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE')
screen.fill( BG_COLOR )

# create the game board

board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

def draw_lines():
    # draw 2 horizontal lines
    pygame.draw.line( screen, LINE_COLOR, (125, 250), (500, 250), LINE_WIDTH)
    pygame.draw.line( screen, LINE_COLOR, (125, 375), (500, 375), LINE_WIDTH)
    # draw 2 vertical lines
    pygame.draw.line( screen, LINE_COLOR, (250, 125), (250, 500), LINE_WIDTH)
    pygame.draw.line( screen, LINE_COLOR, (375, 125), (375, 500), LINE_WIDTH)
draw_lines()

# draw game pieces on board
def draw_pieces():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            margin_row = 0
            margin_col = 0
            # set margins to fit pieces correctly on the board
            if row == 0:
                margin_col = 80
            if row == 2:
                margin_col = -80
            if col == 0:
                margin_row = 80
            if col == 2:
                margin_row = -80
            # draw player 1 piece as a white circle
            if board[row][col] == 1:
                pygame.draw.circle( screen, WHITE, (int(col * 208 + 208 / 2 + margin_row), int(row * 208 + 208 / 2 + margin_col)), CIRCLE_RADIUS, CIRCLE_WIDTH )
            # draw player 2 piece as a pink 'X'
            elif board[row][col] == 2:
                pygame.draw.line( screen, LINE_COLOR, (col * 208 + margin_row + SPACE, row * 208 + 208 + margin_col - SPACE), (col * 208 + 208 + margin_row - SPACE, row * 208 + margin_col + SPACE), LINE_WIDTH )
                pygame.draw.line( screen, LINE_COLOR, (col * 208 + margin_row + SPACE, row * 208 + margin_col + SPACE), (col * 208 + 208 + margin_row - SPACE, row * 208 + 208 + margin_col - SPACE), LINE_WIDTH )

# marks clicked square with player's piece
def mark_square(row, col, player):
    board[row][col] = player
    draw_pieces()

# checks if square is available
# returns true if available, false if not
def available_square(row, col):
    return (board[row][col] == 0)

# checks if board is full
# returns true if full, false if not
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    # check vertical win
    for col in range(BOARD_COLS):
        if ((board[0][col] == player) & (board[1][col] == player) & (board[2][col] == player)):
            draw_vertical_winning_line(col, player)
            return True
    # check horizontal win
    for row in range(BOARD_ROWS):
        if ((board[row][0] == player) & (board[row][1] == player) & (board[row][2] == player)):
            draw_horizontal_winning_line(row, player)
            return True
        
    # check right diagonal win
    if ((board[2][0] == player) & (board[1][1] == player) & (board[0][2] == player)):
        draw_right_diagonal(player)
        return True

    # check left diagonal win
    if ((board[0][0] == player) & (board[1][1] == player) & (board[2][2] == player)):
        draw_left_diagonal(player)
        return True

    return False

# draw a vertical line if a player wins in a column
def draw_vertical_winning_line(col, player):
    if col == 0:
        posX = 185
    elif col == 1:
        posX = 312
    else:
        posX = 439

    if player == 1:
        color = WHITE
    else:
        color = LINE_COLOR

    pygame.draw.line( screen, color, (posX, 125), (posX, 500), LINE_WIDTH )

# draw a horizontal line if a player wins in a row
def draw_horizontal_winning_line(row, player):
    if row == 0:
        posY = 185
    elif row == 1:
        posY = 312
    elif row == 2:
        posY = 439

    if player == 1:
        color = WHITE
    else:
        color = LINE_COLOR

    pygame.draw.line( screen, color, (125, posY), (500, posY), LINE_WIDTH )

# draw an ascending diagonal line if a player wins on the right diagonal
def draw_right_diagonal(player):
    if player == 1:
        color = WHITE
    else:
        color = LINE_COLOR

    pygame.draw.line( screen, color, (125, 500), (500, 125), LINE_WIDTH )

# draw a descending diagonal line if a player wins on the left diagonal
def draw_left_diagonal(player):
    if player == 1:
        color = WHITE
    else:
        color = LINE_COLOR

    pygame.draw.line( screen, color, (125, 125), (500, 500), LINE_WIDTH )

# restarts game to the blank, original board
def restart():
    screen.fill( BG_COLOR )
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

# converts x coordinate to column number
# returns the column number
def coordinates_to_col(mouseX):
    if ((mouseX > 125) & (mouseX < 250)):
        clicked_col = 0
    elif ((mouseX > 250) & (mouseX < 375)):
        clicked_col = 1
    elif ((mouseX > 375) & (mouseX < 500)):
        clicked_col = 2
    return clicked_col

# converts y coordinate to row number
# returns the row number
def coordinates_to_row(mouseY):
    if ((mouseY > 125) & (mouseY < 250)):
        clicked_row = 0
    elif ((mouseY > 250) & (mouseY < 375)):
        clicked_row = 1
    elif ((mouseY > 375) & (mouseY < 500)):
        clicked_row = 2
    return clicked_row



# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # get coordinates of user click
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if ((mouseX < 500) & (mouseX > 125) & (mouseY < 500) & (mouseY > 125)):
                clicked_col = coordinates_to_col(mouseX)
                clicked_row = coordinates_to_row(mouseY)
                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                    player = player % 2 + 1
        # restart game if user presses the 'r' key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
                player = 1

    pygame.display.update()
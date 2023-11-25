import pygame, sys

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BG_COLOR = 200, 150, 150
LINE_COLOR = 185, 90, 90

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'TIC TAC TOE')
screen.fill( BG_COLOR )

# create the game board

def draw_lines():
    # draw 2 horizontal lines
    pygame.draw.line( screen, LINE_COLOR, (100, 225), (500, 225), LINE_WIDTH)
    pygame.draw.line( screen, LINE_COLOR, (100, 375), (500, 375), LINE_WIDTH)
    # draw 2 vertical lines
    pygame.draw.line( screen, LINE_COLOR, (225, 100), (225, 500), LINE_WIDTH)
    pygame.draw.line( screen, LINE_COLOR, (375, 100), (375, 500), LINE_WIDTH)
draw_lines()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
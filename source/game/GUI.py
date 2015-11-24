import sys, pygame
from Board import *
from Logic import *
pygame.init()

pygame.init()
size = width, height = 252, 252
margin = 6
WIDTH = 35
HEIGHT = 35

#colors
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (128,0,128)
YELLOW = (255,255,0)


board = Board()
screen = pygame.display.set_mode(size)
score = 0
displayedScore = 0
selectedRow = 0
selectedCol = 0
selectedColour = 0
time = 60
done = False
clock = pygame.time.Clock()

#grid

def display():

    for row in range(6):
        for col in range(6):
            if board.getBoard()[row][col] == "R":
                color = RED
            elif board.getBoard()[row][col] == "G":
                color = GREEN
            elif board.getBoard()[row][col] == "P":
                color = PURPLE
            elif board.getBoard()[row][col] == "Y":
                color = YELLOW
            elif board.getBoard()[row][col] == "B":
                color = BLUE
            elif board.getBoard()[row][col] == 0:
                color = BLACK
            pygame.draw.rect(screen,
                    color,
                    [(margin + WIDTH) * col + margin,
                    (margin + HEIGHT) * row + margin,
                    WIDTH, HEIGHT])
    timer = (int)(time - ((pygame.time.get_ticks())/1000)) +1
    texts(displayedScore, timer)
    pygame.display.flip()

def texts(_score, _timer):
    font = pygame.font.Font(None,30)
    scoretext = font.render("Score: " + str(_score), 1, (255,255,255))
    screen.blit(scoretext, (150, 10))
    timertext = font.render("Time: " + str(_timer), 1, (255,255,255))
    screen.blit(timertext, (10,10))


while not done:
    display()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0]//(WIDTH+margin)     ##returns the y coordinate of the board
            row = pos[1] //(WIDTH+margin)       ##returns the x coordinate of the board

            if score == 0:
                selectedRow = row
                selectedCol = column
                selectedColour = board.getBoard()[row][column]
                Logic.removeTile(board,selectedRow,selectedCol)
                score+=1

            if score >= 1:
                if Logic.adjacent(selectedRow, selectedCol, row, column) & Logic.colourMatch(board,row,column,selectedColour):# if colours are the same, and the tiles are adjacent
                    selectedRow = row
                    selectedCol = column
                    Logic.removeTile(board,selectedRow,selectedCol)
                    score+=1

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                displayedScore += score
                Logic.addTile(board)
                score = 0

    clock.tick(60)
    pygame.display.flip()
pygame.quit()
        


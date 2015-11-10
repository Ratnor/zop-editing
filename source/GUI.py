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

done = False
clock = pygame.time.Clock()

#grid
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
        pygame.draw.rect(screen,
                     color,
                     [(margin + WIDTH) * col + margin,
                      (margin + HEIGHT) * row + margin,
                      WIDTH, HEIGHT])
        pygame.display.flip()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0]//(WIDTH+margin)     ##returns the y coordinate of the board
            row = pos[1] //(WIDTH+margin)       ##returns the x coordinate of the board
            print("Click ",pos,"Grid coordinates: ", row, column)
            
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
        


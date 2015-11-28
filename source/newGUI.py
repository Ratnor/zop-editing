
import pygame
from Board import *
from Logic import *
pygame.init()


class GameMenu():
    def __init__(self, screen, startItems, board, displayedScore, bg_color=(0,0,0), font=None, font_color=(0, 0, 0)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.counter, self.text = 60, '60'.rjust(10)
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        font_size = int(self.scr_width/10)
        self.startItems = startItems
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color


        '''''''''''
        START SCREEN
        '''''''''''
        self.startItems = []
        for index, item in enumerate(startItems):
            label = self.font.render(item, 1, font_color)

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = (len(startItems) * height)
            posy = (self.scr_height / 2) - (t_h / 2) + (index * (height+10))

            self.startItems.append([item, index, font_color, label, (width, height), (posx, posy)])

        '''''''''''
        GAME SCREEN
        '''''''''''
        self.gameWidth = self.scr_width - (self.scr_width/7)
        self.gameHeight = self.scr_width - (self.scr_width/7)
        self.board = board
        self.blockMargin = int(self.gameHeight/36)
        self.blockWidth = int(self.gameWidth/6 - self.blockMargin - (self.blockMargin/6))
        self.blockHeight = int(self.gameHeight/6 - self.blockMargin - (self.blockMargin/6))
        self.score = 0
        self.displayedScore = displayedScore
        self.maxRows = 6
        self.maxColumns = 6


        self.isDragging = False


    def delay(self):
        count = 0
        while count < 2000000:
            count += 1


    def run(self):
        mainloop = True
        startDisplay = True
        gameDisplay = False
        endDisplay = False


        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(60)

            # quit game
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    self.counter -= 1
                    if self.counter > 0:
                        self.text = str(self.counter).rjust(10)
                    else:
                        gameDisplay = False
                        endDisplay = True
                if event.type == pygame.QUIT:
                    mainloop = False

            # end of game display
            if endDisplay:
                endItem = ("Score: " + str(self.displayedScore))
                endLabel = self.font.render(endItem, 1, font_color)

                width = endLabel.get_rect().width
                height = endLabel.get_rect().height

                end_posx = (self.scr_width / 2) - (width / 2)
                end_posy = (self.scr_height / 2) - (height / 2)

                self.screen.fill(self.bg_color)
                self.screen.blit(endLabel, (end_posx, end_posy))


            # game display
            if gameDisplay:
                self.display()
                print (self.text)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.isDragging = True

                if event.type == pygame.MOUSEBUTTONUP:
                    self.isDragging = False
                    if self.score == 1:
                        board.getBoard()[selectedRow][selectedCol] = selectedColour
                    else:
                        self.displayedScore += self.score
                        Logic.addTile(board)
                    self.score = 0
                    if self.displayedScore >= 60:
                        gameDisplay = False
                        self.screen.fill(self.bg_color)
                        endDisplay = True

                if self.isDragging:
                    if event.type == pygame.MOUSEMOTION:
                        pos = pygame.mouse.get_pos()
                        if (((pos[0] >= 0) & (pos[0] <= self.gameWidth)) & ((pos[1] >= 0 & pos[1]) <= (self.gameHeight))): ## if we click within game display
                            column = pos[0]//(self.blockWidth+self.blockMargin)     ##returns the y coordinate of the board
                            row = pos[1] //(self.blockHeight+self.blockMargin)       ##returns the x coordinate of the board
                            if row >= self.maxRows:
                                row = 5
                            if column >= self.maxColumns:
                                column = 5

                            if self.score == 0:
                                selectedRow = row
                                selectedCol = column
                                selectedColour = board.getBoard()[row][column]
                                Logic.removeTile(board,selectedRow,selectedCol)
                                self.score+=1


                            if self.score >= 1:
                                if Logic.adjacent(selectedRow, selectedCol, row, column) & Logic.colourMatch(board,row,column,selectedColour):# if colours are the same, and the tiles are adjacent
                                    selectedRow = row
                                    selectedCol = column
                                    Logic.removeTile(board,selectedRow,selectedCol)
                                    self.score+=1
                            if event.type == pygame.MOUSEBUTTONUP:
                                self.isDragging = False

                if event.type == pygame.MOUSEBUTTONUP:
                    self.isDragging = False
                    if self.score == 1:
                        board.getBoard()[selectedRow][selectedCol] = selectedColour
                    else:
                        self.displayedScore += self.score
                        Logic.addTile(board)
                    self.score = 0
                    if self.displayedScore >= 60:
                        gameDisplay = False
                        self.screen.fill(self.bg_color)
                        endDisplay = True

            if self.isDragging:
                    if event.type == pygame.MOUSEMOTION:
                        pos = pygame.mouse.get_pos()
                        if (((pos[0] >= 0) & (pos[0] <= self.gameWidth)) & ((pos[1] >= 0 & pos[1]) <= (self.gameHeight))): ## if we click within game display
                            column = pos[0]//(self.blockWidth+self.blockMargin)     ##returns the y coordinate of the board
                            row = pos[1] //(self.blockHeight+self.blockMargin)       ##returns the x coordinate of the board
                            if row >= self.maxRows:
                                row = 5
                            if column >= self.maxColumns:
                                column = 5

                            if self.score == 0:
                                selectedRow = row
                                selectedCol = column
                                selectedColour = board.getBoard()[row][column]
                                Logic.removeTile(board,selectedRow,selectedCol)
                                self.score+=1


                            if self.score >= 1:
                                if Logic.adjacent(selectedRow, selectedCol, row, column) & Logic.colourMatch(board,row,column,selectedColour):# if colours are the same, and the tiles are adjacent
                                    selectedRow = row
                                    selectedCol = column
                                    Logic.removeTile(board,selectedRow,selectedCol)
                                    self.score+=1
            #start menu display
            if startDisplay:
                # Redraw the background
                self.screen.fill(self.bg_color)
                for name, index, font_color, label, (width, height), (posx, posy) in self.startItems:
                    pygame.draw.rect(self.screen,(0, 0, 0),(posx-6, posy-6, width+12, height+2), 1)
                    if index == 0:
                        pygame.draw.rect(self.screen,(255, 0, 0),(posx-5, posy-5, width+10, height), 0)
                    if index == 1:
                        pygame.draw.rect(self.screen,(0, 255, 0),(posx-5, posy-5, width+10, height), 0)
                    if index == 2:
                        pygame.draw.rect(self.screen,(0, 0, 255),(posx-5, posy-5, width+10, height), 0)

                    self.screen.blit(label, (posx, posy))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for name, index, font_color, label, (width, height), (posx, posy) in self.startItems:
                        if ((pos[0] >= posx - 10) & (pos[0] <= posx + width + 5)) & ((pos[1] >= posy - 10) & (pos[1] <= posy + height - 5)):
                            if index == 0:
                                startDisplay = False
                                self.screen.fill(self.bg_color)
                                self.delay()
                                pygame.time.set_timer(pygame.USEREVENT, 1000)
                                gameDisplay = True
                            elif index == 1:
                                print("High Scores")
                            elif index == 2:
                                mainloop = False

            pygame.display.flip()

    def display(self):
        color = 0,0,0
        for row in range(6):
            for col in range(6):
                if self.board.getBoard()[row][col] == "R":
                    color = (255, 0, 0)#red
                elif self.board.getBoard()[row][col] == "G":
                    color = (0, 255, 0)#green
                elif self.board.getBoard()[row][col] == "P":
                    color = (128, 0, 128)#purple
                elif self.board.getBoard()[row][col] == "Y":
                    color = (255 ,255, 0)#yellow
                elif self.board.getBoard()[row][col] == "B":
                    color = (0, 0, 255)#blue
                elif self.board.getBoard()[row][col] == 0:
                    color = (0, 0, 0)#black
                pygame.draw.rect(self.screen,color,
                        [(self.blockMargin + self.blockWidth) * col + self.blockMargin,
                        (self.blockMargin + self.blockHeight) * row + self.blockMargin,
                        self.blockWidth, self.blockHeight])

if __name__ == "__main__":
    # Creating the screen
    screenWidth = 600
    screenHeight = int(screenWidth - (screenWidth/6))
    screen = pygame.display.set_mode((screenWidth, screenHeight), 0, 32)

    startMenu_items = ('Start', 'High Scores', 'Quit')
    board = Board()
    displayedScore = 0

    pygame.display.set_caption('Zop')
    gm = GameMenu(screen, startMenu_items, board, displayedScore)
    gm.run()

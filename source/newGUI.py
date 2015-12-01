import pygame
from Board import *
from Logic import *

pygame.init()


class GameMenu():
    def __init__(self, screen, startItems, board, displayedScore, bg_color=(180, 180, 180), font=None,
                 font_color=(0, 0, 0)):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.counter, self.text = 60, '60'.rjust(1)
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
        font_size = int(self.scr_width / 10)
        self.startItems = startItems
        self.font = pygame.font.SysFont(font, font_size)
        self.font_color = font_color

        '''''''''''
        START SCREEN
        '''''''''''
        #get start labels
        self.startItems = []
        for index, item in enumerate(startItems):
            label = self.font.render(item, 1, font_color)

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = (len(startItems) * height)
            posy = (self.scr_height / 2) - (t_h / 2) + (index * (height + 10))

            self.startItems.append([item, index, font_color, label, (width, height), (posx, posy)])

        '''''''''''
        GAME SCREEN
        '''''''''''
        self.gameWidth = self.scr_width - 3 * (self.scr_width / 9)
        self.gameHeight = self.scr_width - 3 * (self.scr_width / 9)
        self.board = board
        self.blockMargin = int(self.gameHeight / 36)
        self.blockWidth = int(self.gameWidth / 6 - self.blockMargin - (self.blockMargin / 6))
        self.blockHeight = int(self.gameHeight / 6 - self.blockMargin - (self.blockMargin / 6))
        self.score = 0
        self.displayedScore = displayedScore
        self.maxRows = 6
        self.maxColumns = 6

        self.isDragging = False

        self.hsItems = []
        self.resLabel = None
        self.res_height = 0
        self.res_width = 0
        self.res_posx = 0
        self.res_posy = 0

        #if file exists do nothing, else, create a new file with 0 in high scores
        try:
            hs_file = open("high_scores.txt", 'r')
            hs_file.close()
        except:
            hs_file = hs_file = open("high_scores.txt", 'w')
            hs_file.write("High Score List.\n1.0.\n2.0.\n3.0.")
            hs_file.close()

    #delay counter
    def delay(self):
        count = 0
        while count < 2000000:
            count += 1

    def run(self):
        #state variables
        mainloop = True
        startDisplay = True
        gameDisplay = False
        endDisplay = False
        highScoreDisplay = False
        updateHighScores = False

        while mainloop:
            # Limit frame speed to 200 FPS
            self.clock.tick(200)

            # init event variable
            for event in pygame.event.get():
                #timer
                if event.type == pygame.USEREVENT:
                    self.counter -= 1
                    if self.counter >= 0:
                        self.text = str(self.counter).rjust(1)
                    elif self.counter == -1:
                        gameDisplay = False
                        updateHighScores = True
                        endDisplay = True
                # quit
                if event.type == pygame.QUIT:
                    mainloop = False
            '''''''''
            end of game display
            '''''''''
            if endDisplay:
                # read, write to high scores txt file once when end display is called
                if updateHighScores:
                    infile = open('high_scores.txt', 'r')
                    title = infile.readline().split('.')
                    score_1 = int(infile.readline().split('.')[1])
                    score_2 = int(infile.readline().split('.')[1])
                    score_3 = int(infile.readline().split('.')[1])
                    infile.close()

                    (score_1, score_2, score_3) = self.hsSort(self.displayedScore, score_1, score_2, score_3)

                    outfile = open('high_scores.txt', 'w')
                    outfile.write(
                        ".".join(title) + "1." + str(score_1) + ".\n" + "2." + str(score_2) + ".\n" + "3." + str(score_3) + ".\n")
                    outfile.close()

                    updateHighScores = False

                #score label
                endItem = ("Score: " + str(self.displayedScore))
                endLabel = self.font.render(endItem, 1, font_color)

                width = endLabel.get_rect().width
                height = endLabel.get_rect().height

                end_posx = (self.scr_width / 2) - (width / 2)
                end_posy = (self.scr_height / 2) - (height / 2)

                #main menu label
                mmItem = ("Main Menu")
                mmLabel = self.font.render(mmItem, 1, self.font_color)

                mm_width = mmLabel.get_rect().width
                mm_height = mmLabel.get_rect().width

                mm_posx = (self.gameWidth/3) - (mm_width / 2)
                mm_posy = self.scr_height - self.blockMargin * 5

                #restart label
                resItem = ("Restart")
                resLabel = self.font.render(resItem, 1, self.font_color)

                res_width = resLabel.get_rect().width
                res_height = resLabel.get_rect().width

                res_posx = ((self.scr_width + self.gameWidth) / 2) - (res_width / 2)
                res_posy = self.scr_height - self.blockMargin * 5

                # add labels onto screen
                self.screen.fill(self.bg_color)
                self.screen.blit(endLabel, (end_posx, end_posy))
                self.screen.blit(mmLabel, (mm_posx, mm_posy))
                self.screen.blit(resLabel, (res_posx, res_posy))

                #events and labels are pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if ((pos[0] >= mm_posx - 10) & (pos[0] <= mm_posx + mm_width + 5)) & ((pos[1] >= mm_posy - 10) & (pos[1] <= mm_posy + mm_height - 5)):
                        endDisplay = False
                        self.board = Board()
                        self.counter = 60
                        self.text = '60'
                        self.displayedScore = 0
                        self.score = 0
                        self.screen.fill(self.bg_color)
                        startDisplay = True
                    if ((pos[0] >= res_posx - 10) & (pos[0] <= res_posx + res_width + 5)) & ((pos[1] >= res_posy - 10) & (pos[1] <= res_posy + res_height - 5)):
                        endDisplay = False
                        self.board = Board()
                        self.counter = 60
                        self.text = '60'
                        self.displayedScore = 0
                        self.score = 0
                        self.screen.fill(self.bg_color)
                        gameDisplay = True

            '''''''''
            game display
            '''''''''
            if gameDisplay:
                # game display (w/ timer, score, board, and restart)
                self.display()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.isDragging = True

                if event.type == pygame.MOUSEBUTTONUP:
                    self.isDragging = False
                    # if only one tile is selected, keep the same tile
                    if self.score == 1:
                        self.board.getBoard()[selectedRow][selectedCol] = selectedColour
                    # else, update total score and board
                    else:
                        self.displayedScore += self.score
                        Logic.addTile(self.board)
                    #turn score set to 0
                    self.score = 0

                # when mouse button is down
                if self.isDragging:
                    if event.type == pygame.MOUSEMOTION:
                        pos = pygame.mouse.get_pos()
                        if ((pos[0] >= 0) & (pos[0] <= self.gameWidth)) & ((pos[1] >= 0 & pos[1]) <= (self.gameHeight)):  ## if we click within game display
                            column = pos[0] // (self.blockWidth + self.blockMargin)  ##returns the y coordinate of the board
                            row = pos[1] // (self.blockHeight + self.blockMargin)  ##returns the x coordinate of the board
                            if row >= self.maxRows:
                                row = 5
                            if column >= self.maxColumns:
                                column = 5

                            #select first piece
                            if self.score == 0:
                                selectedRow = row
                                selectedCol = column
                                selectedColour = self.board.getBoard()[row][column]
                                Logic.removeTile(self.board, selectedRow, selectedCol)
                                self.score += 1
                            #for new pieces selected
                            if self.score >= 1:
                                if Logic.adjacent(selectedRow, selectedCol, row, column) & Logic.colourMatch(self.board, row, column, selectedColour):  # if colours are the same, and the tiles are adjacent
                                    selectedRow = row
                                    selectedCol = column
                                    Logic.removeTile(self.board, selectedRow, selectedCol)
                                    self.score += 1
                        # if restart is clicked, reset counter, board, and score
                        if ((pos[0] >= self.res_posx - 10) & (pos[0] <= self.res_posx + self.res_width + 5)) & ((pos[1] >= self.res_posy - 10) & (pos[1] <= self.res_posy + self.res_height - 5)):
                            self.board = Board()
                            self.counter = 60
                            self.text = '60'
                            self.displayedScore = 0
                            self.score = 0

            '''''''''
            high score display
            '''''''''
            if highScoreDisplay:
                #open high score txt file, get scores
                infile = open('high_scores.txt', 'r')
                title = infile.readline().split('.')
                score_1 = infile.readline().split('.')
                score_2 = infile.readline().split('.')
                score_3 = infile.readline().split('.')
                infile.close()

                #high score labels
                hsItems = (title[0] + ":", score_1[0] + ". " + score_1[1], score_2[0] + ". " + score_2[1], score_3[0] + ". " + score_3[1])
                self.hsItems = []
                for index, item in enumerate(hsItems):
                    label = self.font.render(item, 1, font_color)

                    hs_width = label.get_rect().width
                    hs_height = label.get_rect().height

                    hs_posx = (self.scr_width / 2) - (hs_width / 2)
                    hs_t_h = (len(hsItems) * hs_height)
                    hs_posy = (self.scr_height / 2) - (hs_t_h / 2) + (index * (hs_height + 10))

                    self.hsItems.append([item, index, font_color, label, (hs_width, hs_height), (hs_posx, hs_posy)])

                #back label
                backItem = ("Back")
                backLabel = self.font.render(backItem, 1, self.font_color)

                back_width = backLabel.get_rect().width
                back_height = backLabel.get_rect().width

                back_posx = ((self.scr_width + self.gameWidth) / 2) - (back_width / 2)
                back_posy = self.scr_height - self.blockMargin * 5


                #redraw background, add labels
                self.screen.fill(self.bg_color)
                for name, index, font_color, label, (hs_width, hs_height), (hs_posx, hs_posy) in self.hsItems:
                    pygame.draw.rect(self.screen, (0, 0, 0), (hs_posx - 6, hs_posy - 6, hs_width + 12, hs_height + 2), 1)
                    if index == 0:
                        pygame.draw.rect(self.screen, (255, 0, 0), (hs_posx - 5, hs_posy - 5, hs_width + 10, hs_height), 0)
                    if index == 1:
                        pygame.draw.rect(self.screen, (0, 255, 0), (hs_posx - 5, hs_posy - 5, hs_width + 10, hs_height), 0)
                    if index == 2:
                        pygame.draw.rect(self.screen, (0, 0, 255), (hs_posx - 5, hs_posy - 5, hs_width + 10, hs_height), 0)
                    if index == 3:
                        pygame.draw.rect(self.screen, (255, 0, 255), (hs_posx - 5, hs_posy - 5, hs_width + 10, hs_height), 0)

                    self.screen.blit(label, (hs_posx, hs_posy))
                self.screen.blit(backLabel, (back_posx, back_posy))
                # back button event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if ((pos[0] >= back_posx - 10) & (pos[0] <= back_posx + back_width + 5)) & ((pos[1] >= back_posy - 10) & (pos[1] <= back_posy + back_height - 5)):
                        highScoreDisplay = False
                        self.screen.fill(self.bg_color)
                        startDisplay = True

            '''''''''
            start menu display
            '''''''''
            if startDisplay:
                # Redraw the background
                #start screen labels and add labels
                self.screen.fill(self.bg_color)
                for name, index, font_color, label, (width, height), (posx, posy) in self.startItems:
                    pygame.draw.rect(self.screen, (0, 0, 0), (posx - 6, posy - 6, width + 12, height + 2), 1)
                    if index == 0:
                        pygame.draw.rect(self.screen, (255, 0, 0), (posx - 5, posy - 5, width + 10, height), 0)
                    if index == 1:
                        pygame.draw.rect(self.screen, (0, 255, 0), (posx - 5, posy - 5, width + 10, height), 0)
                    if index == 2:
                        pygame.draw.rect(self.screen, (0, 0, 255), (posx - 5, posy - 5, width + 10, height), 0)

                    self.screen.blit(label, (posx, posy))
                #label events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for name, index, font_color, label, (width, height), (posx, posy) in self.startItems:
                        if ((pos[0] >= posx - 10) & (pos[0] <= posx + width + 5)) & ((pos[1] >= posy - 10) & (pos[1] <= posy + height - 5)):
                            if index == 0:
                                startDisplay = False
                                self.screen.fill(self.bg_color)
                                self.delay()
                                # start timer
                                pygame.time.set_timer(pygame.USEREVENT, 1000)
                                gameDisplay = True
                            elif index == 1:
                                startDisplay = False
                                self.screen.fill(self.bg_color)
                                highScoreDisplay = True
                            elif index == 2:
                                mainloop = False

            pygame.display.flip()

    def display(self):
        self.screen.fill(self.bg_color)
        for row in range(6):
            for col in range(6):
                if self.board.getBoard()[row][col] == "R":
                    color = (255, 0, 0)  # red
                elif self.board.getBoard()[row][col] == "G":
                    color = (0, 255, 0)  # green
                elif self.board.getBoard()[row][col] == "P":
                    color = (128, 0, 128)  # purple
                elif self.board.getBoard()[row][col] == "Y":
                    color = (255, 255, 0)  # yellow
                elif self.board.getBoard()[row][col] == "B":
                    color = (0, 0, 255)  # blue
                elif self.board.getBoard()[row][col] == 0:
                    color = (0, 0, 0)  # black
                pygame.draw.rect(self.screen, color,
                                 [(self.blockMargin + self.blockWidth) * col + self.blockMargin,
                                  (self.blockMargin + self.blockHeight) * row + self.blockMargin,
                                  self.blockWidth, self.blockHeight])

            # timer label
            timerItem = ("Time: " + self.text)
            timerLabel = self.font.render(timerItem, 1, self.font_color)

            timer_width = timerLabel.get_rect().width

            timer_posx = ((self.scr_width + self.gameWidth) / 2) - (timer_width / 2)
            timer_posy = self.blockMargin

            self.screen.blit(timerLabel, (timer_posx, timer_posy))

            # score label
            scoreItem = ("Score: " + str(self.displayedScore))
            scoreLabel = self.font.render(scoreItem, 1, self.font_color)

            score_width = scoreLabel.get_rect().width

            score_posx = ((self.scr_width + self.gameWidth) / 2) - (score_width / 2)
            score_posy = self.blockMargin * 5

            self.screen.blit(scoreLabel, (score_posx, score_posy))


            # restart label
            resItem = ("Restart")
            self.resLabel = self.font.render(resItem, 1, self.font_color)

            self.res_width = self.resLabel.get_rect().width
            self.res_height = self.resLabel.get_rect().height

            self.res_posx = ((self.scr_width + self.gameWidth) / 2) - (self.res_width / 2)
            self.res_posy = self.scr_height - (self.blockMargin * 5)

            self.screen.blit(self.resLabel, (self.res_posx, self.res_posy))
    # "sort" high score list
    def hsSort(self, currentScore, score1, score2, score3):
        if currentScore > score1:
            score3 = score2
            score2 = score1
            score1 = currentScore
            return (score1, score2, score3)
        elif currentScore > score2:
            score3 = score2
            score2 = currentScore
            return (score1, score2, score3)
        elif currentScore > score3:
            score3 = currentScore
            return (score1, score2, score3)
        else:
            return (score1, score2, score3)



if __name__ == "__main__":
    # Creating the screen
    screenWidth = 1080
    screenHeight = int(screenWidth - 3 * (screenWidth / 9))
    screen = pygame.display.set_mode((screenWidth, screenHeight), 0, 32)

    startMenu_items = ('Start', 'High Scores', 'Quit')
    board = Board()
    displayedScore = 0

    pygame.display.set_caption('Zop')
    gm = GameMenu(screen, startMenu_items, board, displayedScore)
    gm.run()

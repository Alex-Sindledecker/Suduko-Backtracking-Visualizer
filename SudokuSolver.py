import pygame, time, sys


class Sudoku:
    win_size = 650
    color_black = pygame.Color(0, 0, 0)
    
    def __init__(self):
        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.ogboard = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        pygame.init()
        self.screen = pygame.display.set_mode((self.win_size, self.win_size))
        self.m_font = pygame.font.SysFont("Comic Sans MS", 30)
        self.block_size = int(self.win_size / 9)
        

    def checkWinEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True


    def renderBoard(self):
        self.screen.fill(pygame.Color(255, 255, 255))
        
        for i in range(0, self.win_size, self.block_size):
            pygame.draw.line(self.screen, self.color_black, (i, 0), (i, self.win_size))
            pygame.draw.line(self.screen, self.color_black, (0, i), (self.win_size, i))
        for i in range(9):
            for n in range(9):
                if self.ogboard[i][n] == 0 and self.board[i][n] != 0:
                    self.renderNumber(i, n, self.board[i][n], (0, 0, 255))
                elif self.board[i][n] != 0:
                    self.renderNumber(i, n, self.board[i][n])


    def renderNumber(self, row, col, number, color = color_black):
        num = str(number)
        text_xpos = col * self.block_size + self.block_size / 2 - self.m_font.size(num)[0] / 2
        text_ypos = row * self.block_size + self.block_size / 2 - self.m_font.size(num)[1] / 2
        self.screen.blit(self.m_font.render(num, True, color), (text_xpos, text_ypos))


    def validNode(self, row, col, val):
        # print("Validating node at row: {}, and col: {}".format(row, col))
        for i in range(0, 9):
            if self.board[row][i] == val or self.board[i][col] == val:
                return False
        sub_grid_row = row - row % 3
        sub_grid_col = col - col % 3
        for r in range(sub_grid_row, sub_grid_row + 3):
            for c in range(sub_grid_col, sub_grid_col + 3):
                if self.board[r][c] == val:
                    return False
        return True


    def solve(self):
        self.solveNode(0, 0)


    def solveNode(self, row, col):
        if col >= 9:
            row += 1
            col = 0
        if row >= 9:
            return True

        if self.board[row][col] != 0:
            return self.solveNode(row, col + 1)

        for i in range(1, 10):
            self.renderBoard()
            self.renderNumber(row, col, i, (0, 0, 255))
            pygame.display.flip()
            #time.sleep(0.01)
            if self.validNode(row, col, i):
                self.board[row][col] = i
                next_node_solved = self.solveNode(row, col + 1)
                if next_node_solved:
                    return True
                else:
                    self.board[row][col] = 0
            else:
                self.board[row][col] = 0
        return False
    
    
puzzle = Sudoku()
puzzle.solve()
while puzzle.checkWinEvents():
    pass
pygame.quit()

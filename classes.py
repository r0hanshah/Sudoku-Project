import pygame
from sudoku_generator import generate_sudoku
from sudoku_generator import SudokuGenerator
HEIGHT = 800
WIDTH = 600

class Cell:
    def __init__(self, value, row, col, display):  
        #Constructor for the Cell class   
        self.value = value
        self.row = row
        self.col = col
        self.display = display
        self.selected = False
        self.sketched_value = None
        self.original_value = value
        self.submitted = False
        self.reset = False
       
    
  
    def set_cell_value(self, value):
    #Setter for this cell’s value  
        self.value = value
  
    def set_sketched_value(self, sketched_value):  
    #Setter for this cell’s sketched value
        self.sketched_value = sketched_value  
  
#Draws this cell, along with the value inside it.  
#If this cell has a nonzero value, that value is displayed.    
#Otherwise, no value is displayed in the cell.  
#The cell is outlined red if it is currently selected. 

    def draw(self):
        # this clears the cell if it is reset
        if self.reset == True:
            pygame.draw.rect(self.display, ("black"), (self.col * 66 + 20, self.row * 66 + 20, 45, 45))
            self.sketched_value = None
            pygame.draw.rect(self.display, ("black"), (self.col * 64 + 20, self.row * 64 + 20, 45, 45))
            self.reset = False
            
            
        if self.value == self.original_value and self.sketched_value == None and self.reset== True:
                pygame.draw.rect(self.display, ("green"), (self.col * 66 + 20, self.row * 66 + 20, 45, 45))
            
                # print("HELLO")
        # this highlights the selected cell
        if self.selected == True and self.value == 0:
            pygame.draw.rect(self.display, ("red"), (self.col * 66, self.row * 66, 66, 66), 3)
        # this creates the cell
        else: #GRID
            # pygame.draw.rect(self.display, ("white"), (self.col * 75, self.row * 65, 65, 65), 1)
            
            #changed from 50 to 60
            #rectangle = pygame.Rect(self.col * 50, self.row * 50, 50, 50)
            #pygame.draw.rect(self.display, ("white"), rectangle,  2)

            block_size = 600//9
            for i in range(0, 600 - block_size, block_size):
                for j in range(0, 600 - block_size, block_size):
                    rect = pygame.Rect(i, j, block_size, block_size)
                    pygame.draw.rect(self.display, ("white"), rect, 1)
        #This should clear the cell if the value is 0
        if self.sketched_value == 0 and self.value == 0:
            pygame.draw.rect(self.display, ("black"), (self.col * 66 + 20, self.row * 66 + 20, 45, 45))
            print("SOMETHING")
        # 
        if self.value != 0 and self.value != None:
            #NUMBERS ON SCREEN
            font = pygame.font.SysFont('OptimusPrinceps.ttf', 45)
            text = font.render(str(self.value), True, ("white"))
            # create a filled black box behind the value to make it more visible
            pygame.draw.rect(self.display, ("black"), (self.col * 64 + 20, self.row * 64 + 20, 45, 45))
            self.display.blit(text, (self.col * 66 + 22, self.row * 66 + 22))

        if self.sketched_value != None and self.value == 0 and self.sketched_value != 0:
            font = pygame.font.SysFont('OptimusPrinceps.ttf', 35)
            text = font.render(str(self.sketched_value), True, ("green"))
            # create a filled black box behind the sketched value to make it more visible
            pygame.draw.rect(self.display, ("black"), (self.col * 64 + 20, self.row * 64 + 20, 45, 45))
            self.display.blit(text, (self.col * 64 + 20, self.row * 64 + 20))

        if self.selected == False:
            pygame.draw.rect(self.display, ("white"), (self.col * 66, self.row * 66, 66, 66), 3)
            # print("OK")
        if self.sketched_value == None:
            pass
        # conditions for when the cell is reset


            # text = font.render(str(self.value), True, BLACK)
            # self.screen.blit(text, (self.col * CELL_WIDTH + 10, self.row * CELL_HEIGHT + 10))
        #else:
            #pygame.draw.rect(self.screen, BLACK, (self.col * CELL_WIDTH, self.row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 1)
            ''''''
            
            # Get the set of keys pressed and check for user input
            pressed_keys = pygame.key.get_pressed()
       
    '''    
Board (Recommended) 
This class represents an entire Sudoku board. A Board object has 81 Cell objects.
    
    '''
class Board:
  def __init__(self, width, height, display, difficulty): 
  #Constructor for the Board class.  
  #screen is a window from PyGame.  
  #difficulty is a variable to indicate if the user chose easy, medium, or hard.  
    self.width = width
    self.height = height
    self.display = display
    self.difficulty = difficulty
    self.board = generate_sudoku(9, self.difficulty)
    self.cells = [[Cell(self.board[i][j], i, j, self.display) for j in range(9)] for i in range(9)]
    
   
  def draw(self,display):
  #Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.  
  #Draws every cell on this board. 
    block_size = 600//3
  # FROM TICTACTOE
    #this is the bold 3x3
    # draw horizontal lines
    for i in range(0, 4):
        pygame.draw.line(
             display,
             'white',
             (0, i * 200),
             (WIDTH, i * 200),
            10
         )
    #draw vertical lines 
    for j in range(0, 4):
         pygame.draw.line(
             display,
             "white",
             (j * 200, 0),
             (j * 200, 600),
             10
             #line(surface, color, start_pos, end_pos, width=1) -> Rect
         )
    
    # draw the cells
    for i in range(9):
        for j in range(9):
            self.cells[i][j].draw()

    

  def select(self, row, col): 
  #Marks the cell at (row, col) in the board as the current selected cell.  
  #Once a cell has been selected, the user can edit its value or sketched value. 
    for lists in self.cells:
        for cell in lists:
            if cell.selected == True and row >= 0 and row <= 8 and col >= 0 and col <= 8:
                cell.selected = False
                self.cells[row][col].selected = True
            elif cell.selected == False and row >= 0 and row <= 8 and col >= 0 and col <= 8:
                self.cells[row][col].selected = True
                cell.selected = False
             
    if row >= 0 and row <= 8 and col >= 0 and col <= 8:
        self.cells[row][col].selected = True
    
   
  def click(self, x, y):  
  #If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the 
  # (row, col) of the cell which was clicked. Otherwise, this function returns None.
    if x < 0 or x > self.width or y < 0 or y > self.height:
       return None
    row = int(y // 66.67)
    col = int(x // 66.67)
    return (row, col)
   
  def clear(self):  
  #Clears  the  value  cell.  Note  that  the  user  can  only  remove  the  cell  values  and  sketched  value  that  are filled by themselves.  
    for lists in self.cells:
        for cell in lists:
            if cell.selected:
                cell.value = 0
    
   
  def sketch(self, value):
  #Sets the sketched value of the current selected cell equal to user entered value.  
  #It will be displayed at the top left corner of the cell using the draw() function.
    for lists in self.cells:
        for cell in lists:
            if cell.selected:
                if cell.value == 0:
                    cell.sketched_value = value
                    cell.original_value = 0
                    # print(cell.sketched_value)
                    cell.selected = False
                    
                    cell.value = 0
                    return 
    
   
  def place_number(self, value):
  #Sets the value of the current selected cell equal to user entered value.  
  #Called when the user presses the Enter key.  
    for lists in self.cells:
        for cell in lists:
            if cell.selected:
                if cell.submitted == False:
                    cell.value = value
                    cell.selected = False
                    print(cell.value)
                    cell.sketched_value = 0
                    cell.submitted = True 
                    if cell.value == 0:
                        cell.submitted = False
                    return
                

    

    
  def reset_to_original(self):
  #Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit). 
    """ for lists in self.cells:
        for cell in lists:
            if cell.original_value == 0 and cell.value != 0:
                cell.value = 0
                cell.sketched_value = 0
                cell.selected = False
                print("DEEZ nuts")
                return
            else:
                cell.value = 0
                cell.sketched_value = 0
                cell.selected = False
                print("THOSE NUTS")
                return """

    for lists in self.cells:
        for cell in lists:
            #this runs for pre filled in cells
            print(cell.original_value)
            if cell.sketched_value != None:
                cell.value = cell.original_value
                cell.sketched_value = None
                cell.reset = True
                cell.submitted = False
                print("hi michael")
            if cell.original_value != 0:
                cell.value = cell.original_value
                cell.sketched_value = None
                cell.selected = False
                cell.reset = True
                cell.submitted = False
            
                print("hi rohan")
                # return
            #this runs for cells that are not pre filled in/ empty
            else:
                cell.value = 0
                cell.sketched_value = None
                cell.selected = False
                cell.reset = True
                cell.submitted = False
                print("HIIIIIII")
                # return
                
   
  def is_full(self):
    #Returns a Boolean value indicating whether the board is full or not.  
    for i in range(9):
        for j in range(9):
            if self.board[i][j] == 0:
                return False
    return True


  def update_board(self):
    #Updates the underlying 2D board with the values in all cells. 
    for i in range(9):
        for j in range(9):
            self.board[i][j] = self.cells[i][j].value
   
  def find_empty(self):
    #Finds an empty cell and returns its row and col as a tuple (x, y).  
    #If there are no empty cells, returns None.
    for i in range(9):
        for j in range(9):
            if self.board[i][j] == 0:
                return (i, j)
    return None
   
#   this isn't correct
  def check_board(self):  
    #Check whether the Sudoku board is solved correctly by confirming row, column, and boxes are all valid
    #Returns True if the board is solved, False otherwise.
    # checks the rows
    print('checking rows')
    for i in range(9):
        for j in range(8):
            print(self.board[i][j])
            if self.board[i][j] == 0:
                return False
            if self.board[i][j] in self.board[i][j+1:]:
                return False
    
    # checks the columns
    # print('checking columns')
    # for i in range(9):
    #     for j in range(8):
    #         print(self.board[j][i])
    #         if self.board[j][i] == 0:
    #             return False
    #         if self.board[j][i] in self.board[j+1:][i]:
    #             return False
    
    # # checks the boxes
    # print('checking boxes')
    # for i in range(3):
    #     for j in range(2):
    #         print(self.board[i][j])
    #         if self.board[i][j] == 0:
    #             return False
    #         if self.board[i][j] in self.board[i][j+1:]:
    #             return False
    return True
    
import math,random
import pygame
import sys
import copy

HEIGHT = 800
WIDTH = 600

# FINISHED 
class SudokuGenerator:
    '''
    create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.row_length		- the length of each row
	self.removed_cells	- the total number of cells to be removed
	self.board			- a 2D list of ints to represent the board
	self.box_length		- the square root of row_length

	Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed

	Return:
	None
    '''
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
    #   I added the int(), might break something later on -dylan
        self.box_length = int(math.sqrt(self.row_length))
        self.board = [["0" for i in range(self.row_length)]
                         for j in range(self.row_length)]
                         
    
    '''
	Returns a 2D python list of numbers that represents the board

	Parameters: None
	Return: list[list]
    '''
    def get_board(self):
        return self.board

    '''
	Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes

	Parameters: None
	Return: None
    '''
    def print_board(self):
        for i, row in enumerate(self.board):
            for j,col in enumerate(row):
                print(self.board [i][j], end = " ")
            print()
    '''
	Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

	Parameters:
	row is the index of the row we are checking
	num is the value we are looking for in the row
	
	Return: boolean
    '''
    def valid_in_row(self, row, num):
        if num in self.board[row]:
            return False
        return True
    '''
	Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

	Parameters:
	col is the index of the column we are checking
	num is the value we are looking for in the column
	
	Return: boolean
    '''
    #KAYLEE BRIGGS DID THIS AND IT MIGHT NOT WORK, NEED TO TRY
    def valid_in_col(self, col, num):
        for i in range(0, 9):
            if num == int(self.board[i][col]):
                return False       
        return True


    '''
	Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
	num is the value we are looking for in the box

	Return: boolean
    '''
    def valid_in_box(self, row_start, col_start, num):
        box = []
        for i in range(3):
            for j in range(3):
                box.append(self.board[i + row_start][j + col_start])
        if num in box:
            return False
        return True
    
    '''
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

	Parameters:
	row and col are the row index and col index of the cell to check in the board
	num is the value to test if it is safe to enter in this cell

	Return: boolean
    '''
    #THERE IS SOMETHING WRONG HERE, NEED TO FIND OUT HOW TO GET ROW START AND COL START VALUES, WHY ARE FUNCTIONS UNDEFINED?
    def is_valid(self, row, col, num):
        if self.valid_in_row(row, num):
            if self.valid_in_col(col, num): 
                if col % 3 != 0:
                    col = col - col % 3
                if row % 3 != 0:
                    row = row - row % 3
                if self.valid_in_box(row, col, num):
                    return True
        return False


    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''
    # finished!
    def fill_box(self, row_start, col_start):
        box_values = random.sample(range(9), 9)
        box_values = [x + 1 for x in box_values]
        for i in range(3):
            for j in range(3):
                self.board[row_start + i][col_start + j] = box_values[i * 3 + j]
        
    
    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''
    # this might be working, fill box is likely the problem
    def fill_diagonal(self):
        for i in range(0, int(self.row_length), int(self.box_length)):
            self.fill_box(i, i)
        

    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
	
	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''
    def fill_values(self):
        self.fill_diagonal()
        print('Diagonal filled')
        self.fill_remaining(0, self.box_length)
        print('Remaining filled')


    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''
    def remove_cells(self):
        while self.removed_cells > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                self.removed_cells -= 1
        

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''
# stupid function:
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board


'''Cell (Recommended)  
This class represents a single cell in the Sudoku board. There are 81 Cells in a Board.'''
class Cell:
    def __init__(self, value, row, col, display):  
        #Constructor for the Cell class   
        self.value = value
        self.row = row
        self.col = col
        self.display = display
        self.selected = False
        self.sketched_value = 0 
       
    
  
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
        if self.selected:
            pygame.draw.rect(self.display, ("red"), (self.col * 50, self.row * 50, 50, 50), 3)
        else: #GRID
            # pygame.draw.rect(self.display, ("white"), (self.col * 75, self.row * 65, 65, 65), 1)
            
            #changed from 50 to 60
            #rectangle = pygame.Rect(self.col * 50, self.row * 50, 50, 50)
            #pygame.draw.rect(self.display, ("white"), rectangle,  2)

            block_size = 600//9
            for i in range(0, 600 - block_size, block_size):
                for j in range(0, 600 - block_size, block_size):
                    rect = pygame.Rect(i, j, block_size, block_size)
                    pygame.draw.rect(self.display, ("white"), rect, 2)
           
        if self.value != 0:
            #NUMBERS ON SCREEN
            font = pygame.font.SysFont('OptimusPrinceps.ttf', 45)
            text = font.render(str(self.value), True, ("white"))
            self.display.blit(text, (self.col * 50 + 15, self.row * 50 + 15))
        
        if self.sketched_value != 0:
            font = pygame.font.SysFont('OptimusPrinceps.ttf', 15)
            text = font.render(str(self.sketched_value), True, ("white"))
            self.display.blit(text, (self.col * 50 + 15, self.row * 50 + 15))
            
            # text = font.render(str(self.value), True, BLACK)
            # self.screen.blit(text, (self.col * CELL_WIDTH + 10, self.row * CELL_HEIGHT + 10))
        #else:
            #pygame.draw.rect(self.screen, BLACK, (self.col * CELL_WIDTH, self.row * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT), 1)
            ''''''
            
            # Get the set of keys pressed and check for user input
            pressed_keys = pygame.key.get_pressed()
        '''
        # Insert corresponding value based on user keypresses
            if pressed_keys[K_1]:
                #place value in pressed box
                pass
            if pressed_keys[K_2]:
               #place value in pressed box
                pass
            if pressed_keys[K_3:
                #place value in pressed box
                pass
            if pressed_keys[K_4]:
                #place value in pressed box
                pass
            if pressed_keys[K_5]:
                #place value in pressed box
                pass
            if pressed_keys[K_6]:
                #place value in pressed box
                pass
            if pressed_keys[K_7]:
                #place value in pressed box
                pass
            if pressed_keys[K_8]:
                #place value in pressed box
                pass
            if pressed_keys[K_9]:
                #place value in pressed box
                pass
            else:
                #what happens if they dont press a value 1-9?
        '''

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

  # FROM TICTACTOE
    #this is the bold 3x3
    # draw horizontal lines
    # for i in range(0, 4):
    #     pygame.draw.line(
    #         display,
    #         'white',
    #         (0, i * 200),
    #         (WIDTH, i * 200),
    #         9
    #     )
    # # draw vertical lines 
    # for j in range(0, 4):
    #     pygame.draw.line(
    #         display,
    #         "white",
    #         (j * 200, 0),
    #         (j * 200, 599.4),
    #         9
    #         #line(surface, color, start_pos, end_pos, width=1) -> Rect
    #     )
    #this is the 9x9
    # draw horizontal lines
    # for i in range(1, 10):
    #     pygame.draw.line(
    #         display,
    #         'white',
    #         (0, i * 66.6),
    #         (WIDTH, i * 66.6),
    #         1
    #     )
    # # draw vertical lines
    # for j in range(1, 10):
    #     pygame.draw.line(
    #         display,
    #         'white',
    #         (j * 66.6, 0),
    #         (j * 66.6, 599.4),
    #         1
    #         )
    
    # draw the cells
    for i in range(9):
            for j in range(9):
                self.cells[i][j].draw()

     # Initialize buttons
    # Initialize text first
    

  def select(self, row, col): 
  #Marks the cell at (row, col) in the board as the current selected cell.  
  #Once a cell has been selected, the user can edit its value or sketched value. 
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
    pass
   
  def sketch(self, value):
  #Sets the sketched value of the current selected cell equal to user entered value.  
  #It will be displayed at the top left corner of the cell using the draw() function. 
    pass
   
  def place_number(self, value):
  #Sets the value of the current selected cell equal to user entered value.  
  #Called when the user presses the Enter key.  
    self.board[row][col] = value
    self.board[row][col].draw(self.display)
    
    
  def reset_to_original(self):
  #Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit). 
    pass
   
  def is_full(self):
    #Returns a Boolean value indicating whether the board is full or not.  
    for i in range(9):
        for j in range(9):
            if self.board[i][j] == 0:
                return False


  def update_board(self):
    #Updates the underlying 2D board with the values in all cells. 
    pass
   
  def find_empty(self):
    #Finds an empty cell and returns its row and col as a tuple (x, y).  
    pass
   
#   this isn't correct
  def check_board(self):  
    pass

    
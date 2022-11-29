
# Reference "HOW TO MAKE A MENU SCREEN IN PYGAME!" https://www.youtube.com/watch?v=GMBqjxcKogA  

import pygame

'''When the program starts, it should display a Game Start screen. This will have buttons for the user to choose a 
difficulty between easy, medium, or hard. '''

# Setting the dimensions of the window
color = (255,255,255) 
pygame.init()
height = 850
width = 600
display = pygame.display.set_mode((width,height))

# Create caption with font
pygame.display.set_caption("Sudoku")
font = pygame.font.Font('OptimusPrinceps.ttf',55) 

text = font.render('quit' , True , color) 

# Create background
background = pygame.image.load("menubackground.jpeg")

class Button:
    def __init__(self, x_cord, y_cord, image):
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = (x_cord,y_cord)
    #draws button on screen
    def draw(self):
        display.blit(self.image, (self.rect.x, self.rect.y))



# Run the program
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #menu = text.get
        mouse = pygame.mouse.get_pos() 
        
        # Set background potential
        #display.blit(background, (0, 0))
        
        # Updates window with new background
        pygame.display.update() 
        #Menu Title "sudoku"
        suduko_text = font.render(f'Sudoku:', True, 'white')
        display.blit(suduko_text, (200, 150))
        pygame.display.update()
        
        
        
'''Create a Sudoku Board 
Difficulty  Number of empty cells  
easy   30  
medium  40  
hard   50 '''

'''Make "Game Won!" Screen with exit button if all cells are completed correctly"'''

'''Make "Game Over :(" Screen with Restart button if the board is full but not solved correctly'''

if __name__ == '__main__':
    main()
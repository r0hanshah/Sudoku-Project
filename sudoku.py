
# Reference "HOW TO MAKE A MENU SCREEN IN PYGAME!" https://www.youtube.com/watch?v=GMBqjxcKogA  
# Reference "Pygame Tutorial: How to Make a Button" https://www.youtube.com/watch?v=J5bIPtEbS0A
import pygame
import sys

'''When the program starts, it should display a Game Start screen. This will have buttons for the user to choose a 
difficulty between easy, medium, or hard. '''

# Setting the dimensions of the window
pygame.init()
HEIGHT = 800
WIDTH = 600
display = pygame.display.set_mode((WIDTH,HEIGHT))

def start_menu(display):
    start_title_font = pygame.font.Font("OptimusPrinceps.ttf", 100)
    button_font = pygame.font.Font("OptimusPrinceps.ttf", 50)

    # Color background
    display.fill("black")

    # Initialize and draw title
    title_surface = start_title_font.render("Sudoku", 0, "white")
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 200))
    display.blit(title_surface, title_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_text = button_font.render("Easy", 0, "white")
    medium_text = button_font.render("Medium", 0, "white")
    hard_text = button_font.render("Hard", 0, "white")
    quit_text = button_font.render("Quit", 0, "white")

    # Initialize button background color and text
    start_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    start_surface.fill("black")
    start_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0]+ 20, medium_text.get_size()[1]+20))
    medium_surface.fill("black")
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0]+ 20, hard_text.get_size()[1]+20))
    hard_surface.fill("black")
    hard_surface.blit(hard_text, (10, 10))
    quit_surface = pygame.Surface((quit_text.get_size()[0] + 20, quit_text.get_size()[1] + 20))
    quit_surface.fill("black")
    quit_surface.blit(quit_text, (10, 10))

    # Initialize button rectangle
    start_rectangle = start_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 -50))

    medium_rectangle = medium_surface.get_rect(
        center = (WIDTH//2, HEIGHT//2 + 50)
    )
    hard_rectangle = hard_surface.get_rect(
        center = (WIDTH//2, HEIGHT//2 + 150)
    )

    quit_rectangle = quit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 250))

    # Draw buttons
    display.blit(start_surface, start_rectangle)
    display.blit(medium_surface, medium_rectangle)
    display.blit(hard_surface, hard_rectangle)
    display.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rectangle.collidepoint(event.pos):
                    # Checks if mouse is on start button
                    return  # If the mouse is on the start button, we can return to main
                elif quit_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exit the program
                    sys.exit()
        pygame.display.update()

# Create caption with font
pygame.display.set_caption("Sudoku")
font = pygame.font.Font('OptimusPrinceps.ttf',55) 


#suduko_text = font.render(f'Sudoku:', True, 'white')

# Updates window with new background
pygame.display.update() 
#Menu Title "sudoku"
#display.blit(suduko_text, (200, 150))

class Button:
    def __init__(self, x_cord, y_cord, image, text_input):
        self.image = image
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.text_input = text_input
        self.text = pygame.font.Font("OptimusPrinceps.ttf", 40).render(self.text_input, True, "white")
        if image == None:
            self.image = self.text
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_cord,y_cord)
        self.button_clicked = False
        self.text_rect = self.text.get_rect(center=(self.x_cord, self.y_cord))
    #draws image on button on screen (might need to run display through this idk)
    def draw_image(self):
        #gets position of mouse
        mouse = pygame.mouse.get_pos() 
        if self.rect.collidepoint(mouse):
            #left mouse click
            if pygame.mouseget_pressed()[0] == 1 and self.button_clicked == False:
                print('clicked')
                self.button_clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.button_clicked = False 


        display.blit(self.image, (self.rect.x, self.rect.y))

    #draws text on button on screen (hope this works)
    def draw_text(self,display):
        #display.blit(self.text, (self.rect.x, self.rect.y))
        mouse = pygame.mouse.get_pos()
        
        if self.text_rect.collidepoint(mouse):
            #left mouse click
            if pygame.mouse.get_pressed()[0] == 1 and self.button_clicked == False:
                self.button_clicked = True
                display.fill('black')

                return True
            #no mouse click
        if pygame.mouse.get_pressed()[0] == 0:
            self.button_clicked = False 
                

        display.blit(self.text, self.text_rect) #^ this might do the same thing
        
# Run the program
def main():
    running = True
    
    #creating easy button
    #button = Button(100, 100, None, "Easy")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #menu = text.get
        
        
        # Set background potential
        #display.blit(background, (0, 0))
        
        # Updates window with new background
        pygame.display.update() 
        #Menu Title "sudoku"
        #display.blit(suduko_text, (200, 150))

        
        #if button.draw_text(display):
            #INSERT WHAT PRESSING EASY BUTTON DOES
            #display.fill("black")
            #pygame.display.update()
        start_menu(display)
        #pygame.display.update()
        
        
        
'''Create a Sudoku Board 
Difficulty  Number of empty cells  
easy   30  
medium  40  
hard   50 '''

'''Make "Game Won!" Screen with exit button if all cells are completed correctly"'''

'''Make "Game Over :(" Screen with Restart button if the board is full but not solved correctly'''

if __name__ == '__main__':
    main()


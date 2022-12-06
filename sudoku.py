# Reference "HOW TO MAKE A MENU SCREEN IN PYGAME!" https://www.youtube.com/watch?v=GMBqjxcKogA  
# Reference "Pygame Tutorial: How to Make a Button" https://www.youtube.com/watch?v=J5bIPtEbS0A
import pygame
import sys
from sudoku_generator import Board
from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku

'''When the program starts, it should display a Game Start screen. This will have buttons for the user to choose a 
difficulty between easy, medium, or hard. '''
# Setting the dimensions of the window

HEIGHT = 800
WIDTH = 600

sudoku_generator = SudokuGenerator(9,0)

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
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill("black")
    easy_surface.blit(easy_text, (10, 10))
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
    easy_rectangle = easy_surface.get_rect(
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
    display.blit(easy_surface, easy_rectangle)
    display.blit(medium_surface, medium_rectangle)
    display.blit(hard_surface, hard_rectangle)
    display.blit(quit_surface, quit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    difficulty = 30
                    # Checks if mouse is on start button
                    return difficulty # If the mouse is on the start button, we can return to main
                if medium_rectangle.collidepoint(event.pos):
                    difficulty = 40
                    # Checks if mouse is on start button
                    return difficulty
                if hard_rectangle.collidepoint(event.pos):
                    difficulty = 50
                    # Checks if mouse is on start button
                    return difficulty
                elif quit_rectangle.collidepoint(event.pos):
                    # If the mouse is on the quit button, exit the program
                    sys.exit()
        pygame.display.update()



def end_game_lost(display):
    end_title_font = pygame.font.Font("OptimusPrinceps.ttf", 100)
    button_font = pygame.font.Font("OptimusPrinceps.ttf", 50)
     # Color background
    display.fill("black")

    # Initialize and draw title
    title_surface = end_title_font.render("You Lost", 0, "red")
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2-100))
    display.blit(title_surface, title_rectangle)

    #RESTART BUTTON
    
    restart_text = button_font.render("Restart", 0, "white")
    restart_surface = pygame.Surface((restart_text.get_size()[0]+ 20, restart_text.get_size()[1]+20))
    restart_surface.fill("black")
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(center = (300, 600))
    display.blit(restart_text, restart_rectangle)
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    
                    # Checks if mouse is on start button
                    return  # If the mouse is on the reset button, we can return to main add code to actually do restart
                
        pygame.display.update()


def end_game_win(display):
    end_title_font = pygame.font.Font("OptimusPrinceps.ttf", 100)
    button_font = pygame.font.Font("OptimusPrinceps.ttf", 50)
     # Color background
    display.fill("black")

    # Initialize and draw title
    title_surface = end_title_font.render("You Won", 0, "white")
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2-100))
    display.blit(title_surface, title_rectangle)

    #EXIT BUTTON
    exit_text = button_font.render("Exit", 0, "white")
    exit_surface = pygame.Surface((exit_text.get_size()[0]+ 20, exit_text.get_size()[1]+20))
    exit_surface.fill("black")
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(center = (22, 600))
    display.blit(exit_text, exit_rectangle)
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos): 
                    sys.exit()
        pygame.display.update()
#Old Button Class
""" class Button:
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
         """
# Run the program
def main():
    # debugging stuff
    if sys.argv[len(sys.argv) - 1] == '-d':
        def debug_menu():
            func_dict = {
                'print_board':sudoku_generator.print_board, 'fill_values':sudoku_generator.fill_values, 'remove_cells':sudoku_generator.remove_cells
                }
            
            user_input = input('Enter a function to run: ')
            if user_input in ['exit', 'quit']:
                quit()
            else:
                func_dict[user_input]()
            debug_menu()
        
        print('=====================')
        print('Debugging')
        print('=====================')
        debug_menu()
        

        
    # actual program (not debugging)
    else:
        
        pygame.init()
        display = pygame.display.set_mode((WIDTH,HEIGHT))
        running = True
        pygame.display.set_caption("Sudoku")
        
        #creating easy button
        #button = Button(100, 100, None, "Easy")
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            #menu = text.get
            
        
        # Updates window with new background
            pygame.display.update() 
            difficulty = start_menu(display)
            board = Board(WIDTH, HEIGHT, display, difficulty)
            display.fill("black")
            #GAME SCREEN
            # generate_sudoku(9, difficulty)
            board.draw(display)
            # print("Finished board drawing")
            button_font = pygame.font.Font("OptimusPrinceps.ttf", 30)
            reset_text = button_font.render("Reset", 0, "white")
            restart_text = button_font.render("Restart", 0, "white")
            exit_text = button_font.render("Exit", 0, "white")

            # Initialize button background color and text
            reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
            reset_surface.fill("black")
            reset_surface.blit(reset_text, (10, 10))
            
            restart_surface = pygame.Surface((restart_text.get_size()[0]+ 20, restart_text.get_size()[1]+20))
            restart_surface.fill("black")
            restart_surface.blit(restart_text, (10, 10))

            exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
            exit_surface.fill("black")
            exit_surface.blit(exit_text, (10, 10))

            # Initialize button rectangle, positioning 
            reset_rectangle = reset_surface.get_rect(
                center=(99.9, 700)
            )
            restart_rectangle = restart_surface.get_rect(
                center = (299.7, 710)
            )
            exit_rectangle = exit_surface.get_rect(
                center = (499.5, 700)
            )

            # Draw buttons
            display.blit(restart_text, restart_rectangle)
            display.blit(reset_surface, reset_rectangle)
            display.blit(exit_surface, exit_rectangle)

    
            # print("Hello")
            game = True
            while game:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if reset_rectangle.collidepoint(event.pos):
                            # Checks if mouse is on start button
                            return  # If the mouse is on the reset button, we can return to main
                        elif exit_rectangle.collidepoint(event.pos):
                            # If the mouse is on the exit button, exit the program
                            sys.exit()
                    if event.type == pygame.QUIT:
                        game = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        clicked = board.click(pos[0], pos[1])
                        if clicked:
                            board.select(clicked[0], clicked[1])
                            board.draw(display)

                            #CAUSING ISSUE BOARD NOT BEING PRINTED
                            # if event.type == pygame.KEYDOWN:
                            #     if pygame.K_KP0 <= event.key <= pygame.K_KP9:
                            #         print(event.key)
                            #         board.sketch(event.key)
                            # if event.type == pygame.K_RETURN:
                                
                            #     board.place_number()
                pygame.display.update()


            #END GAME SCREEN
            # end_game_lost(display)

            #pygame.display.update()
        
        
        

'''Make "Game Won!" Screen with exit button if all cells are completed correctly"'''

'''Make "Game Over :(" Screen with Restart button if the board is full but not solved correctly'''

if __name__ == '__main__':
    main()


"""
main.py

This is the heartbeat of the game. If you want to play, this is the 
file you run. It turns on the game engine, sets up the window, and 
runs the infinite loop that keeps the game alive until you close it.
"""
import pygame
import sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        # Turns on the Pygame engine
        pygame.init()
        
        # Creates the game window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Fireboy & Watergirl Clone")
        
        # Sets up a clock to keep the game running at a smooth speed
        self.clock = pygame.time.Clock()
        
        # Loads our first stage
        self.level = Level('levels_data.txt')  # FIX: filename was wrong in original

    def run(self):
        """
        The continuous loop that keeps the game from immediately closing. 
        It updates everything 60 times a second.
        """
        while True:
            # 1. Listen for the player clicking the 'X' to close the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # 2. Wipe the screen clean with our background color
            self.screen.fill(BG_COLOR)
            
            # 3. Tell the level manager to draw the walls and move the players
            self.level.run()

            # 4. Show the new updated picture to the player
            pygame.display.update()
            
            # 5. Wait a tiny fraction of a second to keep a steady 60 FPS
            self.clock.tick(FPS)

if __name__ == '__main__':
    # This actually starts the game when you run the file
    game = Game()
    game.run()

"""
What This File Does
This is the master switch (the core engine and game loop). 
It creates the window you actually look at. 
Inside the run function is a while True loop—an infinite cycle that listens for inputs, 
updates the math, and redraws the picture 60 times every single second to create the illusion of smooth movement.

WHAT TO ADD NEXT

CREATE A "STATE MANAGER" THAT ALLOWS THIS FILE TO SWITCH BETWEEN SHOWING A 'MAIN MENU' SCREEN, THE 'PLAYING' SCREEN, AND A 'GAME OVER' SCREEN.

ADD A TIMER OR A SCORE TRACKER TO THE TOP OF THE SCREEN DURING THE GAMEPLAY STATE.

ADD BACKGROUND MUSIC THAT PLAYS AS SOON AS THE Game CLASS IS INITIALIZED.
"""
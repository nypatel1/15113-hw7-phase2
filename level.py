"""
level.py

This file is the stage builder. It reads the blueprint (level_data.txt) 
and translates those typed letters into actual, solid game pieces that 
can be drawn on the screen and interacted with.
"""
import pygame
from settings import *
from player import Fireboy, Watergirl

class Level:
    def __init__(self, filepath):
        # Grabs the main game window so we can draw on it
        self.display_surface = pygame.display.get_surface()
        
        # Lists to hold our game objects
        self.tiles = []
        self.fireboy = None
        self.watergirl = None
        
        # Starts the building process
        self.load_level(filepath)

    def load_level(self, filepath):
        """
        Reads the text file line by line and letter by letter. 
        It calculates the exact math (X and Y coordinates) for where 
        to put a wall or a player based on where the letter is in the text.
        """
        with open(filepath, 'r') as file:
            layout = file.readlines()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row.strip()):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                
                if cell == 'X':
                    # Creates a physical rectangle for the wall
                    wall_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                    self.tiles.append(wall_rect)
                elif cell == 'F':
                    # Drops Fireboy into the world
                    self.fireboy = Fireboy(x, y)
                elif cell == 'W':
                    # Drops Watergirl into the world
                    self.watergirl = Watergirl(x, y)

    def run(self):
        """
        The stage manager. This runs 60 times a second to draw the walls 
        and tell the players to update their movements.
        """
        # Paint the walls on the screen
        for tile in self.tiles:
            pygame.draw.rect(self.display_surface, WALL_COLOR, tile)

        # Update the math for the players and paint them on the screen
        if self.fireboy and self.watergirl:
            self.fireboy.handle_input()
            self.watergirl.handle_input()
            
            self.fireboy.update(self.tiles)
            self.watergirl.update(self.tiles)

            self.display_surface.blit(self.fireboy.image, self.fireboy.rect)
            self.display_surface.blit(self.watergirl.image, self.watergirl.rect)

"""
What This File Does
This file does the heavy lifting to turn text into a playable space (parses the map and manages the level state). 
The load_level function is the most important part: it looks at row 1, column 1 of your text file. 
If it sees an 'X', it creates a 40x40 pixel grey box at the top left of the screen. 
It repeats this for every single letter until the whole stage is built. 
The run function just makes sure everything stays visible on the screen.

WHAT TO ADD NEXT

UPDATE THE load_level FUNCTION TO RECOGNIZE THE NEW HAZARD LETTERS YOU ADDED TO THE TEXT FILE (E.G., elif cell == 'L': create_lava()).

CREATE SEPARATE LISTS FOR DIFFERENT TYPES OF BLOCKS (E.G., self.hazards = [], self.buttons = []) SO THE PLAYERS CAN INTERACT WITH THEM DIFFERENTLY THAN NORMAL WALLS.

ADD LOGIC TO CHECK IF BOTH PLAYERS ARE TOUCHING THEIR RESPECTIVE EXIT DOORS, AND IF SO, CLEAR THE CURRENT STAGE AND LOAD THE NEXT TEXT FILE.
"""
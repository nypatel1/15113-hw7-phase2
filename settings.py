"""
settings.py

This file acts as the master control panel for the game. 
It stores all the global constants and configuration variables. 
Whenever a number or color needs to be used in multiple files 
(like the size of a grid tile or the strength of gravity), 
it should be defined here. This prevents "magic numbers" from 
cluttering the logic in other files.
"""

# --- Screen Dimensions & Performance ---
# These control the size of the game window and how fast it runs.
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60 # Frames Per Second: Caps the game speed so it runs consistently on all computers.

# --- Physics and Grid Setup ---
# TILE_SIZE is the foundation of the game's grid map. Every wall, hazard, 
# and character will base their size on this number (e.g., 40x40 pixels).
TILE_SIZE = 40 

# Movement physics. These control how the characters feel to play.
GRAVITY = 0.5       # How fast players are pulled downward every frame.
PLAYER_SPEED = 5    # How fast players move left and right.
JUMP_FORCE = -10    # Negative value because in Pygame, the Y-axis goes DOWN. Jumping moves UP (towards 0).

# --- Colors (RGB Format) ---
# Centralized color palette using standard Red, Green, Blue values (0-255).
BG_COLOR = (30, 30, 30)       # Dark grey background
FIRE_COLOR = (220, 50, 20)    # Orange/Red for Fireboy
WATER_COLOR = (20, 100, 220)  # Blue for Watergirl
WALL_COLOR = (100, 100, 100)  # Standard grey for solid ground/walls

"""
WHAT TO ADD NEXT

ADD COLORS FOR THE HAZARDS (E.G., LAVA_COLOR = (255, 0, 0), WATER_HAZARD_COLOR = (0, 0, 255), POISON_COLOR = (0, 255, 0)).

ADD COLORS FOR INTERACTABLE OBJECTS (E.G., BUTTON_COLOR, DOOR_COLOR, GEM_COLORS).

ADD FONTS AND TEXT COLORS ONCE THE UI AND MAIN MENU ARE BEING BUILT (E.G., TEXT_COLOR = (255, 255, 255)).

IF THE GAME GETS MORE COMPLEX, ADD VARIABLES FOR TERMINAL VELOCITY (MAX FALLING SPEED) OR FRICTION SO THE PLAYERS DON'T SLIDE ON THE GROUND.
"""
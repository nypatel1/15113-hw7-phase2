# HOMEWORK #7
# Fireboy & Watergirl

## Overview
These are the foundations for a single keyboard game Fireboy and Watergirl built in Pygame. The game uses a text to load levels and an Object-Oriented structure for the entities.

## Setup Instructions
1. Ensure Python 3.x is installed.
2. Install Pygame: `pip install pygame`
3. Run the game: `python main.py`

## Project Architecture
* `main.py`: The main file that starts the game and keeps it running continuously (the core engine and game loop)

* `settings.py`: The file where you store all the basic rules and numbers that don't change (global constants like FPS, colors, and physics variables)

* `level.py`: The file that reads the visual blueprint of the map and turns it into solid game objects and character starting positions 
(parses level_data.txt to generate solid walls and spawn players)

* `player.py`: The file containing the general rules for how characters fall and move, along with the specific keyboard controls for each character 
(contains the base Player physics class and the inherited Fireboy / Watergirl classes for specific inputs)

* `level_data.txt`: The blueprint of the level drawn out using simple keyboard characters (the text-based grid map)

## 🚨 Current State & Master TODO List 🚨
The foundations are complete. The next developer needs to implement the following core mechanics:

* [ ] **Physics:** Make sure the characters stand on floors and bump into walls instead of falling right through them 
(implement Axis-Aligned Bounding Box (AABB) collision detection in player.py so characters do not fall through X blocks)

* [ ] **Hazards:** Create dangerous areas on the map and write the rules for who survives what, like Fireboy surviving lava but dying in water 
(add new tile identifiers to level_data.txt, e.g., 'L' for Lava, 'W' for Water, and program the kill/survival logic for each character)

* [ ] **Interactables:** Build puzzle pieces that the players can use, like blocks to push around or switches to open paths 
(create a system for pushable blocks, buttons, and doors)

* [ ] **UI & Flow:** Create the screens players see outside the actual gameplay (start screen) and make the game load the next stage when both players win (build a main menu, a rules/objective display, and level transition logic when both players reach their exit doors)

## levels_data.txt documentation
What The File Does
This is the visual blueprint for your game stage (the text-based grid map). Instead of using a complicated level editor, you just type out the level using your keyboard. Every letter or symbol represents a 40x40 pixel block on the screen.

X: A solid wall or floor.

F: Where Fireboy starts the level.

W: Where Watergirl starts the level.

.: Empty air (background).

WHAT TO ADD NEXT

ADD NEW LETTERS TO REPRESENT DANGEROUS POOLS (E.G., TYPE 'L' FOR LAVA POOLS AND 'P' FOR WATER POOLS).

ADD LETTERS FOR PUZZLE PIECES (E.G., 'B' FOR A BUTTON, 'D' FOR A DOOR).

CREATE MULTIPLE FILES FOR DIFFERENT STAGES (E.G., level_2.txt, level_3.txt) ONCE THE GAME CAN TRANSITION BETWEEN THEM.
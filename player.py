"""
player.py

This file creates the actors of the game. It defines the basic physical 
rules that apply to everyone (like gravity pulling you down), and then 
it creates specific rules for Fireboy and Watergirl (like which keys 
they listen to).
"""
import pygame
from settings import *


class Player:
    def __init__(self, x, y, color):
        # Creates a solid block for the character's body
        self.image = pygame.Surface((TILE_SIZE * 0.8, TILE_SIZE * 0.8))
        self.image.fill(color)

        # A mathematical box that tracks exactly where the player is
        self.rect = self.image.get_rect(topleft=(x, y))

        # velocity_x is set each frame by handle_input() based on keys held
        # velocity_y accumulates over time as gravity pulls the player down
        self.velocity_x = 0
        self.velocity_y = 0
        self.is_grounded = False  # True only when standing on a solid tile

    # ------------------------------------------------------------------
    # HORIZONTAL COLLISION
    # ------------------------------------------------------------------
    def _move_x_and_collide(self, tiles):
        """
        Step 1 of AABB collision: move the player left or right, then
        check every tile. If we are now overlapping one, push the player
        back out to the tile edge and stop horizontal movement.

        Why do X and Y separately?
        If we moved both at once and then corrected, the game couldn't
        tell which wall was hit — the player might slide up a wall instead
        of landing on the floor. Keeping the axes separate fixes that.
        """
        self.rect.x += self.velocity_x  # Move horizontally first

        for tile in tiles:
            if self.rect.colliderect(tile):
                if self.velocity_x > 0:
                    # Moving right: our right edge entered the tile's left edge.
                    # Push our right side flush with the tile's left side.
                    self.rect.right = tile.left
                elif self.velocity_x < 0:
                    # Moving left: our left edge entered the tile's right edge.
                    # Push our left side flush with the tile's right side.
                    self.rect.left = tile.right
                self.velocity_x = 0  # Stop sliding into the wall

    # ------------------------------------------------------------------
    # VERTICAL COLLISION
    # ------------------------------------------------------------------
    def _move_y_and_collide(self, tiles):
        """
        Step 2 of AABB collision: apply gravity and move the player up or
        down, then check every tile. If overlapping, push the player out
        and update is_grounded so jumping knows it can fire.
        """
        self.velocity_y += GRAVITY      # Gravity adds a little more downward pull each frame
        self.rect.y += self.velocity_y  # Move vertically

        self.is_grounded = False  # Assume we are airborne until a floor tile proves otherwise

        for tile in tiles:
            if self.rect.colliderect(tile):
                if self.velocity_y > 0:
                    # Falling down: our bottom entered the tile's top surface.
                    # Land: push our bottom flush with the tile's top.
                    self.rect.bottom = tile.top
                    self.is_grounded = True  # We are now standing on something solid
                elif self.velocity_y < 0:
                    # Moving up (jumping): our top hit the underside of a tile.
                    # Bump head: push our top flush with the tile's bottom.
                    self.rect.top = tile.bottom
                self.velocity_y = 0  # Stop vertical movement after any surface contact

    # ------------------------------------------------------------------
    # MAIN UPDATE — called every frame from level.py
    # ------------------------------------------------------------------
    def update(self, tiles):
        """
        Runs every frame. The order here is important:
          1. Resolve horizontal movement and collisions first
          2. Then resolve vertical movement (gravity) and collisions
        Doing X before Y prevents corner-clipping glitches where a player
        could pass through a tile corner diagonally.
        """
        self._move_x_and_collide(tiles)
        self._move_y_and_collide(tiles)


# ----------------------------------------------------------------------
# FIREBOY — Arrow Keys
# ----------------------------------------------------------------------
class Fireboy(Player):
    """
    The red character. Controlled with the Arrow Keys.
      LEFT / RIGHT  -> move
      UP            -> jump (only when standing on the ground)
    """
    def __init__(self, x, y):
        super().__init__(x, y, FIRE_COLOR)

    def handle_input(self):
        """
        Read which arrow keys are held and set velocity_x for this frame.
        Jumping sets velocity_y to a large negative number (upward in pygame).
        handle_input() is called BEFORE update() every frame so the
        velocity values are fresh when the collision math runs.
        """
        keys = pygame.key.get_pressed()

        # Reset horizontal velocity each frame so the player stops
        # immediately when no key is held (no sliding)
        self.velocity_x = 0

        if keys[pygame.K_LEFT]:
            self.velocity_x = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.velocity_x = PLAYER_SPEED

        # Jump only when touching the ground — prevents double-jumping
        if keys[pygame.K_UP] and self.is_grounded:
            self.velocity_y = JUMP_FORCE


# ----------------------------------------------------------------------
# WATERGIRL — WASD Keys
# ----------------------------------------------------------------------
class Watergirl(Player):
    """
    The blue character. Controlled with WASD.
      A / D  -> move left / right
      W      -> jump (only when standing on the ground)

    This class was missing entirely from the original file — added here.
    It mirrors Fireboy exactly but listens to WASD instead of arrow keys.
    """
    def __init__(self, x, y):
        super().__init__(x, y, WATER_COLOR)

    def handle_input(self):
        """
        Same logic as Fireboy's handle_input() but listening to
        the W, A, D keys instead of the arrow keys.
        """
        keys = pygame.key.get_pressed()

        self.velocity_x = 0  # Stop horizontal movement if no key is held

        if keys[pygame.K_a]:
            self.velocity_x = -PLAYER_SPEED
        if keys[pygame.K_d]:
            self.velocity_x = PLAYER_SPEED

        if keys[pygame.K_w] and self.is_grounded:
            self.velocity_y = JUMP_FORCE


"""
What This File Does
This file handles how characters move and fall (the base Player physics class 
and the inherited Fireboy / Watergirl classes). 
Because both characters are basically the same shape and obey the same gravity, 
the base Player code handles the falling math so we don't have to write it twice. 
Then, Fireboy and Watergirl just add their specific colors and keyboard controls 
on top of those basic rules.

"""
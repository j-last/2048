from random import randint
import pygame

from tile import Tile

class Board:
    """
    Class for the board / grid of the game.
    Contains grid data and tile objects.
    Allows for movemnt of tiles within the grid as well.
    """
    def __init__(self):
        self.grid = [[None for i in range(4)] for i in range(4)]

    def add_tile_to_grid(self):
        """
        Adds a new tile to a random blank location in the grid
        """
        valid_location = False
        while not valid_location:
            y_coord = randint(0, 3)
            x_coord = randint(0, 3)
            if self.grid[y_coord][x_coord] is None:
                valid_location = True
        
        self.grid[y_coord][x_coord] = Tile(2)

    def move_tiles_up(self):
        """
        Slides all tiles in the grid to the upmost location avaliable in their column.
        Also merges tiles of the same value if necessary.
        """
        for y_coord, row in enumerate(self.grid):
            if y_coord == 0: continue # top row can't be moved upwards

            for x_coord, tile in enumerate(row):
                if tile is None: continue # blank spaces don't move

                for i in range(1, 4): # maximum moved up is 3
                    if y_coord - i != 0 and self.grid[y_coord - i][x_coord] is None: continue

                    tile_above = self.grid[y_coord - i][x_coord]
                    self.grid[y_coord][x_coord] = None
                    if y_coord - i == 0 and tile_above is None: # if top row free
                        self.grid[0][x_coord] = tile
                    elif tile_above.get_value() == tile.get_value(): # if next tile above is same value then merge
                        tile_above.double_value()
                    else: # if next tile above is different value then place 1 below
                        self.grid[y_coord - i + 1][x_coord] = tile
                    break


    def move_tiles_down(self):
        """
        Slides all tiles in the grid to the bottom-most location avaliable in their column.
        Also merges tiles of the same value if necessary.
        """
        for anti_y_coord, row in enumerate(reversed(self.grid)):
            y_coord = 3 - anti_y_coord
            if y_coord == 3: continue # bottom row can't be moved down
            for x_coord, tile in enumerate(row):
                if tile is None: continue # iterate until a tile is found

                for i in range(1, 4):
                    if y_coord + i != 3 and self.grid[y_coord + i][x_coord] is None: continue # iterates to find next tile below

                    tile_below = self.grid[y_coord + i][x_coord]
                    self.grid[y_coord][x_coord] = None # sets current location to blank

                    if y_coord + i == 3 and tile_below is None: # if no tile below current tile, move tile to bottom row
                        self.grid[3][x_coord] = tile

                    elif tile_below.get_value() == tile.get_value(): # if next tile below matches value, merge them
                        tile_below.double_value()

                    else:
                        self.grid[y_coord + i - 1][x_coord] = tile # if next tile below is different value, place in the location above

                    break



    def move_tiles_left(self):
        """
        Slides all tiles in the grid to the leftmost location avaliable in their column.
        Also merges tiles of the same value if necessary.
        """
        for y_coord, row in enumerate(self.grid):
            for x_coord, tile in enumerate(row):
                if tile is None or x_coord == 0: continue # iterate until a tile is found

                for i in range(1, 4): # maximum can be moved is 3
                    if x_coord - i != 0 and self.grid[y_coord][x_coord - i] is None: continue # iterate until a tile (or no tile) to the left is found

                    next_tile_left = self.grid[y_coord][x_coord - i]
                    self.grid[y_coord][x_coord] = None # changes current tile location to a blank

                    if x_coord - i == 0 and next_tile_left is None: # if no tile to the left, then move to the far left
                        self.grid[y_coord][x_coord - i] = tile

                    elif next_tile_left.get_value() == tile.get_value(): # if next tile left is same value then merge
                        next_tile_left.double_value()

                    else: # if next tile left is not the same value, then place tile 1 to the right of it
                        self.grid[y_coord][x_coord - i + 1] = tile

                    break

    def move_tiles_right(self):
        """
        Slides all tiles in the grid to the rightmost location avaliable in their column.
        Also merges tiles of the same value if necessary.
        """
        for y_coord, row in enumerate(self.grid):
            for anti_x_coord, tile in enumerate(reversed(row)):
                x_coord = 3 - anti_x_coord
                if tile is None or x_coord == 3: continue # iterate until a tile is found

                for i in range(1, 4): # maximum can be moved is 3
                    if x_coord + i != 3 and self.grid[y_coord][x_coord + i] is None: continue

                    next_tile_right = self.grid[y_coord][x_coord + i]
                    self.grid[y_coord][x_coord] = None # changes current tile location to a blank

                    if x_coord + i == 3 and next_tile_right is None: # if no tile to the right, then move to the far right
                        self.grid[y_coord][x_coord + i] = tile

                    elif next_tile_right.get_value() == tile.get_value(): # if next tile right is same value then merge
                        next_tile_right.double_value()

                    else: # if next tile left is not the same value, then place tile 1 to the left of it
                        self.grid[y_coord][x_coord + i - 1] = tile

                    break

    def draw_board(self, WIDTH, HEIGHT, SCREEN):
        """
        Draws the grid for the game on the screen (but not the tiles)
        
        Args:
            WIDTH (int): constant from main.py that contains the width of the window
            HEIGHT (int): constant from main.py that contains the height of the window
            SCREEN (pygame window): pygame window allows pygame objects to be drawn onto the screen
        """
        for i in range(5):
            varying_x_pos = i * 0.25 * WIDTH
            pygame.draw.line(SCREEN,
                             (255, 255, 255),
                             (varying_x_pos, 0),
                             (varying_x_pos, HEIGHT),
                             5)

            varying_y_pos = i * 0.25 * HEIGHT
            pygame.draw.line(SCREEN,
                             (255, 255, 255),
                             (0, varying_y_pos),
                             (WIDTH, varying_y_pos),
                             5)

    def draw_tiles(self, WIDTH, HEIGHT, SCREEN):
        """
        Draws the tiles for the game onto the grid
        
        Args:
            WIDTH (int): constant from main.py that contains the width of the window
            HEIGHT (int): constant from main.py that contains the height of the window
            SCREEN (pygame window): pygame window allows pygame objects to be drawn onto the screen
        """
        for y_coord, row in enumerate(self.grid):
            for x_coord, tile in enumerate(row):
                if tile is not None:
                    width = WIDTH / 4
                    height = HEIGHT / 4
                    x = x_coord * width
                    y = y_coord * height
                    tile.draw(x, y, width, height, SCREEN)

    def update(self, WIDTH, HEIGHT, SCREEN):
        """Contains all actions to be done on each frame of the game

        Args:
            WIDTH (int): constant from main.py that contains the width of the window
            HEIGHT (int): constant from main.py that contains the height of the window
            SCREEN (pygame window): pygame window allows pygame objects to be drawn onto the screen
        """
        self.draw_board(WIDTH, HEIGHT, SCREEN)
        self.draw_tiles(WIDTH, HEIGHT, SCREEN) 

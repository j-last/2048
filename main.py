"""Only kinda works might fix later (can press up even if none o fthe tiles can slide up -
    same for other directions))"""
import os
import sys
import time
import pygame

from board import Board

# creating a window
pygame.init()
WIDTH = 600
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) 

# game clock
CLOCK = pygame.time.Clock()

# game elements
board = Board()

def get_keyboard_input(event):
    """Gets keyboard arrow input for the game controls

    Args:
        event (pygame event): used to determine if a key has been pressed

    """
    if event.key == pygame.K_UP:
        board.move_tiles_up()
    elif event.key == pygame.K_DOWN:
        board.move_tiles_down()
    elif event.key == pygame.K_LEFT:
        board.move_tiles_left()
    elif event.key == pygame.K_RIGHT:
        board.move_tiles_right()
    else: return None

    board.add_tile_to_grid()
    return None

def game_loop():
    """Loops every frame and completes all actions for that frame
    """
    board.add_tile_to_grid()
    while True:
        # allows for exiting the window
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    get_keyboard_input(event)
        except SystemError: print("Error")
        
        SCREEN.fill((0, 0, 0)) # fills screen black
        board.update(WIDTH, HEIGHT, SCREEN)

        # end of loop update screen and limit frame rate
        pygame.display.update()
        CLOCK.tick(60)


game_loop()

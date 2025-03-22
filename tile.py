import pygame

pygame.init()

class Tile:
    """
    Contains information about each tile on the grid
    """
    def __init__(self, value):
        """
        Args:
            value (int): The numeric value the tile should hold when first created
        """
        self.value = value

    def get_value(self) -> int:
        """
        Returns: 
            int: the value of the tile
        """
        return self.value

    def double_value(self):
        """Doubles the value of the tile (after merging)"""
        self.value *= 2

    def draw(self, x, y, width, height, SCREEN):
        """Draws the tile onto the gameboard

        Args:
            x (int): x position to draw the tile
            y (int): y position to draw the tile
            width (int): width of the tile to be drawn
            height (int): height of the tile to be drawn
            SCREEN (pygame window): allows for the tile to be drawn onto the pygame window
        """
        pygame.draw.rect(SCREEN, (255, 255, 255), (x, y, width, height))
        font = pygame.font.Font(None, 60)
        text = font.render(str(self.value), True, (0, 0, 0))
        SCREEN.blit(text, (x + width / 2 - 15, y + height / 2 - 30))

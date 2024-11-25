import pygame

class Level:
    def __init__(self, brick_class, screen_width):
        """
        Initialize the Level class.

        :param brick_class: The Brick class used to create bricks.
        :param screen_width: Width of the game screen.
        :param colors: List of colors for each row of bricks.
        :param margin: Space between bricks.
        """
        self.brick_class = brick_class
        self.screen_width = screen_width
        self.margin = 5

    def create_level(self, brick_grid):
        """
        Create a level based on the provided brick grid.

        :param brick_grid: A 2D array representing the layout of bricks (1 = brick, 0 = empty).
        :return: A pygame.sprite.Group containing the bricks.
        """
        bricks = pygame.sprite.Group()
        rows = len(brick_grid)
        cols = len(brick_grid[0])
        brick_width = 70
        brick_height = 25  # Fixed height for bricks

        # Calculate horizontal padding
        total_width = cols * (brick_width + self.margin) - self.margin
        x_offset = (self.screen_width - total_width) // 2
        for row in range(rows):
            for col in range(cols):
                if brick_grid[row][col] == 1:
                    x = x_offset + col * (brick_width + self.margin)
                    y = 50 + row * (brick_height + self.margin)
                    color = (255 - row * 20, 50 + row * 30, 200)  # Different colors for each row
                    health = max(1, 4 - (row // 2) - 1) # Different health for each 2 rows max health of 3
                    brick = self.brick_class(x, y, brick_width, brick_height, color, health)
                    bricks.add(brick)

        return bricks

    def load_level(self, level_number= 0):
        """
        Loads a predefined level layout.

        :param level_number: The level number to load.
        :return: A 2D array representing the layout of bricks.
        """
        levels = [
            [
                [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
            [   
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
                [0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
            [
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
                [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            ],
        ]

        if 0 <= level_number < len(levels):
            return levels[level_number]
        else:
            raise ValueError("Invalid level number.")


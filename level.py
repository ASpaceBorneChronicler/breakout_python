import pygame
import array as arr
# 0 represents no brick, 1 represents a brick
brick_grid = [
    [1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]


# Define some colors
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)

colors = [RED, ORANGE, YELLOW, RED]


class Level:
    def __init__(self, level, brick, all_sprites_list, brick_group):
        self.level = level
        self.brick = brick
        self.all_sprites_list = all_sprites_list
        self.brick_group = brick_group
        self.level = brick_grid
        self.create_level()

    def create_level(self):
        for row in range(len(self.level)):
            for column in range(len(self.level[row])):
                if self.level[row][column] == 1:
                    brick = self.brick(colors[row], 80, 30)
                    brick.rect.x = 60 + (column * 120)
                    brick.rect.y = 60 + (row * 40)
                    self.all_sprites_list.add(brick)
                    self.brick_group.add(brick)
        

    def load_level(self):
        return self.level
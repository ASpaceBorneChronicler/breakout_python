import pygame
from random import randint

BLACK = (0, 0, 0)
 
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # Initialize the superclass (Sprite)
        """
        Initializes a Ball object with a specified color, width, and height.

        Parameters:
            color (tuple): The color of the ball as an RGB tuple.
            width (int): The width of the ball.
            height (int): The height of the ball.
        """
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball 
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        """
        Moves the ball based on its velocity.
        """
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
          
    def bounce(self):
        """
        Negates the x component of the velocity and randomizes the y component
        """
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
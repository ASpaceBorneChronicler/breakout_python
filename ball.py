import pygame
from random import randint

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, paddle, width, height):
        super().__init__()
        self.image = pygame.image.load("img/ball.png").convert_alpha()
        self.rect = self.image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        self.screen = screen
        self.paddle = paddle

        self.velocity = [randint(4, 8), randint(-8, 8)]

    def update(self, brick_group):
        """
        Moves the ball based on its velocity and handles boundary and paddle collisions.
        """
        
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Handle vertical boundary collisions
        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height():
            self.velocity[1] = -self.velocity[1]

        # Handle horizontal boundary collisions
        if self.rect.left <= 0 or self.rect.right >= self.screen.get_width():
            self.velocity[0] = -self.velocity[0]

        # Handle paddle collision
        if pygame.sprite.collide_rect(self, self.paddle):
            self.handle_paddle_collision()

        collided_bricks = pygame.sprite.spritecollide(self, brick_group, False)
        for brick in collided_bricks:
            brick.hit()
            self.bounce()

    def handle_paddle_collision(self):
        """
        Changes the velocity based on where the ball hits the paddle.
        """
        # Reverse vertical velocity
        self.velocity[1] = -abs(self.velocity[1])  # Ensure the ball moves upward

        # Add slight variation to horizontal velocity based on where it hits the paddle
        paddle_center = self.paddle.rect.centerx
        ball_center = self.rect.centerx
        offset = (ball_center - paddle_center) / (self.paddle.rect.width / 2)  # Normalize offset (-1 to 1)

        self.velocity[0] += int(offset * 4)  # Adjust horizontal velocity slightly
        self.velocity[0] = max(-8, min(8, self.velocity[0]))  # Clamp velocity to prevent excessive speed

        # Prevent velocity from becoming zero
        if abs(self.velocity[0]) < 1:
            self.velocity[0] = 1 if self.velocity[0] > 0 else -1

    def bounce(self):
        self.velocity[1] = -self.velocity[1]
        

    def reset_position(self):
        """
        Resets the ball to the center of the screen and gives it a random velocity.
        """
        self.rect.center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
        self.velocity = [randint(4, 8), randint(-8, 8)]

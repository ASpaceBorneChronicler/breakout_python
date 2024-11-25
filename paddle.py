from typing import Any
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PADDLE_VELOCITY = 15

class Paddle(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super().__init__()
        self.image = pygame.image.load("img/paddle.png")
        self.rect = self.image.get_rect(center=(x, y))

        self.screen_width = screen.get_width()
        self.velocity = PADDLE_VELOCITY # Might want to manipulate this later

    def update(self) -> None:
        keys = pygame.key.get_pressed()

        # Handle paddle movement
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += self.velocity

    def start(self,x=None , y=None):
        self.rect.x = x or self.screen_width / 2
        self.rect.y = y or self.screen_height - 50

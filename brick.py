import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(255, 0, 0), health=1):
        """
        Initialize a brick with position, size, color, and health.

        :param x: X-coordinate of the brick's top-left corner.
        :param y: Y-coordinate of the brick's top-left corner.
        :param width: Width of the brick.
        :param height: Height of the brick.
        :param color: Color of the brick.
        :param health: Number of hits the brick can take before breaking.
        """
        super().__init__()

        # Create the brick surface
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        # Set the rect for positioning
        self.rect = self.image.get_rect(topleft=(x, y))

        # Brick attributes
        self.color = color
        self.health = health
        

    def hit(self):
        """
        Reduces the brick's health by 1 and changes its color or removes it if health is zero.
        """
        self.health -= 1
        print(self.health)
        if self.health <= 0:
            self.kill()  # Remove the brick from all sprite groups
        else:
            # Darken the brick color to indicate damage
            darker_color = tuple(max(0, c - 50) for c in self.color)  # Reduce RGB values
            self.image.fill(darker_color)

    def draw(self, screen):
        """
        Draw the brick on the screen.
        """
        screen.blit(self.image, self.rect)

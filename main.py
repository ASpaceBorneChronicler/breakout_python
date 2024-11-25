#Import the pygame library
import pygame
# Import game objects
from paddle import Paddle
from ball import Ball
from brick import Brick
from level import Level

pygame.init()

BLACK = (0, 0, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_L = pygame.font.SysFont('Arial' , 36)
FONT_S = pygame.font.SysFont('Arial' , 24)
COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0)]

FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def setup(level_number=0):
    paddle_group = pygame.sprite.Group()
    paddle = Paddle(screen, int(SCREEN_WIDTH // 2), 550)
    paddle_group.add(paddle)


    # Initialize the Level
    level_manager = Level(Brick, SCREEN_WIDTH)

    # Load and create Level 1
    brick_grid = level_manager.load_level(level_number)  # Load level 0 (first level)
    brick_group = level_manager.create_level(brick_grid)


    ball_group = pygame.sprite.Group()
    ball = Ball(screen, paddle, int(SCREEN_WIDTH // 2), 550)
    ball_group.add(ball)
    return paddle_group, ball_group, brick_group

# show win message
def show_win_message():
    message = "You win level " + str(level_number + 1)
    instruction = "Press space to play level 1 again or 'esc' to quit" if level_number >= 2 else "Press space to play next level"
    text = FONT_L.render(message, True, (255, 255, 255))
    instructions = FONT_S.render(instruction, True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) - 50))
    instructions_rect = instructions.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 50))
    screen.blit(text, text_rect)
    screen.blit(instructions, instructions_rect)
    pygame.display.flip()
# Add counter

def counter_pause():
    global start, paused
    paddle_group.draw(screen)
    ball_group.draw(screen)
    brick_group.draw(screen)
    pygame.display.flip()
    counter = 3
    last_sec = pygame.time.get_ticks()
    while counter > 0:
        
        clock.tick(FPS)
        
        screen.fill(BLACK)

        paddle_group.draw(screen)
        ball_group.draw(screen)
        brick_group.draw(screen)
        
        if not paused:
            time_now = pygame.time.get_ticks()
            
            text = FONT_L.render(str(counter), True, (255, 255, 255))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) - 50))
            screen.blit(text, text_rect)

            if time_now - last_sec >= 1000:
                counter -= 1
                last_sec = time_now
        else:

            text = FONT_L.render("PAUSED", True, (255, 255, 255))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) - 50))
            screen.blit(text, text_rect)

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                paused = not paused
        pygame.display.flip()
    return 1


paddle_group, ball_group, brick_group = setup()

paused = False
start = 0
deciding = False
level_number = 0
# Game loop
running = True
while running:
    
    # Keep loop running at the right speed
    clock.tick(FPS)

    screen.fill(BLACK)
    if start == 0:        
        start = counter_pause()

    # Update paddle
    paddle_group.update() 

    # Update ball
    ball_group.update(brick_group)

    # Draw paddle
    paddle_group.draw(screen)

    # Draw ball
    ball_group.draw(screen)

    # Draw the bricks
    brick_group.draw(screen)

    # Win message
    if len(brick_group) == 0:
        deciding = True
        while deciding:
            screen.fill(BLACK)
            paddle_group.draw(screen)
            ball_group.draw(screen)
            brick_group.draw(screen)

            show_win_message()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    start = 0
                    deciding = False
                    level_number = (level_number + 1) % 3
                    paddle_group, ball_group, brick_group = setup(level_number)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start = 0
                paused = not paused

    # Update screen
    pygame.display.flip()
pygame.quit()
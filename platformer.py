import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BALL_RADIUS = 20
GRAVITY = 1
JUMP_HEIGHT = 100
JUMP_DURATION = 4
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLATFORM_SPEED = 1

# Set up some variables
x = WIDTH // 2
y = HEIGHT - BALL_RADIUS
velocity = [0, 0]
jump_ticks = 0
platforms = []

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create some platforms
for i in range(5):
    platform_x = random.randint(0, WIDTH - PLATFORM_WIDTH)
    platform_y = random.randint(0, HEIGHT - PLATFORM_HEIGHT)
    platforms.append([platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT])

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity[0] = -5
            elif event.key == pygame.K_RIGHT:
                velocity[0] = 5
            elif event.key == pygame.K_UP and jump_ticks == 0:
                velocity[1] = -math.sqrt(2 * GRAVITY * JUMP_HEIGHT)
                jump_ticks = JUMP_DURATION
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                velocity[0] = 0

    # Move the ball
    x += velocity[0]
    y += velocity[1]

    # Apply gravity
    velocity[1] += GRAVITY

    # Check for ground collision
    if y > HEIGHT - BALL_RADIUS:
        y = HEIGHT - BALL_RADIUS
        velocity[1] = 0

    # Check for jump duration
    if jump_ticks > 0:
        jump_ticks -= 1

    # Move platforms
    for i, platform in enumerate(platforms):
        if platform[0] < -PLATFORM_WIDTH:
            del platforms[i]
        else:
            platforms[i] = [platform[0] - PLATFORM_SPEED, platform[1], platform[2], platform[3]]

    # Add new platforms
    if len(platforms) < 5:
        platform_x = WIDTH
        platform_y = random.randint(0, HEIGHT - PLATFORM_HEIGHT)
        platforms.append([platform_x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT])

    # Check for platform collision
    for platform in platforms:
        if (x + BALL_RADIUS > platform[0] and x - BALL_RADIUS < platform[0] + PLATFORM_WIDTH) and (y + BALL_RADIUS > platform[1] and y - BALL_RADIUS < platform[1] + PLATFORM_HEIGHT):
            y = platform[1] - BALL_RADIUS
            velocity[1] = 0

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), BALL_RADIUS)
    for platform in platforms:
        pygame.draw.rect(screen, (0, 255, 0), (platform[0], platform[1], PLATFORM_WIDTH, PLATFORM_HEIGHT))
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
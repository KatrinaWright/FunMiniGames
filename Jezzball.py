import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
BALL_SIZE = 20
SQUARE_SIZE = 20
SPEED = 2
TRAIL_SIZE = 2

# Set up some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the rectangle
rectangle = pygame.Rect(50, 50, WIDTH - 100, HEIGHT - 100)

# Set up the ball
ball = pygame.Rect(WIDTH / 2, HEIGHT / 2, BALL_SIZE, BALL_SIZE)
ball_x_speed = SPEED
ball_y_speed = SPEED

# Set up the square
square = pygame.Rect(WIDTH / 2, (HEIGHT / 2) - (SQUARE_SIZE * 1.5), SQUARE_SIZE, SQUARE_SIZE)
square_x_speed = SPEED
square_y_speed = SPEED

# Set up the trail
trail = []

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball.x += ball_x_speed
    ball.y += ball_y_speed

    # Check for collisions with the rectangle
    if ball.left < rectangle.left or ball.right > rectangle.right:
        ball_x_speed = -ball_x_speed
    if ball.top < rectangle.top or ball.bottom > rectangle.bottom:
        ball_y_speed = -ball_y_speed

    # Check for collisions with the trail
    for t in trail:
        if ball.colliderect(t):
            trail = []
            square.x = WIDTH / 2
            square.y = (HEIGHT / 2) - (SQUARE_SIZE * 1.5)

    # Move the square
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square.x -= square_x_speed
    if keys[pygame.K_RIGHT]:
        square.x += square_x_speed
    if keys[pygame.K_UP]:
        square.y -= square_y_speed
    if keys[pygame.K_DOWN]:
        square.y += square_y_speed

    # Add a new trail point
    if square.colliderect(rectangle):
        trail.append(pygame.Rect(square.x, square.y, TRAIL_SIZE, TRAIL_SIZE))

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, rectangle)
    pygame.draw.ellipse(screen, BLUE, ball)
    pygame.draw.rect(screen, GREEN, square)
    for t in trail:
        pygame.draw.rect(screen, YELLOW, t)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
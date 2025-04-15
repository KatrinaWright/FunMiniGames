## current problem, will get stuck in obstacle if backing up


import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Set up the car
car = pygame.Rect(WIDTH / 2, HEIGHT / 2, 50, 30)
car_angle = 0
car_speed = 0

# Set up the terrain
terrain = pygame.Rect(WIDTH / 2, HEIGHT - 100, 200, 100)

# Set up the camera
camera_x = WIDTH / 2
camera_y = HEIGHT / 2

# Set up the obstacles
class Obstacle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

obstacles = [
    Obstacle(100, 100, 50, 50),
    #Obstacle(300, 200, 70, 70),
    Obstacle(500, 300, 30, 30),
]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the pressed keys
    keys = pygame.key.get_pressed()

    # Update the car's speed
    if keys[pygame.K_UP]:
        car_speed += 0.1
    if keys[pygame.K_DOWN]:
        car_speed -= 0.1

    # Update the car's angle
    if keys[pygame.K_LEFT]:
        car_angle += 5
    if keys[pygame.K_RIGHT]:
        car_angle -= 5

    # Update the car's position
    car.x += car_speed * pygame.math.Vector2(1, 0).rotate(-car_angle).x
    car.y += car_speed * pygame.math.Vector2(1, 0).rotate(-car_angle).y

    # Check for collisions with obstacles
    for obstacle in obstacles:
        if car.colliderect(obstacle.rect):
            # Move the car away from the obstacle
            if car.centerx < obstacle.rect.centerx:
                car.x -= car_speed * pygame.math.Vector2(1, 0).rotate(-car_angle).x
            if car.centery < obstacle.rect.centery:
                car.y -= car_speed * pygame.math.Vector2(1, 0).rotate(-car_angle).y
            car_speed = 0
            car_angle = 0

    # Update the camera's position
    camera_x = car.x + car.width / 2 - WIDTH / 2
    camera_y = car.y + car.height / 2 - HEIGHT / 2

    # Draw everything
    screen.fill(RED)
    pygame.draw.rect(screen, GREEN, (terrain.x - camera_x, terrain.y - camera_y, terrain.width, terrain.height))
    pygame.draw.rect(screen, BLUE, (car.x - camera_x, car.y - camera_y, car.width, car.height))
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 255, 0), (obstacle.rect.x - camera_x, obstacle.rect.y - camera_y, obstacle.rect.width, obstacle.rect.height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)
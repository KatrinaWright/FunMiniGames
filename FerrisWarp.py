import pygame
import sys
import math

# initialize Pygame
pygame.init()

# set up some constants
WIDTH = 800
HEIGHT = 600
SPEED = 0.03
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
RADIUS = 200
CABIN_SIZE = 50
CABIN_SPACING = 50
FRAMEWORK_WIDTH = 50
FRAMEWORK_HEIGHT = 200
FRAMEWORK_COLOR = (255, 0, 0)
CABIN_COLOR = (255, 255, 0)

# set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# set up the Ferris wheel
wheel = pygame.Surface((RADIUS * 2, RADIUS * 2))
pygame.draw.circle(wheel, (0, 0, 255), (RADIUS, RADIUS), RADIUS)
wheel_rect = wheel.get_rect(center=(CENTER_X, CENTER_Y))

# set up the cabins
cabins = []
for i in range(20):
    cabin = pygame.Surface((CABIN_SIZE, CABIN_SIZE))
    pygame.draw.rect(cabin, CABIN_COLOR, (0, 0, CABIN_SIZE, CABIN_SIZE))
    cabin_rect = cabin.get_rect()
    cabin_rect.center = (CENTER_X + math.cos(math.radians(i * 360 / 20)) * (RADIUS + CABIN_SIZE / 2 + CABIN_SPACING),
                         CENTER_Y + math.sin(math.radians(i * 360 / 20)) * (RADIUS + CABIN_SIZE / 2 + CABIN_SPACING))
    cabins.append(cabin)

# set up the framework
framework = pygame.Surface((FRAMEWORK_WIDTH, FRAMEWORK_HEIGHT))
pygame.draw.rect(framework, FRAMEWORK_COLOR, (0, 0, FRAMEWORK_WIDTH, FRAMEWORK_HEIGHT))
framework_rect = framework.get_rect(center=(CENTER_X, CENTER_Y))

# set up the rotation
angle = 0

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # clear the screen
    screen.fill((255, 255, 255))

    # rotate the wheel
    angle += SPEED
    if angle >= 360:
        angle = 0

    # draw the cabins
    for i, cabin in enumerate(cabins):
        cabin_rect.center = (CENTER_X + math.cos(math.radians(angle + i * 360 / 20)) * (RADIUS + CABIN_SIZE / 2 + CABIN_SPACING),
                             CENTER_Y + math.sin(math.radians(angle + i * 360 / 20)) * (RADIUS + CABIN_SIZE / 2 + CABIN_SPACING))
        screen.blit(cabin, cabin_rect)

        # draw connections to the central section of the wheel
        pygame.draw.line(screen, (0, 0, 0), cabin_rect.center, (CENTER_X, CENTER_Y), 2)

        # draw connections to the neighbors
        if i > 0:
            pygame.draw.line(screen, (0, 0, 0), cabin_rect.center, cabins[i-1].get_rect().center, 2)
        if i < len(cabins) - 1:
            pygame.draw.line(screen, (0, 0, 0), cabin_rect.center, cabins[i+1].get_rect().center, 2)

    # draw the framework
    screen.blit(framework, framework_rect)

    # update the display
    pygame.display.flip()
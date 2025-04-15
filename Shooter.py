import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH = 800
HEIGHT = 600
SPEED = 5
PROJECTILE_SPEED = 10
ENEMY_SPEED = 3

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the player
player = pygame.Rect(WIDTH / 2, HEIGHT / 2, 50, 50)
player_start_pos = (WIDTH / 2, HEIGHT / 2)
player_move_x = player_move_y = 0

# Set up the projectiles
projectiles = []

# Set up the enemies
class Enemy(pygame.Rect):
    def __init__(self):
        super().__init__(random.randint(0, WIDTH - 25), random.randint(0, HEIGHT - 25), 25, 25)
        if random.random() < 0.25:  # 25% chance of being green
            self.color = (0, 255, 0)  # Green color
            self.speed = ENEMY_SPEED / 2  # Half speed
        else:
            self.color = (255, 0, 0)  # Red color
            self.speed = ENEMY_SPEED  # Standard speed

enemies = [Enemy() for _ in range(10)]

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - player.x
            dy = mouse_y - player.y
            dist = math.hypot(dx, dy)
            dx, dy = dx / dist, dy / dist
            projectiles.append([player.x + 25, player.y + 25, dx, dy])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_move_y = -SPEED
    elif keys[pygame.K_DOWN]:
        player_move_y = SPEED
    else:
        player_move_y = 0

    if keys[pygame.K_LEFT]:
        player_move_x = -SPEED
    elif keys[pygame.K_RIGHT]:
        player_move_x = SPEED
    else:
        player_move_x = 0

    player.move_ip(player_move_x, player_move_y)

    for i, projectile in enumerate(projectiles):
        projectile[0] += projectile[2] * PROJECTILE_SPEED
        projectile[1] += projectile[3] * PROJECTILE_SPEED
        if projectile[0] < 0 or projectile[0] > WIDTH or projectile[1] < 0 or projectile[1] > HEIGHT:
            del projectiles[i]

    for i, enemy in enumerate(enemies):
        dx = player.x - enemy.x
        dy = player.y - enemy.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        enemy.move_ip(dx * enemy.speed, dy * enemy.speed)
        for j, projectile in enumerate(projectiles):
            proj_rect = pygame.Rect(projectile[0], projectile[1], 10, 10)
            if enemy.colliderect(proj_rect):
                
                del projectiles[j]
                if enemy.color == (0, 255, 0):  # If the enemy is green
                    enemy.color = (255, 0, 0)  # Turn it red
                    enemy.speed = ENEMY_SPEED  # Set its speed to standard
                else:
                    del enemies[i]
                    enemies.append(Enemy())
                break
        if player.colliderect(enemy):
            player.x, player.y = player_start_pos
            enemies = [Enemy() for _ in range(10)]

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)

    for projectile in projectiles:
        pygame.draw.rect(screen, (255, 255, 255), (projectile[0], projectile[1], 10, 10))

    for enemy in enemies:
        pygame.draw.rect(screen, enemy.color, enemy)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
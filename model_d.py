import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enemy Collision Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game variables
bullet_speed = 15
bullets = []
enemies = []
explosions = []
clock = pygame.time.Clock()

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 10)
        
    def update(self):
        self.rect.y -= bullet_speed
        return self.rect.y < 0

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Enemy:
    def __init__(self, x, y, x_speed, y_speed):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x = float(x)
        self.y = float(y)
        self.x_dir = random.choice([1, -1])
        self.health = 1  # Set initial health to 1

    def update(self):
        if self.health <= 0:
            return True
        
        self.x += self.x_speed * self.x_dir
        self.y += self.y_speed
        
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)
        
        if self.x <= 0 or self.x + self.rect.width >= WIDTH:
            self.x_dir *= -1
        
        return False

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
        if self.health > 1:
            self.draw_health_bar(screen)

    def draw_health_bar(self, screen):
        bar_width = self.rect.width
        bar_height = 5
        bar_x = self.rect.x
        bar_y = self.rect.y - 8  # Adjust the vertical position as needed
        border_color = (0, 0, 0)
        fill_color = (0, 255, 0)

        pygame.draw.rect(screen, border_color, (bar_x, bar_y, bar_width, bar_height))
        fill_width = int(bar_width * (self.health / 5))  # Assuming max health is 5
        pygame.draw.rect(screen, fill_color, (bar_x, bar_y, fill_width, bar_height))

class BigEnemy(Enemy):
    def __init__(self, x, y, x_speed, y_speed):
        super().__init__(x, y, x_speed, y_speed)
        self.health = 5  # Set the health of the big enemy to 5
        self.rect = pygame.Rect(x, y, 50, 50)  # Increase the size of the big enemy

    def draw_health_bar(self, screen):
        bar_width = self.rect.width
        bar_height = 8  # Increase the height for the big enemy
        bar_x = self.rect.x
        bar_y = self.rect.y - 12  # Adjust the vertical position as needed
        border_color = (0, 0, 0)
        fill_color = (0, 255, 0)

        pygame.draw.rect(screen, border_color, (bar_x, bar_y, bar_width, bar_height))
        fill_width = int(bar_width * (self.health / 5))
        pygame.draw.rect(screen, fill_color, (bar_x, bar_y, fill_width, bar_height))

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)
        self.draw_health_bar(screen)

# Player settings
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 60, 50, 50)
player_speed = 10

# Spawn initial enemies
def spawn_enemies():
    for _ in range(5):
        enemies.append(Enemy(random.randint(100, WIDTH - 100), random.randint(50, 300), 2, 1))
    for _ in range(2):
        enemies.append(BigEnemy(random.randint(100, WIDTH - 100), random.randint(50, 300), 1.5, 0.5))

spawn_enemies()

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.x + player.width // 2 - 2, player.y))
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += player_speed

    # Update bullets
    bullets = [b for b in bullets if not b.update()]
    
    # Update enemies
    enemies = [e for e in enemies if not e.update()]
    
    # Collision detection
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy.rect):
                enemy.health -= 1
                bullets.remove(bullet)
                if enemy.health <= 0:
                    enemies.remove(enemy)
                break
    
    # Draw player
    pygame.draw.rect(screen, (0, 0, 255), player)
    
    # Draw bullets
    for bullet in bullets:
        bullet.draw(screen)
    
    # Draw enemies
    for enemy in enemies:
        enemy.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

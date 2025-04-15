import pygame
import sys
import math

# Constants
WIDTH, HEIGHT = 800, 600
BOWL_WIDTH, BOWL_HEIGHT = 600, 200
CIRCLE_RADIUS = 20
GRAVITY = 0.5

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 2
        self.vy = 0

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), CIRCLE_RADIUS)

    def update(self, circles):
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY

        if self.y + CIRCLE_RADIUS > HEIGHT - BOWL_HEIGHT - (self.x - WIDTH / 2) ** 2 / (BOWL_WIDTH / 2) ** 2 * BOWL_HEIGHT:
            angle = math.atan((self.x - WIDTH / 2) / (BOWL_WIDTH / 2))
            self.vy = -math.cos(angle) * math.hypot(self.vx, self.vy) * 0.8
            self.vx = -math.sin(angle) * math.hypot(self.vx, self.vy) * 0.8
            self.y = HEIGHT - BOWL_HEIGHT - (self.x - WIDTH / 2) ** 2 / (BOWL_WIDTH / 2) ** 2 * BOWL_HEIGHT - CIRCLE_RADIUS
        if self.x - CIRCLE_RADIUS < WIDTH / 2 - BOWL_WIDTH / 2 or self.x + CIRCLE_RADIUS > WIDTH / 2 + BOWL_WIDTH / 2:
            self.vx = -self.vx

        for other in circles:
            if other != self:
                dx = self.x - other.x
                dy = self.y - other.y
                distance = math.hypot(dx, dy)
                if distance < 2 * CIRCLE_RADIUS:
                    angle = math.atan2(dy, dx)
                    self.vx = math.cos(angle) * math.hypot(self.vx, self.vy) * 0.8
                    self.vy = math.sin(angle) * math.hypot(self.vx, self.vy) * 0.8
                    other.vx = -math.cos(angle) * math.hypot(other.vx, other.vy) * 0.8
                    other.vy = -math.sin(angle) * math.hypot(other.vx, other.vy) * 0.8

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    circles = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                circles.append(Circle(*event.pos))

        screen.fill(WHITE)
        for x in range(int(WIDTH / 2 - BOWL_WIDTH / 2), int(WIDTH / 2 + BOWL_WIDTH / 2)):
            y = HEIGHT - BOWL_HEIGHT - (x - WIDTH / 2) ** 2 / (BOWL_WIDTH / 2) ** 2 * BOWL_HEIGHT
            pygame.draw.line(screen, (0, 0, 0), (x, y), (x, HEIGHT), 2)

        for circle in circles:
            circle.update(circles)
            circle.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
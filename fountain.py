import pygame
import math

# Window size
WIDTH, HEIGHT = 800, 600

# Droplet properties
DROPLET_SIZE = 5
DROPLET_COLOR = (0, 0, 255)
DROPLET_SPEED = 10
GRAVITY = 0.1

class Droplet:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += GRAVITY

    def draw(self, screen):
        pygame.draw.circle(screen, DROPLET_COLOR, (int(self.x), int(self.y)), DROPLET_SIZE)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    droplets = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - WIDTH / 2
        dy = mouse_y - HEIGHT
        distance = math.sqrt(dx**2 + dy**2)
        vx = dx / distance * DROPLET_SPEED
        vy = dy / distance * DROPLET_SPEED
        droplets.append(Droplet(WIDTH / 2, HEIGHT, vx, vy))

        screen.fill((0, 0, 0))

        for droplet in droplets:
            droplet.update()
            droplet.draw(screen)
            if droplet.y > HEIGHT:
                droplets.remove(droplet)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
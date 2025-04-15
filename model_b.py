import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Transfer Challenge")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 100, 100)
BLUE = (100, 150, 255)
GREEN = (100, 255, 100)
GRAY = (150, 150, 150)

# Load sound effects (optional - comment out if you don't have sound files)
try:
    pickup_sound = pygame.mixer.Sound("pickup.wav")  # You'll need to provide these sound files
    drop_sound = pygame.mixer.Sound("drop.wav")
except:
    pickup_sound = None
    drop_sound = None

# Platform class
class Platform:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 120, 25)
        self.color = BLUE

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, GRAY, self.rect, 2)  # Border

# Game objects
platforms = [
    Platform(50, 100),   # Platform 1
    Platform(250, 220),  # Platform 2
    Platform(450, 340),  # Platform 3
    Platform(650, 460),  # Platform 4
    Platform(250, 580)   # Platform 5 (final)
]
platforms[-1].color = GREEN  # Final platform is green

# Ball settings
BALL_RADIUS = 12
ball_pos = [platforms[0].rect.centerx, platforms[0].rect.top - BALL_RADIUS]
ball_on_platform = 0

# Arm settings
ARM_LENGTH = 60
ARM_WIDTH = 12
arm_pos = [platforms[0].rect.centerx, platforms[0].rect.top - ARM_LENGTH]
arm_rotation = 0
arm_holding_ball = False
arm_moving = False
arm_target_platform = 1
animation_progress = 0

# Game state
game_over = False
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def move_arm():
    global arm_pos, arm_holding_ball, ball_pos, ball_on_platform, arm_moving
    global arm_target_platform, game_over, animation_progress

    if animation_progress < 1:
        animation_progress += 0.05  # Animation speed
        current_platform = platforms[ball_on_platform]
        target_platform = platforms[arm_target_platform]

        # Smooth interpolation
        t = animation_progress
        t = t * t * (3 - 2 * t)  # Smoothstep function for natural movement
        
        arm_pos[0] = current_platform.rect.centerx + (target_platform.rect.centerx - current_platform.rect.centerx) * t
        arm_pos[1] = current_platform.rect.top - ARM_LENGTH + (target_platform.rect.top - current_platform.rect.top) * t

        if arm_holding_ball:
            ball_pos = [arm_pos[0], arm_pos[1] + ARM_LENGTH]
    else:
        # Reached target
        arm_pos = [platforms[arm_target_platform].rect.centerx, 
                  platforms[arm_target_platform].rect.top - ARM_LENGTH]
        
        if arm_holding_ball:
            # Release ball
            ball_pos = [platforms[arm_target_platform].rect.centerx, 
                       platforms[arm_target_platform].rect.top - BALL_RADIUS]
            ball_on_platform = arm_target_platform
            arm_holding_ball = False
            arm_moving = False
            animation_progress = 0
            if drop_sound:
                drop_sound.play()

            if ball_on_platform == 4:  # Final platform
                game_over = True
            else:
                arm_target_platform = ball_on_platform + 1

def reset_game():
    global ball_pos, ball_on_platform, arm_pos, arm_holding_ball, arm_moving
    global arm_target_platform, game_over, animation_progress
    
    ball_pos = [platforms[0].rect.centerx, platforms[0].rect.top - BALL_RADIUS]
    ball_on_platform = 0
    arm_pos = [platforms[0].rect.centerx, platforms[0].rect.top - ARM_LENGTH]
    arm_holding_ball = False
    arm_moving = False
    arm_target_platform = 1
    animation_progress = 0
    game_over = False

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over and not arm_moving:
                if not arm_holding_ball:
                    arm_holding_ball = True
                    arm_moving = True
                    if pickup_sound:
                        pickup_sound.play()
            elif event.key == pygame.K_r and game_over:
                reset_game()

    # Update
    if arm_moving:
        move_arm()

    # Draw
    screen.fill(BLACK)

    # Draw platforms
    for platform in platforms:
        platform.draw(screen)

    # Draw arm
    arm_end_x = arm_pos[0]
    arm_end_y = arm_pos[1] + ARM_LENGTH
    pygame.draw.line(screen, WHITE, arm_pos, (arm_end_x, arm_end_y), ARM_WIDTH)
    pygame.draw.circle(screen, GRAY, (int(arm_pos[0]), int(arm_pos[1])), 8)  # Arm base

    # Draw ball
    if not arm_holding_ball:
        pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)
        pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS, 2)  # Outline

    # Draw UI
    level_text = font.render(f"Platform: {ball_on_platform + 1}/5", True, WHITE)
    screen.blit(level_text, (10, 10))

    if game_over:
        # Overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))

        # Game over text
        game_over_text = font.render('Game Complete!', True, WHITE)
        restart_text = font.render('Press R to Restart', True, WHITE)
        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 40))
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
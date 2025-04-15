import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Transfer Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Platform settings
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 20
PLATFORM_SPACING = 120
platforms = [
    pygame.Rect(50, 100, PLATFORM_WIDTH, PLATFORM_HEIGHT),  # Platform 1
    pygame.Rect(250, 220, PLATFORM_WIDTH, PLATFORM_HEIGHT), # Platform 2
    pygame.Rect(450, 340, PLATFORM_WIDTH, PLATFORM_HEIGHT), # Platform 3
    pygame.Rect(650, 460, PLATFORM_WIDTH, PLATFORM_HEIGHT), # Platform 4
    pygame.Rect(250, 580, PLATFORM_WIDTH, PLATFORM_HEIGHT)  # Platform 5 (final)
]

# Ball settings
BALL_RADIUS = 10
ball_pos = [platforms[0].centerx, platforms[0].top - BALL_RADIUS]
ball_on_platform = 0

# Arm settings
ARM_LENGTH = 50
ARM_WIDTH = 10
arm_pos = [platforms[0].centerx, platforms[0].top - ARM_LENGTH]
arm_angle = 0
arm_holding_ball = False
arm_moving = False
arm_target_platform = 1

# Game state
game_over = False
clock = pygame.time.Clock()

def move_arm():
    global arm_pos, arm_angle, arm_holding_ball, ball_pos, ball_on_platform, arm_moving
    global arm_target_platform, game_over

    # Calculate target position (next platform)
    target_x = platforms[arm_target_platform].centerx
    target_y = platforms[arm_target_platform].top - ARM_LENGTH

    # Move arm towards target
    current_x, current_y = arm_pos
    
    # Calculate distance to target
    dx = target_x - current_x
    dy = target_y - current_y
    distance = (dx**2 + dy**2)**0.5

    # Move speed
    speed = 5
    if distance > speed:
        # Move towards target
        current_x += (dx / distance) * speed
        current_y += (dy / distance) * speed
        arm_pos = [current_x, current_y]
        
        # Update ball position if holding
        if arm_holding_ball:
            ball_pos = [current_x, current_y + ARM_LENGTH]
    else:
        # Reached target
        arm_pos = [target_x, target_y]
        if arm_holding_ball:
            # Release ball on new platform
            ball_pos = [platforms[arm_target_platform].centerx, 
                       platforms[arm_target_platform].top - BALL_RADIUS]
            ball_on_platform = arm_target_platform
            arm_holding_ball = False
            arm_moving = False
            
            # Check if reached final platform
            if ball_on_platform == 4:  # Platform 5 (index 4)
                game_over = True
            else:
                # Set next target platform
                arm_target_platform = ball_on_platform + 1

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
                    # Pick up ball
                    arm_holding_ball = True
                    arm_moving = True

    # Update
    if arm_moving:
        move_arm()

    # Draw
    screen.fill(BLACK)

    # Draw platforms
    for i, platform in enumerate(platforms):
        color = GREEN if i == 4 else BLUE  # Final platform is green
        pygame.draw.rect(screen, color, platform)

    # Draw arm
    arm_end_x = arm_pos[0] + ARM_LENGTH * 0.5  # Simple straight arm
    arm_end_y = arm_pos[1] + ARM_LENGTH
    pygame.draw.line(screen, WHITE, arm_pos, (arm_end_x, arm_end_y), ARM_WIDTH)

    # Draw ball
    if not arm_holding_ball:
        pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)

    # Draw game over message
    if game_over:
        font = pygame.font.Font(None, 74)
        text = font.render('Game Complete!', True, WHITE)
        text_rect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
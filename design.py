import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pythagorean Theorem Animation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initial lengths of the sides of the triangle
a = 100
b = 150

# Function to draw the shapes
def draw_shapes(a, b):
    # Clear the screen
    screen.fill(BLACK)
    
    # Draw the triangle
    pygame.draw.polygon(screen, WHITE, [(50, 250), (50 + a, 250), (50, 250 - b)], 2)
    
    # Draw the squares
    square_a = pygame.Rect(50, 250, a, a)
    square_b = pygame.Rect(50, 250 - b, b, b)
    square_c = pygame.Rect(50 + a, 250 - b, math.sqrt(a**2 + b**2), math.sqrt(a**2 + b**2))
    
    pygame.draw.rect(screen, RED, square_a, 2)
    pygame.draw.rect(screen, RED, square_b, 2)
    pygame.draw.rect(screen, RED, square_c, 2)

# Main loop
running = True
clock = pygame.time.Clock()

elapsed_frames = 0
max_frames = 300  # Number of frames for the animation

while running and elapsed_frames < max_frames:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the new lengths of the sides for this frame
    a_step = a / max_frames
    b_step = b / max_frames
    a_current = min(a_step * elapsed_frames, a)
    b_current = min(b_step * elapsed_frames, b)

    # Draw shapes
    draw_shapes(a_current, b_current)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

    # Increment elapsed frames
    elapsed_frames += 1

# Quit Pygame
pygame.quit()


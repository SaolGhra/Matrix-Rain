import pygame
import random

# Initialize pygame
pygame.init()
pygame.display.set_caption('Matrix')

# Screen dimensions
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Define characters and font size
characters = ["0", "1"]
font_size = 20
font = pygame.font.Font(None, font_size)

# Create a list of raindrops
raindrops = [{"x": random.randint(5, WIDTH), "y": random.randint(5, HEIGHT), "speed": random.randint(3, 5)} for _ in range(1250)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for raindrop in raindrops:
        # Move the raindrop
        raindrop["y"] += raindrop["speed"]

        # Reset the raindrop if it goes off the screen
        if raindrop["y"] > HEIGHT:
            raindrop["y"] = 0
            raindrop["x"] = random.randint(0, WIDTH)

        # Draw the raindrop
        character = random.choice(characters)
        text = font.render(character, True, GREEN)
        screen.blit(text, (raindrop["x"], raindrop["y"]))

    pygame.display.flip()
    pygame.time.delay(25)

pygame.quit()

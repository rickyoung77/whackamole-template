import pygame
import random

# Constants
GRID_WIDTH = 20
GRID_HEIGHT = 16
SQUARE_SIZE = 32
SCREEN_WIDTH = GRID_WIDTH * SQUARE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * SQUARE_SIZE

def draw_grid(screen):
    """Draws a 20x16 grid of 32x32 squares on the screen."""
    for x in range(0, SCREEN_WIDTH, SQUARE_SIZE):
        pygame.draw.line(screen, "black", (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, SQUARE_SIZE):
        pygame.draw.line(screen, "black", (0, y), (SCREEN_WIDTH, y))

def main():
    try:
        pygame.init()

        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (SQUARE_SIZE, SQUARE_SIZE))

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = pygame.time.Clock()

        mole_x, mole_y = 0, 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    clicked_square_x = mouse_x // SQUARE_SIZE
                    clicked_square_y = mouse_y // SQUARE_SIZE

                    if clicked_square_x == mole_x and clicked_square_y == mole_y:
                        mole_x = random.randint(0, GRID_WIDTH - 1)
                        mole_y = random.randint(0, GRID_HEIGHT - 1)

            screen.fill("light green")

            # Draw the grid
            draw_grid(screen)

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x * SQUARE_SIZE, mole_y * SQUARE_SIZE)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()



import pygame
from overworld_controller import OverworldController

SCREEN_WIDTH: int = 1600
SCREEN_HEIGHT: int = 900

def main():
    pygame.init()
    pygame.display.set_caption("platformer")
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    c = OverworldController(window, clock)
    
    run = True
    while run:
        run = c.game_loop()
    pygame.quit()

if __name__ == "__main__":
    main()
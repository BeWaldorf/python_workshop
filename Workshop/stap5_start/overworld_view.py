import pygame
from os.path import join

SCREEN_WIDTH: int = 1600
SCREEN_HEIGHT: int = 900

class OverworldView():
    window: pygame.Surface
    
    def __init__(self, window: pygame.Surface) -> None:
        self.window = window
        
    def draw_brackground(self, window: pygame.Surface, name: str) -> None:
        image: pygame.Surface  = pygame.image.load(join("assets", "Background", name))
        _, _, width, height = image.get_rect()
        tile_grid = []

        for column in range(SCREEN_WIDTH // width + 1):
            for row in range(SCREEN_HEIGHT // height + 1):
                coordinate = (column * width, row * height)
                tile_grid.append(coordinate)

        for tile_coord in tile_grid:
            window.blit(image, tile_coord)

        pygame.display.update()
    
    def draw_loop(self) -> None:
        pass
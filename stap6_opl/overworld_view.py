import pygame
from os.path import join
from terrain_controller import TerrainController
from trap_controller import TrapController
from player_controller import PlayerController

SCREEN_WIDTH: int = 1280
SCREEN_HEIGHT: int = 720

class OverworldView():
    window:pygame.Surface
    
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
    
    def draw_terrain(self, terrain_list:list[TerrainController]):
        for terrain in terrain_list:
            type = "PinkGoo"
            surf = terrain.obj_model.select_sprite(type)
            coords = terrain.obj_model.get_coords()
            terrain.obj_view.draw_object(surf, coords)
    
    # eerst trap en speler dan "fout laten zien" dan terrain en bg terug tekenen
    def draw_loop(self, trap:TrapController, terrain_list:list[TerrainController], bg_name: str) -> None:
        self.draw_brackground(self.window, bg_name)
        self.draw_terrain(terrain_list)
        trap.obj_view.draw_loop(trap.obj_model.get_image(), trap.obj_model.get_coords())
        pygame.display.update()
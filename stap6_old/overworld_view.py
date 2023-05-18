import pygame
from os.path import join
from overworld_object_view import OverworldObjectView
from overworld_object_controller import OverworldObjectController



class OverworldView():
    window:pygame.Surface
    
    
    def __init__(self, window: pygame.Surface) -> None:
        self.window = window
        self.draw_brackground(self.window, "Blue.png")
        
    def draw_brackground(self, window: pygame.Surface, name: str) -> None:
        image: pygame.Surface  = pygame.image.load(join("assets", "Background", name))
        _, _, width, height = image.get_rect()
        tile_grid = []
        for column in range(1000 // width + 1):
            for row in range(800 // height + 1):
                coordinate = (column * width, row * height)
                tile_grid.append(coordinate)
        for tile_coord in tile_grid:
            window.blit(image, tile_coord)
        pygame.display.update()
    
    def draw_terrain(self, window, blocks:list[OverworldObjectController]):
        for block in blocks:
            block_state = block.obj_model.get_state()
            surf = block.obj_model.select_sprite(block_state)
            _, rect = block.obj_model.get_surface_rect_tuple()
            coords = rect.topleft
            block.obj_view.draw_object(window, surf, coords)
        pygame.display.update()
    
    def draw_loop(self, window, player:OverworldObjectController, trap:OverworldObjectController = None) -> None:
        surf, rect = player.obj_model.get_surface_rect_tuple()
        player.obj_view.draw_loop(window, surf, rect)
        pygame.display.update()
    
    
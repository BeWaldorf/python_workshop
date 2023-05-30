import pygame
from terrain_controller import TerrainController
from overworld_object_controller import OverworldObjectController

class OverworldModel():
    # Global variables:
    width: int
    height: int
    window: pygame.Surface
    object_constrollers: list[OverworldObjectController] = []
    
    # Constructor:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        terrain_master  = 
        terrain_coords  = 
        self.terrain    =
        
    
    # Private methods:
    def _create_terrain(self) -> None:
        blocks = []
        # Hoe maken we het terrein?
        return blocks
    
    # Public methods:
    def set_window(self, window: pygame.Surface) -> None:
        self.window = window
    
    def logic_loop(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
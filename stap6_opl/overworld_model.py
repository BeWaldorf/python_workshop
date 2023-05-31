import pygame
from terrain_controller import TerrainController
from trap_controller import TrapController
from overworld_object_controller import OverworldObjectController
from player_controller import PlayerController

BLOCK_OFFSET = 160

class OverworldModel():
    # Global variables:
    width: int
    height: int
    window: pygame.Surface
    
    object_controllers: list[OverworldObjectController] = []
    
    FPS:int = 60
    
    # Constructor:
    def __init__(self, window, width: int, height: int) -> None:
        self.width = width
        self.height = height
        terrain_master  = TerrainController(None, None, None, None, None, True)
        terrain_coords  = terrain_master.get_terrain_coords()
        self.terrain    = self._create_terrain(window, terrain_coords)
        self.trap       = TrapController(window, width // 2, height - BLOCK_OFFSET)
        self.object_controllers.append(self.trap)
        

    
    
    # Private methods:
    def _create_terrain(self, window, coords: list[list[int]]) -> list[TerrainController]:
        blocks =  []
        for coord in coords:
            x = coord[0]
            y = coord[1]
            new_block = TerrainController(window, x, y, (96,96))
            blocks.append(new_block)
            self.object_controllers.append(new_block)
        return blocks
    
    # Public methods:
    def set_window(self, window: pygame.Surface) -> None:
        self.window = window
    
    def logic_loop(self, objects) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
        self.trap.obj_tick()
        return True
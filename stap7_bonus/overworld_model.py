import pygame
from terrain_controller import TerrainController
from trap_controller import TrapController
from overworld_object_controller import OverworldObjectController
from player_controller import PlayerController

BLOCK_OFFSET = 160

class OverworldModel():
    width: int
    height: int
    window: pygame.Surface
    
    object_constrollers: list[OverworldObjectController] = []
    
    FPS:int = 60
    
    def __init__(self, window, width: int, height: int) -> None:
        self.width = width
        self.height = height
        
        terrain_master  = TerrainController(None, None, None, None, None, True)
        terrain_coords  = terrain_master.get_terrain_coords()
        self.terrain    = self._create_terrain(window, terrain_coords)
        
        self.trap       = TrapController(window, width // 2, height - BLOCK_OFFSET)
        
        self.object_constrollers.append(self.trap)
        
        self.player     = PlayerController(window, 100, 100)
    
    def set_window(self, window: pygame.Surface) -> None:
        self.window = window
    
    def logic_loop(self, keys, objects) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.player.obj_model.jump_count < 2:
                    self.player.obj_model.jump()
            
        self.trap.obj_tick()
        
        self.player.obj_tick(self.FPS, keys, objects)
        return True
    
    def _create_terrain(self, window, coords: list[list[int]]) -> list[TerrainController]:
        blocks =  []
        for coord in coords:
            x = coord[0]
            y = coord[1]
            new_block = TerrainController(window, x, y, (96,96))
            blocks.append(new_block)
            self.object_constrollers.append(new_block)
        return blocks
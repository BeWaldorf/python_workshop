import pygame
from overworld_object_controller import OverworldObjectController
from player_controller  import PlayerController
from terrain_controller import TerrainController



class OverworldModel():
    FPS = 60

    
    width: int
    height: int
    window: pygame.Surface
    
    clock = pygame.time.Clock()
    player: PlayerController = None
    
    def __init__(self, width: int, height: int) -> None:
        # self.window = window
        self.width = width
        self.height = height
        self.player     =  PlayerController(100, 100, (100, 100))
        self.objects: list[OverworldObjectController] = [] 
        terrain_master = TerrainController(None, None, None, "Master")
        terrain_coords = terrain_master.get_terrain_coords()
        self.terrain = self._create_terrain(terrain_coords, "Grass")
    
    # def set_window(self, window: pygame.Surface) -> None:
    #     self.window = window
    
    def logic_loop(self, window) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        self.player.obj_tick(self.FPS, window)
        return True
    
    def _create_terrain(self, coords: list[list[int]], terrain_type:str) -> list[OverworldObjectController]:
        blocks: list =  []
        for coord in coords:
            x = coord[0]
            y = coord[1]
            new_block = TerrainController(x, y, (96,96))
            new_block.obj_model.get_block_sprite(terrain_type)
            blocks.append(new_block)
        self.objects.extend(blocks)
        
        return blocks
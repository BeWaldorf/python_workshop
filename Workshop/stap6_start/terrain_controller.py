import pygame
from terrain_model import TerrainModel
from terrain_view import TerrainView
from overworld_object_controller import OverworldObjectController

class TerrainController(OverworldObjectController):
    def __init__(self, window: pygame.Surface, x: int, y: int, size: tuple[int, int], terrain_type: str = "Grass",is_master: bool = False):
        if is_master:
            self.obj_model = TerrainModel(None, None, True)
            self._is_master = True
            return            
        self.x = x
        self.y = y
        self.size = size
        
        super().__init__(window)
        self._make_mv()
        self.obj_view.draw_object(self.obj_model.get_block_sprite(terrain_type), (self.x, self.y))
        
    def _make_mv(self) -> None:
        self.obj_model: TerrainModel = TerrainModel(self.x, self.y)
        self.obj_view: TerrainView  = TerrainView(self.window, self.size)
        
    
    def get_terrain_coords(self) -> list[list[int]]:
        if self._is_master:
            return self.obj_model.get_terrain_coords()
        return None
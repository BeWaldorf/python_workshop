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
        
        super().__init__(window)
        self._make_mv(x, y, size)
        self.obj_view.draw_object(self.obj_model.get_block_sprite(terrain_type), self.obj_model.get_coords())
        
    def _make_mv(self, x, y, size) -> None:
        self.obj_model: TerrainModel = TerrainModel(x, y)
        self.obj_view: TerrainView  = TerrainView(self.window, size)
        
    
    def get_terrain_coords(self) -> list[list[int]]:
        if self._is_master:
            return self.obj_model.get_terrain_coords()
        return None
    
    def obj_tick(self):
        super().obj_tick()
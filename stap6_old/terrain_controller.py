import pygame
from terrain_model import TerrainModel
from terrain_view import TerrainView
from overworld_object_controller import OverworldObjectController

class TerrainController(OverworldObjectController):
    
    def __init__(self, x: int, y: int, size: tuple[int, int], terrain_type: str = "Grass"):
        if terrain_type == "Master":
            self.obj_model = TerrainModel(0,0,True)
            self._is_master = True
            return    
        self.x = x
        self.y = y
        self.size = size
        
        super().__init__()
        self._make_mv(terrain_type)
        # self.obj_view._create_block(terrain_type)
        
    def _make_mv(self, terrain_type: str) -> None:
        self.obj_model: TerrainModel = TerrainModel(self.x, self.y)
        self.obj_view: TerrainView  = TerrainView(self.size)
        self.obj_model.state = terrain_type
    
    # def _create_block(self, window: pygame.Surface,  terrain_type:str) -> None:
    #     temp = self.obj_model.get_block_sprite(terrain_type)
    #     self.obj_view.draw_object(window, temp, (self.x, self.y))
    #     
    
    def get_terrain_coords(self) -> list[list[int]]:
        if self._is_master:
            return self.obj_model.get_terrain_coords()
        return None
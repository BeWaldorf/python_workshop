import pygame
from overworld_object_view import OverworldObjectView

class TerrainView(OverworldObjectView):
    
    def __init__(self, window: pygame.Surface, size: tuple[int, int]) -> None:
        super().__init__(window, size)
        
    def draw_object(self, sprite: pygame.Surface, coords: tuple[int, int]) -> None:
        super().draw_object(sprite, coords)
import pygame
from overworld_object_view import OverworldObjectView

class TerrainView(OverworldObjectView):
    
    def __init__(self, size: tuple[int, int]) -> None:
        super().__init__(size)
        
    def draw_object(self, window, sprite: pygame.Surface, coords: tuple[int, int]) -> None:
        super().draw_object(window, sprite, coords)
    
    def draw_loop(self, window, sprite, rect) -> None:
        super().draw_loop(window, sprite, rect)
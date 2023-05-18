import pygame
from overworld_object_view import OverworldObjectView

class PlayerView(OverworldObjectView):
    
    def __init__(self, size: tuple[int, int]) -> None:
        super().__init__(size)
        
    
    def draw_loop(self, window, sprite, rect) -> None:
        super().draw_loop(window, sprite, rect)
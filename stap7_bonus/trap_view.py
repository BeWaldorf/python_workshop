import pygame
from overworld_object_view import OverworldObjectView

class TrapView(OverworldObjectView):
    
    def __init__(self, window, size: tuple[int, int]) -> None:
        super().__init__(window, size)
    
    def draw_loop(self, image: pygame.Surface, coords: tuple[int, int]) -> None:
        super().draw_loop(image, coords)
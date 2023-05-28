import pygame
from overworld_object_view import OverworldObjectView

class PlayerView(OverworldObjectView):
    
    def __init__(self,window: pygame.Surface,  size: tuple[int, int]) -> None:
        super().__init__(window, size)
        
    
    # def draw_loop(self, sprite, coords) -> None:
    #     super().draw_loop(sprite, coords)
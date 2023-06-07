import pygame

class OverworldObjectView():
    window: pygame.Surface
    rect: pygame.Rect
    
    def __init__(self, window: pygame.surface, size: tuple[int ,int]) -> None:
        self.window     = window
        width, height   = size
        self.rect = pygame.Rect(0, 0, width, height)
    
    def draw_object(self, sprite: pygame.Surface, coords: tuple[int, int]) -> None:
        self.window.blit(sprite, coords)
    
    def draw_loop(self, sprite: pygame.Surface, coords: tuple[int, int]) -> None:
        self.draw_object(sprite, coords)
    
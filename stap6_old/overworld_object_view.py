import pygame

class OverworldObjectView():
    window: pygame.Surface
    rect: pygame.Rect
    
    def __init__(self, size: tuple[int ,int]) -> None:
        width, height   = size
        self.width      = width
        self.height     = height
        self.rect = pygame.Rect(0, 0, width, height)
    
    def draw_object(self, window: pygame.surface, sprite: pygame.Surface, coords: tuple[int, int]) -> None:
        sprite = pygame.transform.scale2x(sprite)
        window.blit(sprite, coords, self.rect)
    
    def draw_loop(self, window: pygame.surface, sprite: pygame.Surface, rect: pygame.rect.Rect) -> None:
        sprite = pygame.transform.scale2x(sprite)
        self.rect = rect
        x, y = rect.topleft
        window.blit(sprite, (x, y), self.rect)
        
        
    
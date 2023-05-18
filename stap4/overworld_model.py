import pygame

class OverworldModel():
    width: int
    height: int
    window: pygame.Surface
    
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
    
    def set_window(self, window: pygame.Surface) -> None:
        self.window = window
    
    def logic_loop(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
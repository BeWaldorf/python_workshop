import pygame
from overworld_object_model import OverworldObjectModel

class TrapModel(OverworldObjectModel):
    # Constructor:
    def __init__(self, x: int, y: int, type: str):
        super().__init__(x, y, type)
        self.state:str = "on"
        self.image = self.select_sprite(self.state)
        
    # public methods:
    def logic_loop(self):
        super().logic_loop()
        self.image = self.select_sprite(self.state)
        
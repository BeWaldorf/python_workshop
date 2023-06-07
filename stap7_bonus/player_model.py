import pygame
from overworld_object_model import OverworldObjectModel

class PlayerModel(OverworldObjectModel):
    VELOCITY: int   = 5
    width: int      = 50
    height: int     = 50
    weight: int     = 1
    
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "Player")
        self._is_loopable: bool = True
        self.x_vel: float = 0
        self.y_vel: float = 0
        self.sprite_sheet_dict: dict = self._load_object_sprite_sheets()
        self.image = self.select_sprite("idle")
    
    def logic_loop(self, fps, keys, objects: list[pygame.sprite.Sprite]):
        super().logic_loop()
        self._player_movement_handler(keys, objects)
        
        self.y_vel += min(1, (self.fall_count / fps) * self.weight)
        self.move(self.x_vel, self.y_vel)
        if self.is_hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.is_hit = False
            self.hit_count = 0
        self.fall_count += 1
        self.image = self.select_sprite(self.get_state())
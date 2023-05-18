import pygame
from overworld_object_model import OverworldObjectModel

class PlayerModel(OverworldObjectModel):
    VELOCITY: int = 5
    
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "Player")
        self._is_loopable: bool = True
        self.x_vel: float = 0
        self.y_vel: float = 0
        self.sprite_sheet_dict: dict = self._load_object_sprite_sheets()
        self.image = self.select_sprite(self.get_player_state())
    
    def logic_loop(self, fps):
        super().logic_loop()
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)
        if self.is_hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.is_hit = False
            self.hit_count = 0
        self.fall_count += 1
        self.image = self.select_sprite(self.get_player_state())
        self.update_mask()
        
    
    def hit_head(self):
        self.y_vel *= -1
    
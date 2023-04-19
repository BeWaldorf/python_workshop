import pygame
from os.path import join
from overworld_object import OverworldObjectModel, OverworldObjectView, OverworldObjectController

class PlayerModel(OverworldObjectModel):
    COLOR = (255, 0, 0)
    WEIGHT = 1
    VELOCITY = 1
    
    def __init__(self, x, y, width, height, gravity):
        super().__init__(x, y, width, height)
        self.x_vel: int = 0
        self.y_vel: int = 0
        self.state: str = None
        self.gravity: int = gravity
        self.direction: str = "left"
        self.fall_count: int = 0
        self.jump_count: int = 0
        self.hit: bool = False
        self.hit_count: int = 0
    
    def jump(self):
        self.y_vel = 0# -self.WEIGHT * self.gravity * 8
        self.animation_counter = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += 0 # dy
    
    def make_hit(self):
        self.hit = True
    
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_counter = 0
    
    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_counter = 0
    
    def logic_loop(self, reset_animation_flag, fps):
        super().logic_loop(reset_animation_flag)
        self.y_vel += min(1, (self.fall_count / fps) * self.WEIGHT)
        self.move(self.x_vel, self.y_vel)
        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0
        self.fall_count += 1
    
    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0
    
    def hit_head(self):
        self.count = 0
        self.y_vel *= -1
    
    def update_player_state(self) -> tuple:
        player_action = "idle"
        if self.hit:
            player_action = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                player_action = "jump"
            elif self.jump_count == 2:
                player_action = "double_jump"
        elif self.y_vel > self.WEIGHT * 2:
            player_action = "fall"
        elif self.x_vel != 0:
            player_action = "run"
        self.state = player_action
        player_status = (self.state, self.animation_counter, self.direction)
        return player_status
    
    def has_been_animated(self):
        self.animation_counter += 1
        
class PlayerView(OverworldObjectView):
    SPRITE_WIDTH = SPRITE_HEIGHT = 32
    def __init__(self, asset_path, size_wh, disp_surfaces):
        super().__init__(asset_path, size_wh, disp_surfaces, True, "PinkMan")

class PlayerController(OverworldObjectController):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        
    def _generate_mv(self):
        self.obj_model = PlayerModel(self.x_coord, self.y_coord, self.obj_width, self.obj_height, 1)
        player_wh = (self.obj_model.width, self.obj_model.height)
        disp_surf = (self.obj_model.image, self.obj_model.rect)
        path = "assets\MainCharacters"
        self.obj_view = PlayerView(path, player_wh, disp_surf)
    
    def obj_loop(self, fps, window) -> tuple:
        reset_animation_flag = self.obj_view.reset_animation_flag
        self.obj_model.logic_loop(reset_animation_flag, fps)
        state, ani_count, direction = self.obj_model.update_player_state()
        temp_sprite = self.obj_view.update_sprite(state, ani_count, direction)
        self.obj_model.has_been_animated()
        self.obj_view.draw_loop(window, self.obj_model.image, self.obj_model.current_x, self.obj_model.current_y, 0)

from overworld_object_controller import OverworldObjectController as Parent
from Models.player_model import PlayerModel
from Views.player_view import PlayerView

class PlayerController(Parent):
    name = "PinkGuy"
    
    def __init__(self, x, y, rectangle, player):
        super().__init__(x, y, rectangle, player)
        self.generate_mv()
        
    
    def generate_mv(self):
        self.obj_model = PlayerModel(self.x_coord, self.y_coord, self.my_rect, 1)
        self.obj_view = PlayerView(self.obj_model.SOURCEFOLDER_PATH, self.obj_model.get_size_wh(), self.obj_model)
    
    def jump(self):
        self.y_vel = -self.WEIGHT * self.gravity * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def make_hit(self):
        self.hit = True
    
    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
    
    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
    
    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.WEIGHT)
        self.move(self.x_vel, self.y_vel)
        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0
        self.fall_count += 1
        self.update_sprite()
    
    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0
    
    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

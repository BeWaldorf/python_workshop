from Models.overworld_object_model import OverworldObjectModel

class PlayerModel(OverworldObjectModel):
    COLOR = (255, 0, 0)
    WEIGHT = 1
    NAME = "player"
    SOURCEFOLDER_PATH, = "assets/MainCharacters/PinkMan"
    ANIMATION_DELAY = 3
    
    
    def __init__(self, x, y, rectangle, gravity):
        super().__init__(x, y, rectangle)
        self.x_vel = 0
        self.y_vel = 0
        self.gravity = gravity
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
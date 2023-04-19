import pygame
from overworld_object import OverworldObjectModel, OverworldObjectView, OverworldObjectController

F_WIDTH, F_HEIGHT = 16, 32

class FireModel(OverworldObjectModel):
    WIDTH, HEIGHT = F_WIDTH, F_HEIGHT
    def __init__(self, x, y):
        super().__init__(x, y, self.WIDTH, self.WIDTH)
        self.state = "off"

    def on(self):
        self.state = "on"

    def off(self):
        self.state = "off"

    def logic_loop(self, reset_animation_flag):
        super().logic_loop(reset_animation_flag)
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

class FireView(OverworldObjectView):
    SPRITE_WIDTH = F_WIDTH
    SPRITE_HEIGHT = F_HEIGHT
    def __init__(self, asset_path, size_wh, disp_surfaces_ir):
        super().__init__(asset_path, size_wh, disp_surfaces_ir, False, "Fire")
    
    
    
class FireController(OverworldObjectController):
    WIDTH, HEIGHT = F_WIDTH, F_HEIGHT
    def __init__(self, x, y):
        super().__init__(x, y, self.WIDTH, self.HEIGHT)
        
    def _generate_mv(self) -> None:
        self.obj_model = FireModel(self.x_coord, self.y_coord)
        disp_surf = (self.obj_model.image, self.obj_model.rect)
        size = (self.obj_model.width, self.obj_model.height)
        self.obj_view = FireView("assets\Traps", size, disp_surf)
    
    def on(self):
        self.obj_model.on()
    
    def off(self):
        self.obj_model.off()
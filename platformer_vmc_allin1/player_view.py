from Views.overworld_object_view import OverworldObjectView

class PlayerView(OverworldObjectView):
    def __init__(self, asset_path, size_wh, model) -> None:
        super().__init__(asset_path, size_wh)
        self.model = model
    
    def update_sprite(self):
        sprite_sheet = "idle"
        if self.model.hit:
            sprite_sheet = "hit"
        elif self.model.self.y_vel < 0:
            if self.model.jump_count == 1:
                sprite_sheet = "jump"
            elif self.model.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.model.y_vel > self.WEIGHT * 2:
            sprite_sheet = "fall"
        elif self.model.x_vel != 0:
            sprite_sheet = "run"
        sprite_sheet_name = sprite_sheet + "_" + self.model.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.model.animation_count += 1
        self.update()
import pygame
from os import listdir
from os.path import join, isfile
# from player_model import PlayerModel

class OverworldObjectModel(pygame.sprite.Sprite):
    COLOR: tuple[int, int, int] = (255, 0, 0)
    GRAVITY = 1
    ANIMATION_DELAY: int= 3
    
    WORLD_SIZE: tuple[int, int] = (1000,800)
    
    BLOCK_SIZE: int = 96

    SOURCEFOLDER_PATH:dict[str, str] = {
        "Player": "assets\\MainCharacters\\NinjaFrog",
        "Trap": "assets\\Traps\\Fire",
        "Terrain": "assets\\Terrain",
    }

    SPRITE_WH: dict[str, tuple[int, int]] = {
        "Player": (32, 32),
        "Trap": (16, 32),
        "Terrain": (96, 96),
    }
    
    SPRITE_HAS_DIRECTION: dict[str, bool] = {
        "Player": True,
        "Trap": False,
        "Terrain": False,
    }
    
    SURFACE_WH: dict[str, tuple[int, int]] = {
        "Player": (50, 50),
        "Trap": (16, 32),
        "Terrain": (96, 96),
    }
    
    _is_loopable: bool = True
    direction: str = "left"
    
    has_collided: bool = False
    has_collided_left: bool = False
    has_collided_right:bool = False
    fall_count = 0
    hit_count: int = 0
    animation_counter: int = 0
    reset_animation_flag: bool = False
    
    def __init__(self, x: int, y: int, type: str):
        super().__init__()
        
        self.type = type
        
        width, height = self.SURFACE_WH[type]
        self.current_x: int = x
        self.current_y: int = y
        
        self.rect: pygame.rect.Rect = pygame.rect.Rect(x, y, width, height)
        self.image:pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.mask: pygame.Mask = None
        
        self.state: str = None
        self.sprite_sheet_dict: dict = self._load_object_sprite_sheets()
        self.is_hit: bool = False
        
    
    def set_coords(self, x: int = None, y: int = None) -> None:
        if x != None:
            self.current_x = x
        if y != None:
            self.current_y = y
   
    def get_coords(self) -> tuple[int, int]:
        return (self.current_x, self.current_y)
    
    def get_size_wh(self) -> tuple:
        size = (self.width, self.height)
        return size
    
    def get_state(self) -> str:
        return self.state
    
    def set_state(self, obj_state) -> None:
        self.state = obj_state
    
    def is_loopable(self) -> bool:
        return self._is_loopable
    
    def logic_loop(self):
        if self.reset_animation_flag == True:
            self.animation_counter = 0
            self.reset_animation_flag = False
        
    def get_surface_rect_tuple(self) -> tuple[pygame.Surface, pygame.Rect]:
        return (self.image, self.rect)
        
    def get_rect(self) -> pygame.Rect:
        return self.rect
    
    def get_player_state(self) -> str:
        if self.type != "Player":
            return "object is geen player object"
        state = "idle"
        if self.is_hit:
            state = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                state = "jump"
            elif self.jump_count == 2:
                state = "double_jump"
        elif self.y_vel > self.GRAVITY * 2:
            state = "fall"
        elif self.x_vel != 0:
            state = "run"
        state_name = state + "_" + self.direction
        self.state = state_name
        return state_name
    
    def select_sprite(self, sprite_state: str) ->pygame.Surface:
        if self.type == "Terrain":
            return self.sprite_sheet_dict[sprite_state]
            
        path = self.SOURCEFOLDER_PATH[self.type]
        sprite_dict_key = join(path, sprite_state)
        sprite_sheet = list(self.sprite_sheet_dict[sprite_dict_key])
        animation_length = len(sprite_sheet)
        if self.animation_counter > animation_length:
            self.animation_counter = 0
        sprite_index = ((self.animation_counter // self.ANIMATION_DELAY) % animation_length)
        self.animation_counter += 1

        return sprite_sheet[sprite_index]
    
    def _load_object_sprite_sheets(self):
        if self.type == "Terrain":
            return self._make_block_dict()
        sprite_width, sprite_height = self.SPRITE_WH[self.type]
        my_dir = self.SOURCEFOLDER_PATH[self.type]
        image_sources = [join(my_dir, file) for file in listdir(my_dir) if isfile(join(my_dir, file))]
        all_sprites = {}
        for image_source in image_sources:
            sprite_sheet = pygame.image.load(image_source).convert_alpha()
            images = []
            for sprite_coord in range((sprite_sheet.get_width() // sprite_width)):
                surface = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(sprite_coord * sprite_width, 0, sprite_width, sprite_height)
                surface.blit(sprite_sheet, (0, 0), rect)
                # images.append(surface)
                images.append(pygame.transform.scale2x(surface))
            if self.SPRITE_HAS_DIRECTION[self.type]:
                all_sprites[image_source.replace(".png", "") + "_right"] = images
                all_sprites[image_source.replace(".png", "") + "_left"] = self._flip(images)
            else:
                all_sprites[image_source.replace(".png", "")] = images
        return all_sprites
    
    def _flip(self, sprites: list):
        return [pygame.transform.flip(sprite, True, False) for sprite in sprites]
    
       
    def _make_block_dict(self):
        block_sprite_coords = [
            (0, 0),     (0, 64),    (0, 128), 
            (96, 0),    (96, 64),   (96, 128), 
                        (272, 64), 
        ]
        block_names = [
            "Cobble",   "Wood", "Scales",
            "Grass",    "Fall", "PinkGoo",
                        "Bricks",
        ]
        sprite_sheet = pygame.image.load(join(self.SOURCEFOLDER_PATH["Terrain"], "Terrain.png")).convert_alpha()
        block_dict = {}
        for sprite_index in range(7):
            x, y = block_sprite_coords[sprite_index]
            sprite_surface: pygame.Surface = pygame.Surface(self.SURFACE_WH["Terrain"], pygame.SRCALPHA, 32)
            rect: pygame.Rect = pygame.Rect(x, y, 96, 96)
            sprite_surface.blit(sprite_sheet, (0, 0), rect)
            # sprite_surface = pygame.transform.scale2x(sprite_surface)
            block_dict[block_names[sprite_index]] = sprite_surface
        return block_dict
    
    def vertical_collider(self, player, dy: float,) -> None:
        if player.type != "Player":
            return "player parameter is geen player object"
        if self.detect_collision(player):
            if dy > 0:
                player.rect.bottom = self.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = self.rect.bottom
                player.hit_head()
        
    
    def horizontal_collider(self, player, dx: float) ->None:
        if player.type != "Player":
            return "player parameter is geen player object"
        player.move(dx,0)
        player.update_mask()
        player.has_collided_right = False
        player.has_collided_left = False
        if self.detect_collision(player):
            if dx > 0:
                player.has_collided_right = True 
            if dx < 0:  
                player.has_collided_left = True 
        player.move(-dx,0)
        player.update_mask()
    
    def update_mask(self):
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
    
    def detect_collision(self, player) ->bool:
        if player.type != "Player":
            return "player parameter is geen player object"
        player.update_mask()
        return pygame.sprite.collide_mask(self, player)

    
    def move(self, dx:float, dy:float):
        if self.type != "Player":
            return "object is geen player object"
        self.rect.x += dx
        self.rect.y += dy
    
    def make_is_hit(self):
        self.is_hit = True
    
    def move_left(self, velocity: int):
        if self.type != "Player":
            return "object is geen player object"
        self.x_vel = -velocity
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0
    def move_right(self, velocity: int):
        if self.type != "Player":
            return "object is geen player object"
        self.x_vel = velocity
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0
    
    def input_handler(self, keys, velocity) -> None:
        if self.type != "Player":
            return "object is geen player object"
        if keys[pygame.K_LEFT] and not self.has_collided_left:
            self.move_left(velocity)
        if keys[pygame.K_RIGHT] and not self.has_collided_right:
            self.move_right(velocity)
    
    def landed(self):
        if self.type != "Player":
            return "object is geen player object"
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0
        
    def jump(self):
        if self.type != "Player":
            return "object is geen player object"
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
    
import pygame
from os import listdir
from os.path import join, isfile

class OverworldObjectModel(pygame.sprite.Sprite):
    ANIMATION_DELAY: int= 3
    
    WORLD_HEIGHT: int = 720
    WORLD_WIDTH: int = 1280
    WORLD_SIZE: tuple[int, int] = (WORLD_WIDTH, WORLD_HEIGHT)
    
    BLOCK_SIZE: int = 96

    SOURCEFOLDER_PATH:dict[str, str] = {
        "Player": "assets/MainCharacters/PinkMan",
        "Trap": join("assets", "Traps", "Fire"), # "assets/Traps/Fire",
        "Terrain": join("assets", "Terrain"), # "assets/Terrain"
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
    
    def __init__(self, x: int, y: int, type: str):
        super().__init__()
        
        self.type = type
        
        width, height = self.SURFACE_WH[type]
        self.current_x: int = x
        self.current_y: int = y
        
        self.rect: pygame.Rect = pygame.Rect(x, y, width, height)
        self.image:pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.mask: pygame.Mask = None
        
        self.state: str = None
        self.sprite_sheet_dict: dict = self._load_object_sprite_sheets()
        self.animation_counter: int = 0
        self.reset_animation_flag: bool = False
    
    def set_coords(self, x: int = None, y: int = None) -> None:
        if x != None:
            self.current_x = x
        if y != None:
            self.current_y = y
            
    def get_image(self) -> pygame.Surface:
        return self.image
    
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
    
    def select_sprite(self, sprite_name: str, direction: str = "left") ->pygame.Surface:
        if self.type == "Terrain":
            return self.sprite_sheet_dict[sprite_name]
            
        path = self.SOURCEFOLDER_PATH[self.type]
        sprite_dict_key = join(path, sprite_name)
        if self.SPRITE_HAS_DIRECTION[self.type] != False:
            sprite_dict_key += "_"+ direction
        sprite_sheet = list(self.sprite_sheet_dict[sprite_dict_key])

        animation_length = len(sprite_sheet)
        sprite_index = ((self.animation_counter // self.ANIMATION_DELAY) % animation_length)
        self.animation_counter += 1
        if sprite_index > animation_length:
            self.reset_animation_flag = True
            self._reset_animation()
        return sprite_sheet[sprite_index]
    
    def _reset_animation(self):
        self.animation_counter = 0
        self.reset_animation_flag = False
    
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
            result = pygame.Surface((96,96), pygame.SRCALPHA, 32)
            sprite_surface.blit(sprite_sheet, (0, 0), rect)
            sprite_surface = pygame.transform.scale2x(sprite_surface)
            result.blit(sprite_surface, (0, 0), pygame.rect.Rect(0, 0, 96, 96))
            block_dict[block_names[sprite_index]] = result
        return block_dict
    
    def _get_Terrain_coords(self) -> list[list[int]]:
        _, world_height = self.WORLD_SIZE
        coords = []
        coords.extend(self._get_floor_coords())
        coords.append([0, world_height - (self.BLOCK_SIZE * 2)])
        for block in range(4):
            coords.append([(self.BLOCK_SIZE * block) + self.BLOCK_SIZE * 2, world_height - (self.BLOCK_SIZE * 4)])    
        coords.append([0, world_height - (self.BLOCK_SIZE * 6)])
        for block in range(5):
            coords.append([(self.BLOCK_SIZE * block) + self.BLOCK_SIZE * 7, world_height - (self.BLOCK_SIZE * 6)])
        return coords
        return coords
    
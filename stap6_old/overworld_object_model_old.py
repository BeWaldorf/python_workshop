import pygame
from os import listdir
from os.path import join, isfile

class OverworldObjectModel(pygame.sprite.Sprite):
    ANIMATION_DELAY: int= 3

    SOURCEFOLDER_PATH:dict[str] = {
        "Player": "assets\MainCharacters\NinjaFrog",
        "Trap": "assets\Traps",
        "Terrain": "assets\Terrain",
    }

    SPRITE_WH: dict[tuple(int, int)] = {
        "Player": (32, 32),
        "Trap": (16, 32),
        "Terrain": (96, 96),
    }
    
    SPRITE_HAS_DIRECTION: dict[bool] = {
        "Player": True,
        "Trap": False,
        "Terrain": False,
    }
    
    SURFACE_WH: dict[tuple] = {
        "Player": (50, 50),
        "Trap": (16, 32),
        "Terrain": (96, 96),
    }
    
    def __init__(self, x: int, y: int, type: str):
        super().__init__()
        
        self.type = type
        
        width, height = self.SURFACE_WH[type]
        self.current_x: int = x
        self.current_y: int = y
        
        self.rect: pygame.Rect = pygame.Rect(x, y, width, height)
        self.image:pygame.Surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.mask: pygame.Mask = None
        
        self.sprite_sheet_dict: dict = []
        self.animation_counter: int = 0
        self.state: str = None
    
    def set_coords(self,x: int = None, y: int = None) -> None:
        if x != None:
            self.current_x = x
        if y != None:
            self.current_y = y
    
    def get_size_wh(self) -> tuple:
        size = (self.width, self.height)
        return size
    
    def update_image(self, img: pygame.surface):
        self.image = img
        if img != None:
            self.mask = pygame.mask.from_surface(img)
            self.rect = img.get_rect(topleft=(self.rect.x, self.rect.y))
    
    def logic_loop(self, reset_animation_flag):
        if reset_animation_flag == True:
            self.animation_counter = 0
    
    def _load_object_sprite_sheets(self, sprite_width, sprite_height):
        #   image_sources = []
        #   for file in listdir(self.asset_folder):
        #       if isfile(join(self.asset_folder, file)):
        #           image_sources.append(join(self.asset_folder, file))
        # image_sources = [file for file in listdir(self.asset_folder) if isfile(join(self.asset_folder, file))]
        # Eventueel list comprehension?
        all_sprites = {}
        for image_source in image_sources:
            image_source = str(image_source)
            sprite_sheet = pygame.image.load(image_source).convert_alpha()
            images = []
            for sprite in range((sprite_sheet.get_width() // sprite_width)):
                surface = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(sprite * sprite_width, 0, sprite_width, sprite_height)
                surface.blit(sprite_sheet, (0, 0), rect)
                images.append(pygame.transform.scale2x(surface))
            if self.has_direction:
                all_sprites[image_source.replace(".png", "") + "_right"] = images
                all_sprites[image_source.replace(".png", "") + "_left"] = self._flip(images)
            else:
                all_sprites[image_source.replace(".png", "")] = images
        return all_sprites
    
def _flip(self, sprites: list):
    #flipped_sprites = []
    #for sprite in sprites:
    #    flipped_sprites.append(pygame.transform.flip(sprite, True, False))
    #return flipped_sprites
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]    
        

class OverworldObjectView():
    
    
    def __init__(self, asset_folder: str, size_wh: tuple, disp_surfaces_ir:tuple, has_direction:bool = False, name:str = None) -> None:
        self.asset_folder = asset_folder
        self.image, self.rect = disp_surfaces_ir
        self.has_direction = has_direction
        if name != None:
            self.asset_folder = join(self.asset_folder, name)
        self.width, self.height = size_wh
        self.sprite_sheet_dict = self._load_object_sprite_sheets(self.SPRITE_WIDTH, self.SPRITE_HEIGHT)
        self.reset_animation_flag = False
    
    
    def draw_overworld_object(self, window: pygame.surface.Surface, object_to_draw:  OverworldObjectModel, offset_x: int):
        coords = (object_to_draw.rect.x - offset_x, object_to_draw.rect.y)
        window.blit(object_to_draw.image, coords)
    
        
    def update_sprite(self, obj_state: str, ani_count: int = None, direction = False) -> pygame.Surface:
        sprite_key = join(self.asset_folder,obj_state) 
        if self.has_direction != False:
            sprite_key += "_" + direction
        sprite_sheet = self.sprite_sheet_dict[sprite_key]
        animation_length = len(sprite_sheet)
        if animation_length == 0:
            print(sprite_key)
            print(self.sprite_sheet_dict[sprite_key])
        sprite_index = ((ani_count // self.ANIMATION_DELAY) % animation_length)
        if ani_count > animation_length:
            self.reset_animation_flag = True
        self.image = sprite_sheet[sprite_index]
        return self.image
    
    def draw_loop(self, window: pygame.Surface, image:pygame.Surface, x, y, offset_x: int):
        x -= offset_x
        coords = (x, y)
        window.blit(image, coords)
    

class OverworldObjectController():
    name = obj_model = obj_view = rect = None
    
    def __init__(self, x: int, y: int, width: int, height: int):
        self.obj_width = width
        self.obj_height = height
        self.x_coord = x
        self.y_coord = y
        self._generate_mv()
        
        
    def _generate_mv(self):
        self.obj_model = OverworldObjectModel(self.x_coord,self.y_coord, self.obj_width, self.obj_height)
        self.rect = self.obj_model.rect
        disp_surf = (self.obj_model.image, self.rect)
        asset_folder = self.obj_model.SOURCEFOLDER_PATH
        size =  self.obj_model.get_size_wh()
        self.obj_view = OverworldObjectView(asset_folder, size, disp_surf)
        self.obj_model.sprite_sheet_dict = self.obj_view.sprite_sheet_dict
    
    def draw_object(self, window, offset_x):
        self.obj_view.draw_overworld_object(window, self.obj_model, offset_x)
        
    def obj_loop(self, window):
        flag = self.obj_view.reset_animation_flag
        self.obj_model.logic_loop(flag)
        img = self.obj_model.image
        x = self.obj_model.current_x
        y = self.obj_model.current_y
        self.obj_view.draw_loop(window, img, x, y, 0)
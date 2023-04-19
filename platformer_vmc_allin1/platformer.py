import os
import pygame
from os import listdir
from os.path import isfile, join


"""                                                                      """
"""                  OVERWORLD OBJECT                                    """
"""                                                                      """
class OverworldObjectModel(pygame.sprite.Sprite):
    NAME = SOURCEFOLDER_PATH = None
    width = height = current_x = current_y = rect = mask = image = sprites = None
    def __init__(self, x, y, rectangle):
        super().__init__()
        self.rect = rectangle
        self.current_x = x
        self.current_y = y
        self.mask = None
    
    def get_coords(self) -> tuple:
        coords = (self.current_x, self.current_y)
        return coords
    
    def set_coords(self,x = None, y = None) -> None:
        if x != None:
            self.current_x = x
        if y != None:
            self.current_y = y
    
    def get_size_wh(self) -> tuple:
        size = (self.width, self.height)
        return size
    
    def get_rectangle(self):
        return self.rect
    
    def update_sprite(self, img: pygame.surface):
        self.image = img
        if img != None:
            self.mask = pygame.mask.from_surface(img)
            self.rect = img.get_rect(topleft=(self.rect.x, self.rect.y))

class OverworldObjectView():
    def __init__(self, asset_path, size_wh, direction = None) -> None:
        self.asset_folder = asset_path
        # self.source_path = join(self.asset_folder, self.source_name)
        self.width, self.height = size_wh
        self.sprites = self.load_object_sprite_sheets(direction)
        self.current_sprite = None
    
    def load_object_sprite_sheets(self, direction = False):
        sprite_sources = []
        for file in listdir(self.asset_folder):
            if isfile(join(self.asset_folder, file)):
                sprite_sources.append(join(self.asset_folder, file))
        # images = [file for file in listdir(self.source_path) if isfile(join(self.source_path, file))]
        # Eventueel list comprehension?
        all_sprites = {}
        for sprite_source in sprite_sources:
            sprite_source = str(sprite_source)
            sprite_sheet = pygame.image.load(sprite_source).convert_alpha()
            sprites = []
            for i in range(sprite_sheet.get_width() // self.width):
                surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * self.width, 0, self.width, self.height)
                surface.blit(sprite_sheet, (0, 0), rect)
                sprites.append(pygame.transform.scale2x(surface))
            if direction:
                all_sprites[sprite_source.replace(".png", "") + "_right"] = sprites
                all_sprites[sprite_source.replace(".png", "") + "_left"] = self.flip(sprites)
            else:
                all_sprites[sprite_source.replace(".png", "")] = sprites
        return all_sprites
    
    def flip(self, sprites: list):
        flipped_sprites = []
        for sprite in sprites:
            flipped_sprites.append(pygame.transform.flip(sprite, True, False))
        # [pygame.transform.flip(sprite, True, False) for sprite in sprites]
        return flipped_sprites
    
    def draw_overworld_object(self, window, object_to_draw, offset_x):
        window.blit(object_to_draw.image, (object_to_draw.rect.x - offset_x, object_to_draw.rect.y))
    
    def get_sprites(self):
        return self.sprites

class OverworldObjectController():
    x_coord = y_coord = name = obj_width = obj_height = obj_model = obj_view = rect = None
    
    def __init__(self, x, y, rectangle = None):
        self.rect = rectangle
        self.x_coord = x
        self.y_coord = y
        
        self.generate_mv()
        if self.obj_view.current_sprite != None:
            self.obj_model.update_sprite(self.obj_view.current_sprite)
        self.obj_model.sprites = self.obj_view.sprites
        
    def generate_mv(self):
        self.obj_model = OverworldObjectModel(self.x_coord, self.y_coord, self.my_rect)
        self.obj_view = OverworldObjectView (self.my_rect, self.obj_model.SOURCEFOLDER_PATH, self.obj_model.source_name, self.obj_model.get_size_wh())
    
    def show_object(self, window, offset_x):
        self.obj_view.draw_overworld_object(window, self.obj_model, offset_x)


"""                                                                                              """
"""                         world objects                                                        """
"""                                                                                              """
class TerrainModel(OverworldObjectModel):
    def __init__(self, x, y, size):
        self.current_x = x
        self.current_y = y
        self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(96, 0, size, size)
        
    def get_surface(self):
        return self.surface
    
class TerrainView(OverworldObjectView):
    def __init__(self, asset_path, size, surface, rect):
        super().__init__(asset_path, (size, size))
        self.size = size
        self.surface = surface
        self.rect = rect
        source_path = join(asset_path, "Terrain.png")
        print(source_path)
        self.current_sprite = pygame.image.load(source_path).convert_alpha
        """ self.image = self.current_sprite = pygame.image.load(asset_path).convert_alpha() """
        """ self.surface.blit(self.image, (0, 0), self.rect) """
        """  """
    def startup():
        pass
    
    def build_terrain_unit(self, surface,rectangle):
        print(self.current_sprite)
        surface.blit(self.current_sprite, (0,0), rectangle)
        return pygame.transform.scale2x(surface)
    
    def draw_unit(self, unit):
        self.current_sprite.blit(unit, (0,0))
        
class TerrainController(OverworldObjectController):
    def __init__(self, x, y):
        super().__init__(x,y)
        sprites = self.obj_view.load_object_sprite_sheets()
        self.obj_model.update_sprite
        self.unit = self.obj_view.build_terrain_unit(self.obj_model.get_surface(), self.obj_model.rect)
        self.obj_view.draw_unit(self.unit)
    
    def generate_mv(self):
        self.obj_model = TerrainModel(self.x_coord, self.y_coord, 96)
        self.obj_view = TerrainView("assets\Terrain", 96, self.obj_model.surface, self.obj_model.rect)
        
class FireModel(OverworldObjectModel):
    ANIMATION_DELAY = 3
    fire = None
    def __init__(self, x, y, rectangle):
        super().__init__(x, y, rectangle)
        self.animation_count = 0
        self.animation_name = "off"

    def on(self):
        self.animation_name = "on"

    def off(self):
        self.animation_name = "off"

    def loop(self):
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.update_sprite(self.image)

        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0

class FireView(OverworldObjectView):
    state = "off"
    def __init__(self, asset_path, size_wh) -> None:
        super().__init__(asset_path, size_wh)
        
    def get_animation(self, state, anim_count):
        self.current_sprite = self.sprites[state][anim_count]
        return self.current_sprite
    
    
class FireController(OverworldObjectController):
    WIDTH, HEIGHT = 16, 32
    def __init__(self, x, y):
        rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)
        super().__init__(x, y, rect)
        self.obj_model.update_sprite(self.obj_view.current_sprite)
    
    def generate_mv(self) -> None:
        self.obj_model = FireModel(self.x_coord, self.y_coord, pygame.Rect(self.x_coord, self.y_coord, self.WIDTH, self.HEIGHT))
        self.obj_view = FireView("assets\Traps\Fire", (self.WIDTH, self.HEIGHT))




"""                                                                                          """
"""                     PLAYER                                                               """
"""                                                                                          """
class PlayerModel(OverworldObjectModel):
    COLOR = (255, 0, 0)
    WEIGHT = 1
    NAME = "player"
    SOURCEFOLDER_PATH = "assets\MainCharacters\PinkMan"
    VELOCITY = 1
    
    def __init__(self, x, y, width, height, gravity):
        rectangle = pygame.Rect(x, y, width, height)
        super().__init__(x, y, rectangle)
        self.width: int = width
        self.height: int = height
        self.x_vel: int = 0
        self.y_vel: int = 0
        self.state: str = None
        self.gravity: int = gravity
        self.direction: str = "left"
        self.animation_count: int = 0
        self.fall_count: int = 0
        self.jump_count: int = 0
        self.hit: bool = False
        self.hit_count: int = 0
    
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
    
    def loop(self, fps, sprite) -> str:
        self.y_vel += min(1, (self.fall_count / fps) * self.WEIGHT)
        self.move(self.x_vel, self.y_vel)
        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0
        self.fall_count += 1
        self.update_sprite(sprite)
        return self.update_player_state()
    
    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0
    
    def hit_head(self):
        self.count = 0
        self.y_vel *= -1
    
    def update_player_state(self) -> str:
        player_state = "idle"
        if self.hit:
            player_state = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                player_state = "jump"
            elif self.jump_count == 2:
                player_state = "double_jump"
        elif self.y_vel > self.WEIGHT * 2:
            player_state = "fall"
        elif self.x_vel != 0:
            player_state = "run"
        self.state = player_state
        return player_state
    
    def has_been_animated(self):
        self.animation_count += 1
        
class PlayerView(OverworldObjectView):
    ANIMATION_DELAY = 3
    def __init__(self, asset_path, size_wh, model) -> None:
        super().__init__(asset_path, size_wh, True)
        self.model = model
    
    def update_sprite(self, sheet_to_use: str, ani_count):
        sprite_sheet_name = self.asset_folder + "\\" + sheet_to_use + "_" + self.model.direction
        sprites = self.sprites[sprite_sheet_name]
        print(len(sprites))
        print(sprite_sheet_name)
        sprite_index = (ani_count // self.ANIMATION_DELAY) % len(sprites)
        self.current_sprite = sprites[sprite_index]
        return self.current_sprite

class PlayerController(OverworldObjectController):
    name = "PinkGuy"
    width = height = None
    def __init__(self, x, y, width, height):
        self.height = height
        self.width = width
        super().__init__(x, y)
        self.my_rect = self.obj_model.rect
        
    def generate_mv(self):
        self.obj_model = PlayerModel(self.x_coord, self.y_coord, self.width, self.height, 1)
        player_wh = self.obj_model.get_size_wh()
        player_asset_path = self.obj_model.SOURCEFOLDER_PATH
        self.obj_view = PlayerView(player_asset_path, player_wh, self.obj_model)
    
    def player_loop(self, fps):
        temp_state: str = self.obj_model.update_player_state()
        temp_sprite = self.obj_view.update_sprite(temp_state, self.obj_model.animation_count)
        self.obj_model.loop(fps, temp_sprite)
        self.obj_model.has_been_animated()


"""                                                                                          """
"""                     game                                                                 """
"""                                                                                          """
class OverworldModel():
    WIDTH, HEIGHT = 1000, 800
    FPS = 60
    GRAVITY = 1
    PLAYER_SPEED = 5
    BLOCK_SIZE = 96
    TITLE = "Platformer"
    player: PlayerController = None
    trap = player = objects = player_velocity = trap = None

    
    def __init__(self) -> None:
        self.scroll_area_width = 200
        self.offset_x = 0
        self.clock = self.clock = pygame.time.Clock()
    
    def handle_vertical_collision(self, player, dy):
        collided_objects = []
        for object in self.objects:
            if pygame.sprite.collide_mask(player, object.obj_model):
                if dy > 0:
                    player.rect.bottom = object.obj_model.rect.top
                    player.landed()
                elif dy < 0:
                    player.rect.top = object.obj_model.rect.bottom
                    player.hit_head()
                collided_objects.append(object)
        return collided_objects

    def collide(self, player: PlayerModel, dx):
        player.move(dx, 0)
        player.update()
        collided_object = None
        test = 0
        for object in self.objects:
            test += 4
            if pygame.sprite.collide_mask(player, object.obj_model):
                collided_object = object
                break
        player.move(-dx, 0)
        player.update()
        return collided_object
    
    def handle_move(self, player: PlayerModel):
        keys = pygame.key.get_pressed()

        player.x_vel = 0
        collide_left = self.collide(player, -self.player_velocity * 2)
        collide_right = self.collide(player, self.player_velocity * 2)

        if keys[pygame.K_LEFT] and not collide_left:
            player.move_left(self.player_velocity)
        if keys[pygame.K_RIGHT] and not collide_right:
            player.move_right(self.player_velocity)

        vertical_collide = self.handle_vertical_collision(player, player.y_vel)
        to_check = [collide_left, collide_right, *vertical_collide]

        for obj in to_check:
            if obj and obj.name == "fire":
                player.make_hit()
        
    def generate_background(self, name) -> tuple:
        background_image = pygame.image.load(join("assets", "Background", name))
        _, _, width, height = background_image.get_rect()
        tiles = []
        for column in range(self.WIDTH // width + 1):
            for row in range(self.HEIGHT // height + 1):
                position = (column * width, row * height)
                tiles.append(position)
        return (tiles, background_image)
        
    def generate_floor(self) -> list:
        floor = []
        for new_tile in range(-self.WIDTH // self.BLOCK_SIZE, (self.WIDTH * 2) // self.BLOCK_SIZE):
            floor.append(TerrainController(new_tile * self.BLOCK_SIZE, self.HEIGHT - self.BLOCK_SIZE))
        return floor
    
    def generate_objects(self, fire) -> list:
        self.objects = [
                    TerrainController(0, self.HEIGHT - self.BLOCK_SIZE * 2),
                    TerrainController(self.BLOCK_SIZE * 3, self.HEIGHT - self.BLOCK_SIZE * 4),
                    #fire,
                    ]
        for tile in self.generate_floor():
            self.objects.append(tile)
    
    def generate_player(self, x, y, width, heigth):
        self.player = PlayerController(x, y, width, heigth)
        self.player_velocity = self.player.obj_model.VELOCITY * self.PLAYER_SPEED
    
    def generate_trap(self, x):
        y = self.HEIGHT - self.BLOCK_SIZE - 64
        self.trap = FireController(x, y)
    
    
class Level1View():
    def __init__(self, caption, size_wh):
        pygame.display.set_caption(caption)
        self.screen_width, self.screen_height = size_wh 
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))       
    
    def draw_level(self, generated_bg, player, objects, offset_x):
        background_tiles, bg_image = generated_bg
        for tile in background_tiles:
            self.window.blit(bg_image, tile)
        for obj in objects:
            obj.show_object(self.window, offset_x)
        player.show_object(self.window, offset_x)
        pygame.display.update()
    
    def draw_loop(self, player, objects, offset_x):
        for obj in objects:
            obj.show_object(self.window, offset_x)
        player.show_object(self.window, offset_x)
        pygame.display.update()
                
class LevelController():
    def __init__(self, world: OverworldModel, view: Level1View):
        self.world = world
        self.view = view
    
    def debugg(self, x_offset, width, scroll_width, player_mod):
        if ((player_mod.rect.right - x_offset >= width - scroll_width)
        and player_mod.x_vel > 0) or ((player_mod.rect.left - x_offset <= scroll_width)
        and player_mod.x_vel < 0):
            x_offset += player_mod.x_vel
                
    def gameloop(self):
        # block_size = 96
        # fire = FireModel(100, self.world.HEIGHT - block_size - 64, 16, 32)
        # fire.on()
        run = True
        while run:
            self.world.clock.tick(self.world.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.world.player.jump_count < 2:
                        self.world.player.jump()
            self.world.player.player_loop(self.world.FPS)
            # fire.loop()
            self.world.handle_move(self.world.player.obj_model)
            self.view.draw_level(self.world.generate_background("Green.png") , self.world.player, self.world.objects, self.world.offset_x)
            self.debugg(self.world.offset_x, self.world.WIDTH, self.world.scroll_area_width, self.world.player.obj_model)
            
    def start(self):
        pygame.init()
        self.world.generate_trap(100)
        self.world.generate_objects(self.world.trap)
        self.world.generate_player(100, 100, 50, 50)
        
        
                    
    
    def exit():
        pygame.quit()


def main():
    run = True
    m = OverworldModel()
    v = Level1View("Platformer",(1000, 800))
    c = LevelController(m, v)
    
    c.start()
    c.gameloop()
    c.exit()
    quit()

if __name__ == "__main__":
    main()
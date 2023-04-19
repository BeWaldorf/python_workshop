import pygame
from os.path import join
from terrain import TerrainController
from fire import FireController
from player import PlayerController, PlayerModel


class OverworldModel():
    WIDTH: int = 1000 
    HEIGHT: int = 800
    FPS: int = 60
    GRAVITY: int = 1
    PLAYER_SPEED: int = 5
    BLOCK_SIZE: int = 96
    TITLE: str = "Platformer"
    player: PlayerController = None
    trap = player = objects = player_velocity = trap = None

    
    def __init__(self) -> None:
        self.scroll_area_width = 200
        self.offset_x = 0
        self.clock = self.clock = pygame.time.Clock()
        self.fire = None
    
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
    
    def generate_objects(self, fire):
        objects = [
                    TerrainController(0, self.HEIGHT - self.BLOCK_SIZE * 2),
                    TerrainController(self.BLOCK_SIZE * 3, self.HEIGHT - self.BLOCK_SIZE * 4),
                    fire,
                    ]
        for tile in self.generate_floor():
            objects.append(tile)
        
        self.objects = objects
    
    def generate_player(self, x, y, width, heigth):
        self.player = PlayerController(x, y, width, heigth)
        self.player_velocity = self.player.obj_model.VELOCITY * self.PLAYER_SPEED
    
    def generate_trap(self, x):
        y = self.HEIGHT - self.BLOCK_SIZE - 64
        self.trap = FireController(x, y)
    
    
class OverworldView():
    def __init__(self, caption, size_wh):
        pygame.display.set_caption(caption)
        self.screen_width, self.screen_height = size_wh 
        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))       
    
    def draw_level(self, generated_bg, player, objects, offset_x):
        background_tiles, bg_image = generated_bg
        for tile in background_tiles:
            self.window.blit(bg_image, tile)
        #for obj in objects:
        #    obj.draw_object(self.window, offset_x)
        player.draw_object(self.window, offset_x)
        pygame.display.update()
    
                
class OverworldController():
    def __init__(self, world: OverworldModel, world_view: OverworldView):
        self.world = world
        self.world_view = world_view
    
    def debugg(self, x_offset, width, scroll_width, player_mod):
        if ((player_mod.rect.right - x_offset >= width - scroll_width)
        and player_mod.x_vel > 0) or ((player_mod.rect.left - x_offset <= scroll_width)
        and player_mod.x_vel < 0):
            x_offset += player_mod.x_vel
                
    def gameloop(self):
        #self.world.trap.on()
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
            self.world.player.obj_loop(self.world.FPS, self.world_view.window)
            #self.world.trap.obj_loop(self.world_view.window)
            self.world_view.draw_level(self.world.generate_background("Blue.png"),self.world.player,self.world.objects,0)
            # self.world.handle_move(self.world.player.obj_model)
            
            self.debugg(self.world.offset_x, self.world.WIDTH, self.world.scroll_area_width, self.world.player.obj_model)
            pygame.display.update()
            
    
    def start(self):
        pygame.init()
        # self.world.generate_trap(100)
        # self.world.generate_objects(self.world.trap)
        self.world.generate_player(100, 100, 50, 50)
        self.world_view.draw_level(self.world.generate_background("Green.png") , self.world.player, self.world.objects, self.world.offset_x)
        
        
                    
    
    def exit(self):
        pygame.quit()
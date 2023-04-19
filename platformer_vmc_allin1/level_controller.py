import os
import pygame
from Models.overworld_model import OverworldModel as World
from Models.block_model import BlockModel
from Models.fire_model import FireModel

from Views.level1_view import Level1View

class LevelController():

    def __init__(self, world, view):
        self.world = World()
        self.view = Level1View()
    
    def sprite_loader():
        pass
    
    
    
    def handle_move(player, objects):
        keys = pygame.key.get_pressed()
    
        player.x_vel = 0
        collide_left = collide(player, objects, -PLAYER_VEL * 2)
        collide_right = collide(player, objects, PLAYER_VEL * 2)
    
        if keys[pygame.K_LEFT] and not collide_left:
            player.move_left(PLAYER_VEL)
        if keys[pygame.K_RIGHT] and not collide_right:
            player.move_right(PLAYER_VEL)
    
        vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
        to_check = [collide_left, collide_right, *vertical_collide]
    
        for obj in to_check:
            if obj and obj.name == "fire":
                player.make_hit()
                
    
    def gameloop():
        clock = pygame.time.Clock()
        background, bg_image = get_background("Blue.png")
    
        block_size = 96
    
        player = PlayerModel(100, 100, 50, 50)
        fire = FireModel(100, HEIGHT - block_size - 64, 16, 32)
        fire.on()
        floor = [BlockModel(i * block_size, HEIGHT - block_size, block_size)
                for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
        objects = [*floor, BlockModel(0, HEIGHT - block_size * 2, block_size),
                BlockModel(block_size * 3, HEIGHT - block_size * 4, block_size), fire]
    
        offset_x = 0
        scroll_area_width = 200
    
        run = True
        while run:
            clock.tick(FPS)
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and player.jump_count < 2:
                        player.jump()
    
            player.loop(FPS)
            fire.loop()
            handle_move(player, objects)
            draw(window, background, bg_image, player, objects, offset_x)
    
            if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                    (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
                offset_x += player.x_vel

    def create_block(x, y, size):
        super().__init__(x, y, size, size)
        block = get_block(size)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)

    def get_block(size):
        path = join("assets", "Terrain", "Terrain.png")
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        rect = pygame.Rect(96, 0, size, size)
        surface.blit(image, (0, 0), rect)
        return pygame.transform.scale2x(surface) 
    
    def start():
        pygame.init()            
    
    def exit():
        pygame.quit()
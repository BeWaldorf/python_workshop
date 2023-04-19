from os import listdir
from os.path import isfile, join
import pygame

class OverworldObjectView():
    def __init__(self, asset_path, size_wh) -> None:
        self.asset_folder = asset_path
        self.source_path = join(self.asset_folder, self.source_name)
        self.width, self.heigth = size_wh
        
    
    def load_object_sprite_sheets(self, direction = False):
        sprite_sources = []
        for file in listdir(self.source_path):
            if isfile(join(self.source_path, file)):
                sprite_sources.append(file)
        # images = [file for file in listdir(self.source_path) if isfile(join(self.source_path, file))]
        # Eventueel list comprehension?
        all_sprites = {}
        for sprite_source in sprite_sources:
            sprite_sheet = pygame.image.load(join(self.source_path, sprite_source)).convert_alpha()
            sprites = []
            for i in range(sprite_sheet.get_width() // self.width):
                surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * self.width, 0, self.width, self.height)
                surface.blit(sprite_sheet, (0, 0), rect)
                sprites.append(pygame.transform.scale2x(surface))
            if direction:
                all_sprites[pygame.image.replace(".png", "") + "_right"] = sprites
                all_sprites[pygame.image.replace(".png", "") + "_left"] = pygame.flip(sprites)
            else:
                all_sprites[pygame.image.replace(".png", "")] = sprites
        return all_sprites
    
    def draw_overworld_object(self, object_to_draw, offset_x):
        self.window.blit(object_to_draw.image, (object_to_draw.rect.x - offset_x, object_to_draw.rect.y))
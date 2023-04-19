import pygame
from overworld_object import OverworldObjectModel, OverworldObjectView, OverworldObjectController
from os.path import join

F_BLOCK_SIZE = 96

class TerrainModel(OverworldObjectModel):
    BLOCK_SIZE = F_BLOCK_SIZE
    def __init__(self, x, y):
        super().__init__(x, y, self.BLOCK_SIZE, self.BLOCK_SIZE)
        self.current_x = x
        self.current_y = y
        self.surface = pygame.Surface((self.BLOCK_SIZE, self.BLOCK_SIZE), pygame.SRCALPHA, 32)
    
class TerrainView(OverworldObjectView):
    SPRITE_WIDTH = SPRITE_HEIGHT = F_BLOCK_SIZE
    def __init__(self, asset_path: str, size: tuple[int, int], disp_surfaces_ir: tuple[pygame.Surface, pygame.Surface]):
        super().__init__(asset_path, size, disp_surfaces_ir)
        """ self.asset_folder = asset_path """
        """ self.size = size """
        """ self.surface = pygame.Surface((size, size), pygame.SRCALPHA, 32) """
        """ self.rect = pygame.Rect(96, 0, size, size) """
        """ self.sprites = pygame.image.load(asset_path).convert_alpha() """
        """ self.current_sprite = pygame.image.load(asset_path).convert_alpha() """
        """ self.surface.blit(self.current_sprite, (0, 0), self.rect) """
        """ terrain_unit = pygame.transform.scale2x(self.surface) """
        """ self.current_sprite.blit(terrain_unit, (0,0)) """
        """ self.mask = pygame.mask.from_surface(self.current_sprite) """
        """ self.image = self.current_sprite = pygame.image.load(asset_path).convert_alpha() """
        """ self.surface.blit(self.image, (0, 0), self.rect) """
        """  """
    
    """ def load_object_sprite_sheets(self): """
    """     sprites = pygame.image.load(self.asset_folder).convert_alpha """
    """     return sprites """
    """  """
    """ def draw_unit(self, surface): """
    """     self.current_sprite.blit(surface, (0,0)) """
        
class TerrainController(OverworldObjectController):
    BLOCK_SIZE = F_BLOCK_SIZE
    def __init__(self, x, y):
        super().__init__(x, y,self.BLOCK_SIZE, self.BLOCK_SIZE)
        
    
    def _generate_mv(self):
        self.obj_model = TerrainModel(self.x_coord, self.y_coord)
        disp_surf = (self.obj_model.image, self.obj_model.rect)
        self.obj_view = TerrainView("assets\Terrain", (self.BLOCK_SIZE,self.BLOCK_SIZE), disp_surf)
        
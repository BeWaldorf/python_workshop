import os
import sys
models_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Models'))
sys.path.append(models_path)

from Models.overworld_object_model import OverworldObjectModel
from Views.overworld_object_view import OverworldObjectView



class OverworldObjectController():
    x_coord, y_coord, name, obj_width, obj_height, obj_model, obj_view, my_rect, obj_type = None
    
    def __init__(self, x, y, rectangle, obj_type = None):
        self.my_rect = rectangle
        self.x_coord = x
        self.y_coord = y
        self.type = obj_type
        
        self.generate_mv()
        
    def generate_mv(self):
        self.obj_model = OverworldObjectModel(self.x_coord, self.y_coord, self.my_rect, self.name)
        self.obj_view = OverworldObjectView (self.my_rect, self.obj_model.SOURCEFOLDER_PATH, self.obj_model.source_name, self.obj_model.get_size_wh())
    
        
        
        
        
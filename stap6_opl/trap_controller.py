from trap_model import TrapModel
from trap_view import TrapView
from overworld_object_controller import OverworldObjectController

class TrapController(OverworldObjectController):
    def __init__(self, window, x, y) -> None:
        super().__init__(window)
        self._make_mv(x, y, window)
    
    def _make_mv(self, x, y, window) -> None:
        self.obj_model = TrapModel(x, y, "Trap")
        self.obj_view = TrapView(window, (16, 32))
    
    def obj_tick(self):
        self.obj_model.logic_loop()
        self.obj_view.draw_loop(self.obj_model.get_image(), self.obj_model.get_coords())

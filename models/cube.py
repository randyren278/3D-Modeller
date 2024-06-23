from models.primitive import Primitive

class Cube(Primitive):
    def __init__(self):
        super(Cube, self).__init__()
        self.call_list = G_OBJ_CUBE

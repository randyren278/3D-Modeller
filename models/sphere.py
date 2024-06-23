from models.primitive import Primitive

class Sphere(Primitive):
    def __init__(self):
        super(Sphere, self).__init__()
        self.call_list = G_OBJ_SPHERE

from models.primitive import Primitive
from OpenGL.GL import *
from OpenGL.GLU import *

class Sphere(Primitive):
    def __init__(self):
        super(Sphere, self).__init__()
        self.call_list = self.create_call_list()

    def create_call_list(self):
        """ Create a display list for the sphere """
        call_list = glGenLists(1)
        glNewList(call_list, GL_COMPILE)
        quadric = gluNewQuadric()
        gluSphere(quadric, 1.0, 32, 32)
        glEndList()
        return call_list

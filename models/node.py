import numpy
import random
from OpenGL.GL import *
from utils.colors import COLORS, MIN_COLOR, MAX_COLOR

print("Node module loaded")


class Node(object):
    def __init__(self):
        self.color_index = random.randint(MIN_COLOR, MAX_COLOR)
        self.translation_matrix = numpy.identity(4)
        self.scaling_matrix = numpy.identity(4)
        self.selected = False

    def render(self):
        """ Renders the item to the screen """
        glPushMatrix()
        glMultMatrixf(numpy.transpose(self.translation_matrix))
        glMultMatrixf(self.scaling_matrix)
        cur_color = COLORS[self.color_index]
        glColor3f(cur_color[0], cur_color[1], cur_color[2])
        if self.selected:
            glMaterialfv(GL_FRONT, GL_EMISSION, [0.3, 0.3, 0.3])

        self.render_self()

        if self.selected:
            glMaterialfv(GL_FRONT, GL_EMISSION, [0.0, 0.0, 0.0])
        glPopMatrix()

    def render_self(self):
        raise NotImplementedError("The Abstract Node Class doesn't define 'render_self'")

    def translate(self, x, y, z):
        self.translation_matrix = numpy.dot(
            self.translation_matrix, 
            numpy.array([
                [1, 0, 0, x],
                [0, 1, 0, y],
                [0, 0, 1, z],
                [0, 0, 0, 1]
            ])
        )

    def scale(self, s):
        scale_matrix = numpy.array([
            [s, 0, 0, 0],
            [0, s, 0, 0],
            [0, 0, s, 0],
            [0, 0, 0, 1]
        ])
        self.scaling_matrix = numpy.dot(self.scaling_matrix, scale_matrix)

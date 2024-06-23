import numpy
import math

class Trackball(object):
    def __init__(self, theta=0.0, phi=0.0, distance=1.0):
        self.theta = theta
        self.phi = phi
        self.distance = distance
        self.matrix = self._create_rotation_matrix()

    def drag_to(self, x0, y0, dx, dy):
        self.theta += dy * 0.2
        self.phi += dx * 0.2
        self.matrix = self._create_rotation_matrix()

    def _create_rotation_matrix(self):
        theta = math.radians(self.theta)
        phi = math.radians(self.phi)

        cos_t, sin_t = math.cos(theta), math.sin(theta)
        cos_p, sin_p = math.cos(phi), math.sin(phi)

        rotation_matrix = numpy.array([
            [cos_p, -sin_p * cos_t, sin_p * sin_t, 0.0],
            [sin_p, cos_p * cos_t, -cos_p * sin_t, 0.0],
            [0.0, sin_t, cos_t, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])

        return rotation_matrix

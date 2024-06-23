import numpy as np

class Trackball(object):
    def __init__(self, size=0.8, speed=0.1):
        self.size = size
        self.speed = speed
        self.matrix = np.identity(4)

    def drag_to(self, start_x, start_y, dx, dy):
        axis = np.array([dy, dx, 0.0])
        angle = self.speed * np.sqrt(dx * dx + dy * dy)
        axis = self._normalize(axis)
        self._rotate(angle, axis)

    def _rotate(self, angle, axis):
        c = np.cos(angle)
        s = np.sin(angle)
        C = 1 - c
        x, y, z = axis
        rmat = np.array([
            [x * x * C + c, x * y * C - z * s, x * z * C + y * s],
            [y * x * C + z * s, y * y * C + c, y * z * C - x * s],
            [z * x * C - y * s, z * y * C + x * s, z * z * C + c]
        ])
        tmat = np.identity(4)
        tmat[:3, :3] = rmat
        self.matrix = np.dot(self.matrix, tmat)

    def _normalize(self, v):
        norm = np.linalg.norm(v)
        if norm == 0: 
           return v
        return v / norm

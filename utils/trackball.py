import numpy as np

class Trackball:
    def __init__(self, theta=0, distance=5):
        self.theta = theta
        self.distance = distance
        self.matrix = np.identity(4)

    def drag_to(self, old_x, old_y, new_x, new_y):
        # Implement drag logic to update the matrix for rotation
        # This is a placeholder for actual implementation
        dx = new_x - old_x
        dy = new_y - old_y
        angle = np.sqrt(dx * dx + dy * dy) / self.distance
        self.matrix = self._rotation_matrix(angle, dx, dy) @ self.matrix

    def _rotation_matrix(self, angle, dx, dy):
        # Create a rotation matrix given an angle and a vector (dx, dy)
        c, s = np.cos(angle), np.sin(angle)
        axis = np.array([dx, dy, 0])
        axis = axis / np.linalg.norm(axis)
        x, y, z = axis
        return np.array([
            [c + (1 - c) * x * x, (1 - c) * x * y - s * z, (1 - c) * x * z + s * y, 0],
            [(1 - c) * y * x + s * z, c + (1 - c) * y * y, (1 - c) * y * z - s * x, 0],
            [(1 - c) * z * x - s * y, (1 - c) * z * y + s * x, c + (1 - c) * z * z, 0],
            [0, 0, 0, 1]
        ])

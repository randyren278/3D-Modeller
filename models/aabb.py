import numpy

class AABB(object):
    """ Axis-Aligned Bounding Box """
    def __init__(self, min_point, max_point):
        self.min_point = numpy.array(min_point)
        self.max_point = numpy.array(max_point)

    def ray_hit(self, start, direction, mat):
        """ Check if a ray hits the AABB """
        # Transform the start and direction into the AABB's coordinate space
        inv_mat = numpy.linalg.inv(mat)
        start = numpy.dot(inv_mat, numpy.append(start, 1))[:3]
        direction = numpy.dot(inv_mat, numpy.append(direction, 0))[:3]
        direction /= numpy.linalg.norm(direction)

        # Slab method for ray-AABB intersection
        tmin = (self.min_point - start) / direction
        tmax = (self.max_point - start) / direction

        t1 = numpy.minimum(tmin, tmax)
        t2 = numpy.maximum(tmin, tmax)

        t_near = numpy.max(t1)
        t_far = numpy.min(t2)

        if t_near > t_far or t_far < 0:
            return False, None

        return True, t_near

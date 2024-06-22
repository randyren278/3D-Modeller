from models.node import Node

class Scene(object):
    PLACE_DEPTH = 15.0

    def __init__(self):
        self.node_list = list()
        self.selected_node = None

    def add_node(self, node):
        """ Add a new node to the scene """
        self.node_list.append(node)

    def render(self):
        """ Render the scene """
        for node in self.node_list:
            node.render()

    def pick(self, start, direction, mat):
        """ Execute selection """
        if self.selected_node is not None:
            self.selected_node.select(False)
            self.selected_node = None

        mindist = float('inf')
        closest_node = None
        for node in self.node_list:
            hit, distance = node.pick(start, direction, mat)
            if hit and distance < mindist:
                mindist, closest_node = distance, node

        if closest_node is not None:
            closest_node.select()
            closest_node.depth = mindist
            closest_node.selected_loc = start + direction * mindist
            self.selected_node = closest_node

    def move_selected(self, start, direction, inv_modelview):
        """ Move the selected node, if there is one """
        if self.selected_node is None: return

        node = self.selected_node
        depth = node.depth
        oldloc = node.selected_loc
        newloc = (start + direction * depth)
        translation = newloc - oldloc
        pre_tran = numpy.array([translation[0], translation[1], translation[2], 0])
        translation = inv_modelview.dot(pre_tran)
        node.translate(translation[0], translation[1], translation[2])
        node.selected_loc = newloc

    def rotate_selected_color(self, forwards):
        """ Rotate the color of the currently selected node """
        if self.selected_node is None: return
        self.selected_node.rotate_color(forwards)

    def scale_selected(self, up):
        """ Scale the current selection """
        if self.selected_node is None: return
        self.selected_node.scale(up)

    def place(self, shape, start, direction, inv_modelview):
        """ Place a new node """
        new_node = None
        if shape == 'sphere': new_node = Sphere()
        elif shape == 'cube': new_node = Cube()
        elif shape == 'figure': new_node = SnowFigure()

        self.add_node(new_node)
        translation = (start + direction * self.PLACE_DEPTH)
        pre_tran = numpy.array([translation[0], translation[1], translation[2], 1])
        translation = inv_modelview.dot(pre_tran)
        new_node.translate(translation[0], translation[1], translation[2])

import numpy
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from models.scene import Scene
from models.cube import Cube
from models.sphere import Sphere
from models.snowfigure import SnowFigure
from viewer.interaction import Interaction
from utils.trackball import Trackball
from utils.colors import COLORS

class Viewer(object):
    def __init__(self):
        """ Initialize the viewer. """
        self.init_interface()
        self.init_opengl()
        self.init_primitives()  # Add this line to initialize display lists
        self.init_scene()
        self.init_interaction()


    def init_interface(self):
        """ Initialize the window and register the render function """
        glutInit()
        glutInitWindowSize(640, 480)
        glutCreateWindow("3D Modeller")
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutDisplayFunc(self.render)

    def init_opengl(self):
        """ Initialize the OpenGL settings to render the scene """
        self.inverseModelView = numpy.identity(4)
        self.modelView = numpy.identity(4)

        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)

        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, GLfloat_4(0, 0, 1, 0))
        glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, GLfloat_3(0, 0, -1))

        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)
        glClearColor(0.4, 0.4, 0.4, 0.0)

    def init_scene(self):
        """ Initialize the scene object and initial scene """
        self.scene = Scene()
        self.create_sample_scene()

    def create_sample_scene(self):
        """ Create a sample scene with basic shapes """
        cube_node = Cube()
        cube_node.translate(2, 0, 2)
        cube_node.color_index = 2
        self.scene.add_node(cube_node)

        sphere_node = Sphere()
        sphere_node.translate(-2, 0, 2)
        sphere_node.color_index = 3
        self.scene.add_node(sphere_node)

        hierarchical_node = SnowFigure()
        hierarchical_node.translate(-2, 0, -2)
        self.scene.add_node(hierarchical_node)

    def init_interaction(self):
        """ Initialize user interaction and callbacks """
        self.interaction = Interaction()
        self.interaction.register_callback('pick', self.pick)
        self.interaction.register_callback('move', self.move)
        self.interaction.register_callback('place', self.place)
        self.interaction.register_callback('rotate_color', self.rotate_color)
        self.interaction.register_callback('scale', self.scale)

    def render(self):
        """ The render pass for the scene """
        self.init_view()

        glEnable(GL_LIGHTING)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        loc = self.interaction.translation
        glTranslated(loc[0], loc[1], loc[2])
        glMultMatrixf(self.interaction.trackball.matrix)

        currentModelView = numpy.array(glGetFloatv(GL_MODELVIEW_MATRIX))
        self.modelView = numpy.transpose(currentModelView)
        self.inverseModelView = numpy.linalg.inv(numpy.transpose(currentModelView))

        self.scene.render()

        glDisable(GL_LIGHTING)
        glCallList(G_OBJ_PLANE)
        glPopMatrix()
        glFlush()

    def init_view(self):
        """ Initialize the projection matrix """
        xSize, ySize = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
        aspect_ratio = float(xSize) / float(ySize)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        glViewport(0, 0, xSize, ySize)
        gluPerspective(70, aspect_ratio, 0.1, 1000.0)
        glTranslated(0, 0, -15)

    def pick(self, x, y):
        """ Execute pick of an object. Selects an object in the scene. """
        start, direction = self.get_ray(x, y)
        self.scene.pick(start, direction, self.modelView)

    def move(self, x, y):
        """ Execute a move command on the scene. """
        start, direction = self.get_ray(x, y)
        self.scene.move_selected(start, direction, self.inverseModelView)

    def rotate_color(self, forward):
        """ Rotate the color of the selected Node. Boolean 'forward' indicates direction of rotation. """
        self.scene.rotate_selected_color(forward)

    def scale(self, up):
        """ Scale the selected Node. Boolean up indicates scaling larger. """
        self.scene.scale_selected(up)

    def place(self, shape, x, y):
        """ Execute a placement of a new primitive into the scene. """
        start, direction = self.get_ray(x, y)
        self.scene.place(shape, start, direction, self.inverseModelView)

    def get_ray(self, x, y):
        """ Generate a ray beginning at the near plane, in the direction that the x, y coordinates are facing """
        self.init_view()

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        start = numpy.array(gluUnProject(x, y, 0.001))
        end = numpy.array(gluUnProject(x, y, 0.999))

        direction = end - start
        direction = direction / numpy.linalg.norm(direction)

        return (start, direction)

    def main_loop(self):
        glutMainLoop()
        
    def init_primitives(self):
        """ Initialize display lists for primitives """
        global G_OBJ_PLANE
        G_OBJ_PLANE = glGenLists(1)
        glNewList(G_OBJ_PLANE, GL_COMPILE)
        glBegin(GL_LINES)
        for i in range(-10, 11):
            glVertex3f(i, 0, -10)
            glVertex3f(i, 0, 10)
            glVertex3f(-10, 0, i)
            glVertex3f(10, 0, i)
        glEnd()
        glEndList()




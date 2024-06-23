from OpenGL.GLUT import *
from utils.trackball import Trackball

class Interaction(object):
    def __init__(self):
        self.pressed = None
        self.translation = [0, 0, 0, 0]
        self.trackball = Trackball()
        self.mouse_loc = None
        self.callbacks = {}

        self.register()

    def register(self):
        glutMouseFunc(self.handle_mouse_button)
        glutMotionFunc(self.handle_mouse_move)
        glutKeyboardFunc(self.handle_keystroke)
        glutSpecialFunc(self.handle_special_key)

    def register_callback(self, name, func):
        if name not in self.callbacks:
            self.callbacks[name] = []
        self.callbacks[name].append(func)

    def trigger(self, name, *args, **kwargs):
        if name in self.callbacks:
            for func in self.callbacks[name]:
                func(*args, **kwargs)

    def handle_mouse_button(self, button, mode, x, y):
        y = glutGet(GLUT_WINDOW_HEIGHT) - y
        self.mouse_loc = (x, y)

        if mode == GLUT_DOWN:
            self.pressed = button
            if button == GLUT_LEFT_BUTTON:
                self.trigger('pick', x, y)
            elif button == GLUT_RIGHT_BUTTON:
                pass  # Initialize trackball here if needed
            elif button == 3:  # Scroll up
                self.translation[2] += 1.0
            elif button == 4:  # Scroll down
                self.translation[2] -= 1.0
        else:
            self.pressed = None
        glutPostRedisplay()

    def handle_mouse_move(self, x, y):
        y = glutGet(GLUT_WINDOW_HEIGHT) - y
        if self.pressed is not None:
            dx = x - self.mouse_loc[0]
            dy = y - self.mouse_loc[1]
            if self.pressed == GLUT_LEFT_BUTTON:
                self.trigger('move', x, y)
            elif self.pressed == GLUT_RIGHT_BUTTON:
                self.trackball.drag_to(self.mouse_loc[0], self.mouse_loc[1], dx, dy)
            self.mouse_loc = (x, y)
            glutPostRedisplay()

    def handle_keystroke(self, key, x, y):
        if key == b's':
            self.trigger('place', 'sphere', x, y)
        elif key == b'c':
            self.trigger('place', 'cube', x, y)
        glutPostRedisplay()

    def handle_special_key(self, key, x, y):
        if key == GLUT_KEY_UP:
            self.trigger('scale', up=True)
        elif key == GLUT_KEY_DOWN:
            self.trigger('scale', up=False)
        elif key == GLUT_KEY_LEFT:
            self.trigger('rotate_color', forward=False)
        elif key == GLUT_KEY_RIGHT:
            self.trigger('rotate_color', forward=True)
        glutPostRedisplay()

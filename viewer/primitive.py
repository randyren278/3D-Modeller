from OpenGL.GL import glGenLists, glNewList, glEndList, glBegin, glEnd, glVertex3f, glColor3f, GL_COMPILE, GL_QUADS, GL_LINES

G_OBJ_PLANE = None
G_OBJ_AXIS = None

def init_primitives():
    global G_OBJ_PLANE, G_OBJ_AXIS

    # Initialize grid
    G_OBJ_PLANE = glGenLists(1)
    glNewList(G_OBJ_PLANE, GL_COMPILE)
    glBegin(GL_LINES)
    for i in range(-10, 11):
        if i == 0:
            glColor3f(1, 0, 0)  # Red axis
        else:
            glColor3f(0.7, 0.7, 0.7)  # Grid color
        glVertex3f(i, -10, 0)
        glVertex3f(i, 10, 0)
        glVertex3f(-10, i, 0)
        glVertex3f(10, i, 0)
    glEnd()
    glEndList()

    # Initialize axis
    G_OBJ_AXIS = glGenLists(1)
    glNewList(G_OBJ_AXIS, GL_COMPILE)
    glBegin(GL_LINES)
    # X axis - red
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(10, 0, 0)
    # Y axis - green
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 10, 0)
    # Z axis - blue
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 10)
    glEnd()
    glEndList()

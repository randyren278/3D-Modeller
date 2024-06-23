from OpenGL.GL import glGenLists, glNewList, glEndList, glBegin, glEnd, glVertex3f, GL_COMPILE, GL_QUADS

G_OBJ_PLANE = None

def init_primitives():
    global G_OBJ_PLANE
    G_OBJ_PLANE = glGenLists(1)
    glNewList(G_OBJ_PLANE, GL_COMPILE)
    glBegin(GL_QUADS)
    for x in range(-5, 5):
        for y in range(-5, 5):
            glVertex3f(x, y, 0)
            glVertex3f(x+1, y, 0)
            glVertex3f(x+1, y+1, 0)
            glVertex3f(x, y+1, 0)
    glEnd()
    glEndList()

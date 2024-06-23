#! /usr/bin/env python
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluUnProject
from OpenGL.GLUT import *

import numpy
from numpy.linalg import norm, inv

from viewer.viewer import Viewer

def main():
    print("Script is starting...")
    try:
        print("Initializing viewer...")
        viewer = Viewer()
        print("Viewer initialized successfully.")
        print("Starting main loop...")
        viewer.main_loop()
    except Exception as e:
        print("An error occurred during initialization or execution:")
        print(str(e))
    print("Script finished.")

if __name__ == "__main__":
    main()

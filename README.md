# 3D Modeller

## Overview

This 3D modeller program allows you to create, manipulate, and view 3D objects in a virtual environment. It uses OpenGL for rendering and provides an intuitive interface for interacting with the 3D scene.

## Features

- Create and place 3D objects (spheres, cubes, and snow figures) in the scene.
- Select and move objects using the mouse.
- Rotate and scale objects using the keyboard.
- Navigate the scene with intuitive mouse controls (pan, zoom, rotate).

## Key Functions and Their Mappings

### Mouse Functions
- **Left Click:** Select objects in the scene.
- **Middle Button (Scroll):** 
  - **Scroll Up:** Zoom in.
  - **Scroll Down:** Zoom out.
- **Mouse Movement:**
  - **Dragging with Left Button:** Move selected object.
  - **Dragging with Middle Button:** Pan the camera view.
  - **Dragging with Right Button:** Rotate the camera view using a virtual trackball.

### Keyboard Functions
- **s:** Place a sphere at the cursor position.
- **c:** Place a cube at the cursor position.
- **f:** Place a snow figure at the cursor position.
- **Arrow Keys:**
  - **Up Arrow:** Scale the selected object up.
  - **Down Arrow:** Scale the selected object down.
  - **Left Arrow:** Rotate the color of the selected object forward.
  - **Right Arrow:** Rotate the color of the selected object backward.

## Components of the Program

### Viewer Class
- Initializes the interface, sets up OpenGL parameters, and manages the rendering loop.
- Handles window creation and setting up the display mode.
- Initializes the scene with sample objects and sets up interaction callbacks.

### Scene Class
- Manages a list of objects (nodes) in the scene.
- Handles rendering of all objects in the scene.
- Executes picking (selection) of objects.
- Manages moving and placing objects in the scene.
- Handles rotating and scaling of selected objects.

### Node and Primitive Classes
- Base class `Node` represents a general scene element.
- `Primitive` class inherits from `Node` and represents basic shapes like `Sphere` and `Cube`.
- `SnowFigure` is an example of a hierarchical node composed of multiple `Sphere` nodes.

### Interaction Class
- Handles user input from the mouse and keyboard.
- Manages callbacks for different actions like picking, moving, placing, rotating, and scaling objects.

### Trackball Class
- Implements a virtual trackball for intuitive camera control.
- Handles rotation, zoom, and pan based on mouse movements.

## Running the Program

### Prerequisites

Make sure you have the required Python packages installed. You can install them using the `requirements.txt` file:

```bash
pip install -r requirements.txt

python main.py
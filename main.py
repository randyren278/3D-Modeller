<<<<<<< HEAD
import sys
import os

# Add the current directory and the 'viewer' directory to the sys.path
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), 'viewer'))

print("Script is starting...")

try:
    from viewer.viewer import Viewer
    print("Successfully imported Viewer from viewer.viewer")
except ImportError as e:
    print(f"Error importing Viewer: {e}")
    sys.exit(1)
=======
print("Script is starting...")

from viewer.viewer import Viewer
>>>>>>> 46e23fdcf5bc0bda441a75d40b641eb56b65226a

if __name__ == "__main__":
    print("Starting the viewer...")
    viewer = Viewer()
    viewer.main_loop()
    print("Viewer started.")

print("Script is starting...")

from viewer.viewer import Viewer

if __name__ == "__main__":
    print("Starting the viewer...")
    viewer = Viewer()
    viewer.main_loop()
    print("Viewer started.")

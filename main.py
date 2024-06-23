import sys
sys.setrecursionlimit(2000)

print("Script is starting...")

try:
    from viewer import Viewer
    print("Initializing viewer...")
    viewer = Viewer()
    print("Starting main loop...")
    viewer.main_loop()
except Exception as e:
    print("An error occurred during initialization or execution:")
    print(e)

print("Script finished.")

#! /usr/bin/env python

def main():
    print("Script is starting...")
    try:
        from viewer.viewer import Viewer
        print("Initializing viewer...")
        viewer = Viewer()
        print("Viewer initialized successfully.")
        print("Starting main loop...")
        viewer.main_loop()
    except Exception as e:
        print(f"An error occurred during initialization or execution:\n{e}")
    finally:
        print("Script finished.")

if __name__ == "__main__":
    main()

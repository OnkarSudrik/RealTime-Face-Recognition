import dlib
import face_recognition
import cv2
import sys
import platform
import numpy as np

def check_library_version(library_name, version):
    try:
        library = __import__(library_name)
        if hasattr(library, "__version__"):
            print(f"{library_name} version:", library.__version__)
        else:
            print(f"{library_name} version is not available.")
    except ImportError:
        print(f"{library_name} is not installed.")

# Check dlib version
check_library_version("dlib", dlib.__version__)

# Check face_recognition version
check_library_version("face_recognition", face_recognition.__version__)

# Check OpenCV (cv2) version
check_library_version("cv2", cv2.__version__)

# Check NumPy version
check_library_version("numpy", np.__version__)

# Check Python version
print("Python version:", sys.version)

# Get the OS name
os_name = platform.system()

# Get the OS version
os_version = platform.release()

# Print the OS name and version
print(f"Operating System: {os_name}")
print(f"OS Version: {os_version}")

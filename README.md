# Real-Time Face Recognition Project

![Project Preview](link_to_your_project_video.gif)

## Overview

This project is a real-time face recognition system that can recognize famous celebrities as well as faces of people you want to add to its database. It uses Python and OpenCV along with the Face Recognition library to perform real-time face recognition with a user-friendly interface. The system provides a confidence level for each recognized face and indicates whether a face is unknown.

## Features

- Recognizes faces in real-time using your computer's webcam.
- Maintains a database of known faces from the "Faces" directory.
- Calculates and displays confidence levels for each recognized face.
- Highlights recognized faces with green bounding boxes and unknown faces with red bounding boxes.
- Easy-to-use and user-friendly interface.

## Prerequisites

Before you get started, make sure you have the following prerequisites installed on your system:

- Python 3.x
- OpenCV
- Face Recognition
- Other dependencies (refer to [Requirements.txt](Requirements.txt) for details)

## Installation and Usage

Follow these steps to set up and use the Real-Time Face Recognition Project:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/RealTime_Face_Recognition_project.git
   ```

2. Navigate to the project directory:

   ```bash
   cd RealTime_Face_Recognition_project
   ```

3. Install the required dependencies by running:

   ```bash
   pip install -r Requirements.txt
   ```

4. Prepare your dataset of known faces:
   - Organize your face images in the "Faces" directory following the structure mentioned below:

     ```
     ├── Faces
     │   ├── Celebrity_1
     │   │   ├── celebrity1_1.jpg
     │   │   ├── celebrity1_2.jpg
     │   │   └── ...
     │   ├── Celebrity_2
     │   │   ├── celebrity2_1.jpg
     │   │   ├── celebrity2_2.jpg
     │   │   └── ...
     │   └── ...
     ```

   - The project will recognize faces from subdirectories under the "Faces" directory, with each subdirectory representing a person's name.

5. Run the main project file:

   ```bash
   python main.py
   ```

6. The project will open a webcam window and start recognizing faces in real-time.

7. Press 'q' or Esc (27) to exit the webcam feed.

## Configuration

- You can adjust the face matching threshold in the `main.py` file by modifying the `face_match_threshold` parameter in the `FaceRec` class constructor. This threshold determines the confidence level for recognizing a face.

## Demo

[Link to a demo video showcasing the project in action](https://github.com/OnkarSudrik/RealTime-Face-Recognition/blob/main/Facial_Recoginition_System.mp4)

## License

This project is licensed under the MIT License - see the [LICENSE](https://raw.githubusercontent.com/runwayml/model-face-recognition/master/LICENSE) file for details.

## Acknowledgments

- Special thanks to the [Face Recognition library](https://github.com/ageitgey/face_recognition) for providing the face recognition functionality.

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub pull request process.

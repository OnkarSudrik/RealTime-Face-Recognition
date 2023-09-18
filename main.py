import cv2
import face_recognition
import os
import numpy as np
import math

class FaceRec:
    def __init__(self, face_match_threshold=0.5):
        # Initialize known face encodings, names, and face matching threshold
        self.known_face_encodings = []
        self.known_face_names = []
        self.face_match_threshold = face_match_threshold
        # Encode known faces
        self.encode_faces()

    def encode_faces(self):
        # Clear previous known face data
        self.known_face_encodings = []
        self.known_face_names = []

        # Loop through folders containing face images
        for person_folder in os.listdir('Faces'):
            person_name = os.path.basename(person_folder)
            person_encodings = []

            # Load and encode each face image in the folder
            for image in os.listdir(os.path.join('Faces', person_folder)):
                face_image = face_recognition.load_image_file(os.path.join('Faces', person_folder, image))
                face_encodings = face_recognition.face_encodings(face_image)

                for face_encoding in face_encodings:
                    person_encodings.append(face_encoding)

            if person_encodings:
                # Calculate the average face encoding for the person
                avg_face_encoding = np.mean(person_encodings, axis=0)
                self.known_face_encodings.append(avg_face_encoding)
                self.known_face_names.append(person_name)

    def recognize_faces(self, frame):
        # Detect face locations and encodings in the input frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Compare the detected face with known faces
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)

            # Find the best match for the detected face
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
                confidence = self.face_confidence(face_distances[best_match_index])
                tag_color = (0, 255, 0) if float(confidence[:-1]) > 50.0 else (0, 0, 255)
            else:
                name = "Unknown"
                confidence = "N/A"
                tag_color = (0, 0, 128)

            # Draw a rectangle around the detected face and display name and confidence
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), tag_color, 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, f'{name} {confidence}', (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        return frame

    def face_confidence(self, face_distance):
        # Calculate confidence based on face distance from the matching threshold
        range_ = (1.0 - self.face_match_threshold)
        linear_value = (1.0 - face_distance) / (range_ * 2.0)

        if face_distance > self.face_match_threshold:
            return str(round(linear_value * 100, 2)) + '%'
        else:
            value = (linear_value + ((1.0 - linear_value) * math.pow((linear_value - 0.5) * 2, 2.0))) * 100
            return str(round(value, 2)) + '%'

if __name__ == "__main__":
    try:
        # Initialize the face recognizer with a specified matching threshold
        face_recognizer = FaceRec(face_match_threshold=0.6)
        # Open a video capture stream from the webcam
        video_capture = cv2.VideoCapture(0)
        video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        while True:
            # Read a frame from the webcam
            ret, frame = video_capture.read()
            if not ret:
                break

            # Recognize faces in the frame and display results
            frame = face_recognizer.recognize_faces(frame)
            cv2.imshow('Face Recognition', frame)

            # Exit the loop on 'q' key or Esc key (27)
            if cv2.waitKey(1) & 0xFF in (ord('q'), 27):
                break

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Release the video capture and close OpenCV windows
        video_capture.release()
        cv2.destroyAllWindows()

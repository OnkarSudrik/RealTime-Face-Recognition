import os
import cv2
import face_recognition

# Input directory containing the images
input_directory = "D:\\Project\\RealTime_Face_Recoginition_project\\Faces\\Conor_McGregor"
# Output directory where cropped and renamed images will be saved
output_directory = "D:\\Project\\RealTime_Face_Recoginition_project\\Faces\\Conor_McGregor_Cropped"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through each image file in the input directory
for filename in os.listdir(input_directory):
    image_path = os.path.join(input_directory, filename)

    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Detect faces in the image using face_recognition
    face_locations = face_recognition.face_locations(image)

    # If one or more faces are detected, crop and save them
    if face_locations:
        # Assume there is only one face per image for simplicity
        top, right, bottom, left = face_locations[0]
        face = image[top:bottom, left:right]

        # Create a new filename (e.g., Conor_McGregor1.jpg)
        new_filename = f"Conor_McGregor_{len(os.listdir(output_directory)) + 1}.jpg"
        output_path = os.path.join(output_directory, new_filename)

        # Save the cropped face as Conor_McGregor1.jpg (or similar)
        cv2.imwrite(output_path, face)
        print(f"Saved: {output_path}")

print("Face cropping and renaming completed.")

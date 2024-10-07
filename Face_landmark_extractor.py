import os
import cv2
import mediapipe as mp

# Disable TensorFlow OneDNN optimization (if using TensorFlow in the same environment)
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)

# Define the path of the single image
image_path = 'D:/image.jpg'

# Open a text file to store the landmark data
with open('landmarks_output.txt', 'w') as file:
    # Write header to the file
    file.write(f"{'IMAGE_NAME':<15}   {'LANDMARK_INDEX':<15}   {'X_PIXEL':<10}   {'Y_PIXEL':<10}   {'Z_COORDINATE'}\n")

    # Read the image
    frame = cv2.imread(image_path)

    if frame is None:
        print(f"Could not read {image_path}")
    else:
        height, width, _ = frame.shape  # Get the actual width and height of the image

        # Convert the image from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Loop through each of the 468 (or 478) landmarks
                for idx, landmark in enumerate(face_landmarks.landmark):
                    # Denormalize the x and y coordinates by multiplying by the actual width and height
                    x_pixel = int(landmark.x * width)   # Denormalize x using the width (e.g., 1920)
                    y_pixel = int(landmark.y * height)  # Denormalize y using the height (e.g., 1080)
                    z_value = landmark.z  # z is a relative depth value

                    # Write the landmark data to the file (image name, landmark index, x, y in pixels, z)
                    file.write(f"{os.path.basename(image_path):<15}   {idx:<15}   {x_pixel:<10}   {y_pixel:<10}   {z_value:<15.6f}\n")

                    # Draw a circle for each landmark on the image
                    cv2.circle(frame, (x_pixel, y_pixel), 2, (0, 255, 0), -1)  # Green color, radius 2

        # Display the image with landmarks
        cv2.imshow('Landmarks', frame)
        cv2.waitKey(0)  # Wait for a key press to close the image window

        # Save the image with landmarks
        output_image_path = f'output_landmarks_{os.path.basename(image_path)}'
        cv2.imwrite(output_image_path, frame)

# Close the file
file.close()

print(f"Finished processing {os.path.basename(image_path)} and saving landmark data.")

Face Mesh Landmark Extraction

This project uses the "MediaPipe Face Mesh solution" to detect facial landmarks in a single image and extract their **x**, **y**, and **z** coordinates. The coordinates are written to a `.txt` file, and the image is saved with landmarks overlaid on the face.

Table of Contents
- [Introduction]
- [Features]
- [Requirements]
- [Installation]
- [Usage]
- [Output]
- [Project Structure]

Introduction
This project detects facial landmarks from an input image using MediaPipe's Face Mesh. It extracts the **x**, **y** pixel coordinates, and the **z** depth coordinate for each of the 468 landmarks and saves them to a `.txt` file. It also generates an image with the detected landmarks drawn over the face.

Features
- Detects 468 face mesh landmarks using "MediaPipe".
- Writes the landmark coordinates (x, y in pixels, z as relative depth) to a text file.
- Saves the processed image with the landmarks drawn as small circles.
- Processes a single image with customizable input/output paths.

Requirements
- Python 3.x
- OpenCV (`opencv-python`)
- MediaPipe

Installation
1. Clone the Repository:
    ```bash
    git clone https://github.com/yourusername/face-mesh-landmarks.git
    cd face-mesh-landmarks
    ```

2. Install the Required Libraries:
    Install the dependencies using pip:
    ```bash
    pip install opencv-python mediapipe
    ```

Usage
1. Set the Image Path:  
   Update the `image_path` variable in the script with the location of your image. The default path is set to `'D:/images/image_1.jpg'`.

2. Run the Script:  
   Execute the Python script to extract face mesh landmarks and save the output.
   ```bash
   python face_mesh_landmarks.py
   ```

3. View the Results:  
   The script will output two files:
   - A `.txt` file with the x, y, z coordinates of the landmarks.
   - An image file with landmarks drawn on the original image.

Example:
```python
# Define the path of the single image
image_path = 'D:/images/image_1.jpg'
```

Once you run the script, it will output:
- `landmarks_output.txt`: This contains the landmark coordinates.
- `output_landmarks_image_1.jpg`: The image with face landmarks.

Output
1. Landmark Coordinates File (`landmarks_output.txt`)
This file will contain the following columns:
- **IMAGE_NAME**: The name of the image processed.
- **LANDMARK_INDEX**: The index number of the landmark (0-467).
- **X_PIXEL**: The x-coordinate of the landmark in pixel values.
- **Y_PIXEL**: The y-coordinate of the landmark in pixel values.
- **Z_COORDINATE**: The z-coordinate, which is a relative depth value.

Sample output:
```
IMAGE_NAME      LANDMARK_INDEX   X_PIXEL    Y_PIXEL    Z_COORDINATE
image_1.jpg     0                500        600        0.003402
image_1.jpg     1                520        580        0.003600
...
```

2. Output Image
An image with the face mesh landmarks drawn as green circles will be saved with the filename `output_landmarks_<image_name>.jpg`.

Project Structure
```
face-mesh-landmarks/
│
├── face_mesh_landmarks.py    # Main Python script to run the project
├── README.md                 # Project documentation
├── landmarks_output.txt      # Generated output file containing the landmarks (created after running the code)
├── output_landmarks_image_1.jpg  # Image with landmarks (created after running the code)
└── images/
      └── image_1.jpg         # Example input image (replace with your own image)
```

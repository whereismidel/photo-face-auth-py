# Face Authentication System

This repository contains a basic face authentication system using Python, OpenCV, and the `face_recognition` library. The system allows you to register a face, capture an authentication image, recognize faces, and display recognized faces with bounding boxes.

## Requirements

- Python 3.x
- OpenCV
- face_recognition
- numpy (usually installed as a dependency of face_recognition)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/photo-face-auth-py.git
    cd photo-face-auth-py
    ```

2. Install the required libraries:
    ```bash
    pip install opencv-python face_recognition numpy
    ```

## Usage

### Register a Face

To register a face, run the following function:

```python
register_face('your_face_name')
```

This will open the webcam. Press 's' to save the captured face or 'q' to cancel. The face image will be saved in the registered directory with the provided title.

Capture an Authentication Image
To capture an image for authentication purposes, use:

python
Copy code
capture_auth_image('your_face_name')
This will open the webcam. Press 's' to save the authentication image or 'q' to cancel. The image will be saved in the auth directory with the provided title followed by _auth.

### Recognize a Face
To recognize a face, use:

```python
result, image, face_locations = recognize_face('path_to_registered_face', 'path_to_auth_image')
```
This function will compare the known face with the authentication image and print whether the face is recognized. It returns a tuple with a boolean indicating if the face was recognized, the image, and the face locations.

### Display Recognized Face with Bounding Box
To display the recognized face with a bounding box, use:

```python
show_face_location(image, face_locations)
```
This will show the image with the face bounded by a green rectangle.

### Code Description
```python
register_face(title)
```
Captures a face image from the webcam.
Saves the captured face in the registered directory with the provided title.
```python
capture_auth_image(title)
```
Captures an authentication image from the webcam.
Saves the captured image in the auth directory with the provided title followed by _auth.
```python
recognize_face(known_face_path, unknown_face_path)
```
Loads the known face image and its encoding.
Loads the unknown face image and converts it to RGB.
Detects faces in the unknown image and compares them with the known face encoding.
Returns a boolean indicating if the face was recognized, the image, and face locations.
```python
show_face_location(image, face_locations)
```
Draws a rectangle around detected faces in the image.
Displays the image with bounding boxes.

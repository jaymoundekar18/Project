# Face Detection Using DeepFace and OpenCV

This project demonstrates how to perform real-time face detection using the [DeepFace](https://github.com/serengil/deepface) library and OpenCV. It captures video from the system's camera, detects faces in real-time, and displays bounding boxes along with the confidence score of the detected faces.

## DeepFace Overview
DeepFace is a Python library for face recognition and facial attribute analysis. It is built on top of state-of-the-art deep learning models and provides a straightforward API for facial analysis tasks. DeepFace makes face recognition accessible and easy to implement by integrating with popular deep learning frameworks like TensorFlow, Keras, and PyTorch.

## App Features
- Real-time face detection using a system camera.
- Bounding box and confidence score display for detected faces.
- Detection fails gracefully for non-front-facing faces.

## Install Required Libraries

- Use the following commands to install the dependencies:

  ```bash
      python -m pip install opencv-python==4.10.0.84
      python -m pip install deepface==0.0.92
  ```

- **Run the Script** Run the script in your terminal or IDE:
  ```bash
      python DeepFace_Face_Detection.py
  ```
## Working

- The script accesses the system camera using OpenCV.
- The camera feed is read in real-time, and each frame is mirrored for a more intuitive experience.
- The DeepFace library processes the frame to detect faces and extract:
  - Confidence level of the face detection.
  - Bounding box coordinates for detected faces.
- OpenCV overlays the bounding box and confidence score on the video feed.
- If no face is detected or the face is not front-facing, a message is displaye

## Usage Instructions
- The live camera feed will be displayed in a new window.
- Press `q` to quit the application.

## Note
- Detection may fail for non-front-facing or partially obscured faces.
- The accuracy depends on the quality of the system's camera.
- Performance may drop under challenging lighting or extreme facial angles.

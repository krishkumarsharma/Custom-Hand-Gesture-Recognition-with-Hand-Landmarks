# Custom Hand Gesture Recognition with Hand Landmarks

This project implements a **custom hand gesture recognition system** using **hand landmarks** detected by [MediaPipe](https://mediapipe.dev/). It allows real-time recognition of custom gestures, which can be used in applications like gesture-controlled interfaces, sign language detection, and interactive projects.

## Features

- Real-time hand detection and tracking
- Extraction of 21 hand landmarks
- Custom gesture recognition
- Easy to train and add new gestures
- Works with webcam input
- Lightweight and efficient for real-time applications

## Technologies Used

- **Python 3.x**
- [OpenCV](https://opencv.org/) – for video capture and image processing
- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands) – for hand detection and landmarks
- **NumPy** – for gesture data processing
- Optional: **Scikit-learn / TensorFlow / PyTorch** – for gesture classification models

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/custom-hand-gesture-recognition.git
cd custom-hand-gesture-recognition

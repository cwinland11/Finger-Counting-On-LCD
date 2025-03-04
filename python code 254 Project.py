import os
import cv2
import time
import numpy as np
import serial
from keras import Sequential
from keras.layers import TFSMLayer

# -----------------------------
# Paths & Model Setup
# -----------------------------
model_path = r"C:\Users\camer\OneDrive\Desktop\Homework and Tools\IT 254\model.savedmodel"
labels_path = r"C:\Users\camer\OneDrive\Desktop\Homework and Tools\IT 254\labels.txt"

# Create an inference-only model using TFSMLayer (Keras 3 compatible)
model = Sequential([
    TFSMLayer(model_path, call_endpoint="serving_default")
])

# Load labels from your text file (one label per line)
with open(labels_path, "r") as f:
    class_names = [line.strip() for line in f.readlines()]
print("Loaded class names:", class_names)

# -----------------------------
# Set up Arduino Serial Connection
# -----------------------------
arduino = serial.Serial('COM4', 9600)  # Ensure 'COM4' matches your system's port
time.sleep(2)  # Allow time for the serial connection to initialize

# -----------------------------
# Set up the Camera
# -----------------------------
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("❌ Cannot open camera")
    exit()

# Set camera resolution to 800x600
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

# Create a resizable window for display
cv2.namedWindow("Webcam Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Webcam Image", 1024, 768)

# -----------------------------
# Main Loop
# -----------------------------
last_print_time = 0
time_interval = 2  # seconds

while True:
    ret, frame = camera.read()
    if not ret:
        print("❌ Failed to grab frame.")
        break

    # Resize the frame to 224x224 for the model (using INTER_CUBIC for better quality)
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_CUBIC)

    # Show the original frame in the window
    cv2.imshow("Webcam Image", frame)

    # Preprocess: convert to float, expand dims, and normalize to [-1, 1]
    image = np.asarray(resized_frame, dtype=np.float32)
    image = np.expand_dims(image, axis=0)
    image = (image / 127.5) - 1

    # Run the prediction (TFSMLayer returns a dictionary)
    prediction = model(image)
    output_key = list(prediction.keys())[0]
    prediction_tensor = prediction[output_key].numpy()

    # Get the index of the highest probability
    index = np.argmax(prediction_tensor)

    # Add 1 to the index to shift the number (Wrap from 9 back to 0)
    index = (index + 1) % 10

    # Confidence score (you can still use this for debugging or monitoring)
    confidence_score = prediction_tensor[0][index]
    class_name = class_names[index]

    # Get the current time to control printing interval
    current_time = time.time()
    if current_time - last_print_time >= time_interval:
        print(f"Class: {class_name} | Confidence: {confidence_score * 100:.2f}%")
        last_print_time = current_time
        # Send the predicted digit (as a character) to Arduino
        arduino.write(str(index).encode())  # Send index as string

    # Exit on ESC key
    if cv2.waitKey(1) == 27:
        break

# Cleanup resources
camera.release()
cv2.destroyAllWindows()
arduino.close()

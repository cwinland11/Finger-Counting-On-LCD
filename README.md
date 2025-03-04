# Finger-Counting-On-LCD
This project uses a camera and a machine learning model to recognize hand gestures and display the corresponding number on an LCD screen. The camera captures images of your hand gestures, and the model predicts which number you are holding up. The predicted number is then sent to an Arduino board, which controls the LCD screen to display the number.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to Build a Finger Counting Display System

Step 1: Understand the Concept The idea behind this project is to recognize how many fingers you're holding up and display the corresponding number on an LCD screen. We achieve this by using a machine learning model that has been trained to recognize different hand gestures. When you hold up your hand in front of the camera, the system will predict the number of fingers based on the gesture, and that number will be displayed on an LCD screen. Additionally, the system will also show a confidence score, indicating how sure the model is about the prediction.

Step 2: Gather the Required Materials Before you can start building, you’ll need the following hardware and software:

Hardware:
Camera: A webcam or any camera that connects to your computer to capture the hand gestures.
Arduino Mega 2560 (or any Arduino board) to interface with the LCD screen.
LCD Screen (1602): Used to display the recognized number and confidence level.
Wires and Breadboard: For connecting your LCD to the Arduino.
Computer: To run the machine learning model and code.
USB cable: To connect the Arduino to your computer.

Software:
Python: For writing the code that will capture images, process them using the model, and send data to the Arduino.
OpenCV: A library for working with images and video.
TensorFlow/Keras: A machine learning framework used for creating and running the model.
Arduino IDE: To program the Arduino and control the LCD screen.

Step 3: Set Up Your Camera and Arduino Start by setting up your webcam. It should be positioned so it can clearly capture your hand gestures. Then, connect the Arduino to your computer and wire the LCD to the Arduino according to the pin configuration you prefer (usually using the pins for RS, E, D4, D5, D6, and D7).

Step 4: Train or Use a Pre-Trained Model To recognize the number of fingers you’re holding up, you’ll need a machine learning model that can classify hand gestures. You can either train your own model using Teachable Machine  // TensorFlow/Keras (which might take time and requires labeled data) or you can use a pre-trained model available online. 

Step 5: Write the Code Once you have your model, write a Python script that captures images from the webcam, sends them to the model, and receives the predictions. Then, the code will send the predicted digit to the Arduino using serial communication. The Arduino will display the digit and confidence score on the LCD screen.

Step 6: Upload the Code to the Arduino Write a simple Arduino program that listens for data from the Python script through the serial port. When the Arduino receives a new digit, it will update the LCD screen with the predicted number and confidence.

Step 7: Test Your System With everything set up, you can now test your system. Hold up your hand in front of the camera and see if the correct number of fingers is displayed on the LCD screen. If the prediction is incorrect, you may need to adjust the model or camera setup to improve accuracy.

Personal Notes: I was going to add the confidence percentage to the bottom row of the LCD, but I couldn't get it to work, any ideas would be appreciated. 

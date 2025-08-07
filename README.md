# 📸 Real-time Color Recognition with OpenCV

This project is a simple yet effective application that uses Python and the OpenCV library to perform real-time color recognition from a webcam feed. The program identifies the color of an object placed in the center of the camera's view and displays its name.

The assignment was completed as part of a training task for Smart Methods.

---

## 🚀 Features
- Real-time video stream from a webcam.
- Identifies a wide range of colors, including vibrant colors (Red, Green, Blue) and neutral shades (White, Black, Grey).
- Displays the recognized color name on the video feed.
- Simple and easy to set up.

---

## 🛠️ Prerequisites
Before you begin, you need to have the following software installed on your system:
- Anaconda: A powerful platform for data science and machine learning, which includes Python and a package manager (conda).
- Visual Studio Code (VS Code): A lightweight but powerful source code editor.

---

## ⚙️ Installation & Setup

### ⬇️ Step 1: Install Python and Libraries

1.  Open Anaconda Prompt.
2.  Create a dedicated environment (Recommended) to avoid conflicts with other projects.

   
    conda create --name color_recognition python=3.9
    
3.  Activate the environment before installing libraries.

   
    conda activate color_recognition
    
4.  Install OpenCV and NumPy using pip.

   
    pip install opencv-python numpy
    
### 📂 Step 2: Prepare the Project Files

1.  Open VS Code.
2.  Go to File -> Open Folder... and select an empty folder for your project.
3.  Create a new file named color_recognition.py and copy the project code into it.

### ▶️ Step 3: Run the Application

To run the code, use the Anaconda Prompt.

1.  Open Anaconda Prompt and activate your environment.

   
    conda activate color_recognition
    
2.  Navigate to your project directory using the cd command.

   
    cd C:\Path\To\Your\Project\Folder
    
3.  Execute the script using the python command.

   
    python color_recognition.py
    
    A new window will open showing your webcam feed. To exit, press the q key.

---

## 🧠 How It Works
- The program captures video frames from your webcam using cv2.VideoCapture().
- It enters a while loop to continuously read each frame.
- The color of the pixel at the center of the frame is analyzed.
- The get_color_name function compares this color's HSV (Hue, Saturation, Value) range to predefined ranges for a wide variety of colors.
- The recognized color name is then displayed on the screen.

---

## 👩‍💻 Author
Developed by Raghad Alrashidi

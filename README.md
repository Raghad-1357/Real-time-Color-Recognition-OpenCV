#📸 Real-time Color Recognition with OpenCV 

This project is a simple yet effective application that uses Python and the OpenCV library to perform real-time color recognition from a webcam feed. The program identifies the color of an object placed in the center of the camera's view and displays its name.

## Features 🚀
- Real-time video stream from a webcam. 🎥
- Identifies a wide range of colors, including vibrant colors (Red, Green, Blue) and neutral shades (White, Black, Grey). 🎨
- Displays the recognized color name on the video feed. ✍️
- Simple and easy to set up. ✅

## Prerequisites 🛠️
Before you begin, you need to have the following software installed on your system:
- Anaconda: A powerful platform for data science and machine learning, which includes Python and a package manager (conda). 🐍
- Visual Studio Code (VS Code): A lightweight but powerful source code editor. 💻

## Installation & Setup ⚙️

Follow these steps to set up the project environment and install the necessary libraries.

### Step 1: Install Python and Libraries ⬇️

1.  Open Anaconda Prompt:
    * Search for "Anaconda Prompt" in your Start Menu and open it.

2.  Create a dedicated environment (Recommended):
    * To avoid conflicts with other projects, create a new virtual environment. You can name it color_recognition.

   
    conda create --name color_recognition python=3.9
    
3.  Activate the environment:
    * You must activate the environment before installing libraries.

   
    conda activate color_recognition
    
4.  Install OpenCV and NumPy:
    * Use pip to install the required libraries within your new environment.

   
    pip install opencv-python numpy
    
### Step 2: Prepare the Project Files 📂

1.  Open VS Code:
    * Open Visual Studio Code.
    * Go to File -> Open Folder... and select an empty folder where you will save your project files.

2.  Create the Python script:
    * Inside VS Code, create a new file named webcam_color_recognition.py.
    * Copy and paste the project code, including the updated list of colors, into this file.

### Step 3: Run the Application ▶️

To run the code, use the Anaconda Prompt. This method ensures that the script runs within the correct environment you set up earlier.

1.  Open Anaconda Prompt (if not already open) and activate your environment:

   
    conda activate color_recognition
    
2.  Navigate to your project directory:
    * Use the cd command to change your current directory to the folder where you saved webcam_color_recognition.py.

   
    cd C:\Path\To\Your\Project\Folder
    
    * Replace C:\Path\To\Your\Project\Folder with the actual path to your project folder.

3.  Run the Python script:
    * Execute the script using the python command.

   
    python webcam_color_recognition.py
    
    A new window will open showing your webcam feed.

### How It Works 🧠

- The program captures video frames from your webcam using cv2.VideoCapture().
- It enters a while loop to continuously read each frame.
- The color of the pixel at the center of the frame is analyzed. 🔍
- The get_color_name function compares this color's HSV (Hue, Saturation, Value) range to predefined ranges for a wide variety of colors, including vibrant shades and neutral tones like white, black, and grey. 🌈
- The recognized color name is then displayed on the screen. 🖼️

To exit the application, simply press the q key on your keyboard while the webcam window is active. 🛑

## License 📜

This project is licensed under the MIT License.

# Smile Detection
### 1.  Description

This code creates a real-time webcam application that detects faces, eyes, and smiles, and displays encouraging messages based on whether a smile is detected.


### 2. How to translate and run the program ?

- Install OpenCV: Ensure OpenCV is installed in your Python environment. If not, use pip install opencv-python.
    ````c
    pip install opencv-python
    ````

- Run and compile the program using the command
    
    ````c
    python main.py
    ````

### 3. How the program is programmed?

- Key steps:

    * Imports necessary libraries: cv2 for computer vision and random (likely for future enhancements).
    * Loads pre-trained classifiers: These are XML files trained to detect faces, eyes, and smiles.
    * Starts webcam: Captures video from your computer's camera.
    * Enters main loop: Continuously processes video frames: 
        - Reads a frame from the camera.
        - Converts the frame to grayscale for efficient processing.
        - Detects faces using the face classifier.
    * For each detected face:
        - Draws a rectangle around the face.
        - Detects eyes within the face region.
        - Draws rectangles around detected eyes.
        - Detects smiles within the face region.
        - Displays a positive message if a smile is detected, otherwise encourages smiling.
        - Displays the processed frame on the screen.

    * Checks for the 'q' key press to quit the program. Releases camera and closes windows: Properly closes resources when the loop ends.

### 4. Links to source code and websites that were used in the solution

-   [OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
   
-   [Haar cascade classifiers]( https://docs.opencv.org/4.8.0/db/d28/tutorial_cascade_classifier.html)

-   [Youtube](https://www.youtube.com/watch?v=_23gclr91P4&list=PL0lO_mIqDDFUAQ2RdAgLp6Tj_fREcxk6T)



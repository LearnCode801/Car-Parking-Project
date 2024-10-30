Here’s a detailed README file for your **Automatic Parking Space Detection and Counting System** project:

```markdown
# Automatic Parking Space Detection and Counting System

## Description

This project automates parking space detection and counting in video footage using computer vision techniques. It leverages OpenCV, NumPy, cvzone, and pickle for data storage.

## Working Method

### Initialization

1. **Imports Necessary Libraries**:
   - OpenCV (cv2)
   - NumPy (np)
   - cvzone
   - pickle

2. **Video Capture**:
   - Sets up video capture using `cv2.VideoCapture` for the `carPark.mp4` video file.

3. **Load Parking Coordinates**:
   - Loads pre-defined parking space coordinates from the `carParkingMarked` file using `pickle.load`, which contains a list of tuples representing the top-left corner coordinates (x, y) for each parking space.

### `checkParkingSpace` Function

- **Input**: Takes a preprocessed image (`imgPro`).
- **Functionality**:
  - Initializes a `spacecounter` to keep track of free spaces.
  - Iterates through the list of parking space coordinates:
    - Extracts coordinates and crops a region of interest (ROI).
    - Counts non-zero pixels in the ROI using `cv2.countNonZero`.
    - Displays the count using `cvzone.putTextRect`.
    - Based on the count threshold (500):
      - If count < 500 (empty space):
        - Draws a green rectangle around the parking space.
        - Increments `spacecounter`.
      - Else (occupied space):
        - Draws a red rectangle.
  - Displays total free spaces and total parking spaces.

### Main Loop

- Processes each frame in the video:
  - Checks if the video has ended and resets if necessary.
  - Reads a frame and converts it to grayscale, applies Gaussian blur, and performs adaptive thresholding to create a binary image.
  - Applies median blur and dilation to enhance parking space regions.
  - Calls `checkParkingSpace` to analyze the preprocessed image.
  - Displays the final processed frame and waits for a key press.

## How to Use

### Prerequisites

- Python 3.x
- OpenCV: `pip install opencv-python`
- NumPy: `pip install numpy`
- cvzone: `pip install cvzone`
- Pickle (usually included in standard Python installations)

### Download the Code

1. Clone the repository from GitHub:
   ```bash
   git clone https://<github_repo_url>
   ```

### Run the Script

1. Navigate to the project directory.
2. Ensure `carPark.mp4` and `carParkingMarked` files are in the same directory.
3. Execute the script:
   ```bash
   python main.py
   ```

### Interaction

- Press any key to stop the video processing and close the window.

## Additional Notes

- The `carParkingMarked` file needs to be created beforehand. Use a separate script to manually mark the parking space coordinates in a static image and save them using pickle.
- Consider refining parameters in the image processing pipeline (thresholding, blur levels) for optimal performance with your specific video footage.
- Extend functionality to display parking availability in real-time, log data for analysis, or integrate with a parking management system.


```

Replace `https://<github_repo_url>` and `[Your Name](your-linkedin-url)` with your actual GitHub repository URL and your LinkedIn profile link. Let me know if you need further modifications!

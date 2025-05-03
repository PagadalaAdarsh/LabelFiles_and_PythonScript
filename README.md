# Instructions for Testing the Labeled Video Generation Script (`draw_boxes.py`)

This document outlines the steps to test the provided Python script (`draw_boxes.py`) for generating a labeled video from your labeled data.

## Prerequisites

Before running the script, ensure you have the following installed on your system:

* **Python 3:** Make sure you have Python 3 installed. You can check by running `python --version` or `python3 --version` in your terminal.
* **OpenCV (cv2):** This library is used for video processing and drawing. If you don't have it, you can install it using pip:
    ```bash
    pip install opencv-python
    ```

## Setup

1.  **Download the Repository:** If you haven't already, download or clone this GitHub repository to your local machine.

2.  **Locate the Necessary Files:** Ensure you have the following files within the repository or know their exact paths:
    * **Video File:** The video file you want to label (currently set to `C:/Users/adars/Downloads/FireTruckRecording_Resolution.mp4` in the script).
    * **Labels Directory:** The directory containing the text files with the bounding box coordinates for each frame (currently set to `C:\Users\adars\Downloads\Updated_Yolo_Truck\obj_train_data` in the script). Each label file should have the same name as the corresponding video frame (e.g., `frame_000001.txt` for the second frame) and contain one object per line in the format: `<class_id> <x_center> <y_center> <width> <height>` (normalized values).
    * **Class Names File:** The file containing the names of your object classes (currently set to `C:\Users\adars\Downloads\Updated_Yolo_Truck\obj.names` in the script), with one class name per line.
    * **The Python Script:** The script named `draw_boxes.py`.

## Running the Script

1.  **Open a Terminal or Command Prompt:** Navigate to the directory where you have saved the `draw_boxes.py` script.

2.  **Run the Script:** Execute the script using the Python interpreter:
    ```bash
    python draw_boxes.py
    ```

3.  **Check the Output:** After the script finishes running, it will print a message indicating the location where the labeled video has been saved (currently set to `C:/Users/adars/Downloads/output_labeled_video.mp4`). Open this video file to view the results. You should see bounding boxes drawn around the detected objects with their corresponding class labels.

## Modifications for Testing

Here are a few modifications you can make to the script to test different aspects:

### 1. Changing Input/Output Paths:

* **Input Video:** To test with a different video, modify the `video_path` variable at the beginning of the script to the new video file's path. For example:
    ```python
    video_path = "path/to/your/new_video.mp4"
    ```
* **Labels Directory:** If your labeled data is in a different location, update the `labels_dir` variable:
    ```python
    labels_dir = r"path/to/your/new_labels_directory"
    ```
* **Class Names File:** If you have a different `obj.names` file, update the `names_path` variable:
    ```python
    names_path = r"path/to/your/new_obj.names"
    ```
* **Output Video:** To save the labeled video to a different location or with a different name, change the `output_video_path` variable:
    ```python
    output_video_path = "path/to/your/new_output_video.mp4"
    ```

    **Remember to save the `draw_boxes.py` script after making any changes.**

### 2. Testing with a Subset of Frames (for faster testing):

You can modify the `while True:` loop to process only a certain number of frames. For example, to process the first 100 frames:

```python
frame_number = 0
max_frames_to_process = 100  # Set the desired number of frames

while True:
    ret, frame = cap.read()
    if not ret or frame_number >= max_frames_to_process:
        break
    # ... (rest of your processing code) ...
    frame_number += 1

import cv2
import numpy as np

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture('video_name.mp4')

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Create a tracker
tracker = cv2.TrackerCSRT_create()

# Read the first frame
ret, frame = cap.read()

# Select a region to track (manually)
bbox = cv2.selectROI('Frame', frame, False)
tracker.init(frame, bbox)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Update the tracker
    success, bbox = tracker.update(frame)

    # Draw bounding box
    if success:
        (x, y, w, h) = tuple(map(int, bbox))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Press Q on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

# This uses a pretrained model called YOLOV3 for car detection
import cv2
import numpy as np

# Load the YOLO model configuration and weights
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

# Load the COCO class labels our YOLO model was trained on
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Get the output layer names that we need from YOLO
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Open the video file (change the filename if necessary)
cap = cv2.VideoCapture("video.mp4")  # Replace with your highway video filename if different

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    height, width, channels = frame.shape

    # Create a blob from the frame and perform a forward pass through YOLO
    blob = cv2.dnn.blobFromImage(frame, scalefactor=0.00392, size=(416, 416),
                                 mean=(0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Initialize our lists of detected bounding boxes, confidences, and class IDs
    boxes = []
    confidences = []
    class_ids = []

    # Process each output layer from YOLO
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            # Filter out weak predictions and focus on "car" detections (COCO label "car")
            if confidence > 0.5 and classes[class_id] == "car":
                # Scale the bounding box coordinates back relative to the image size
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply Non-Maximum Suppression to eliminate redundant overlapping boxes with lower confidences
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Draw bounding boxes for detected cars
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in indexes.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y - 10), font, 0.5, (0, 255, 0), 2)

    # Display the frame with detected cars
    cv2.imshow("Car Detection", frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

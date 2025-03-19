import cv2

# Load the pre-trained Haar cascade classifier for face detection.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open the video file.
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Exit loop if no frame is returned (end of video).

    # Convert the frame to grayscale (Haar cascades require grayscale images).
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around detected faces.
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the frame with detected faces.
    cv2.imshow("Face Detection", frame)

    # Break the loop on 'q' key press.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close display windows.
cap.release()
cv2.destroyAllWindows()

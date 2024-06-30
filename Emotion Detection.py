import cv2
from deepface import DeepFace

# Load the face cascade
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    try:
        # Analyze the frame for emotions
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        result[0]
        emotion = result[0]['dominant_emotion']
        
    except ValueError:
        emotion = "No face detected"

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Define font and add emotion text to the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, emotion, (50, 50), font, 3, (0, 0, 255), 2, cv2.LINE_4)

    # Display the frame
    cv2.imshow('Demo Video', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(2) & 0xFF == 27:
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()

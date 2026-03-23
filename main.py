import cv2

# Load pre-trained face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale (for detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Apply blur to each detected face
    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]

        # 🔥 Strong blur (fixed)
        blurred_face = cv2.GaussianBlur(face, (99, 99), 30)

        # Replace original face with blurred one
        frame[y:y+h, x:x+w] = blurred_face

    # Show output
    cv2.imshow("Face Anonymizer", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
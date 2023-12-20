
import mediapipe as mp
import cv2  # OpenCV

# Initialize the mediapipe module
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize the webcam capture
cap = cv2.VideoCapture(0)

# Initialize the hand tracking module
with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # Convert the BGR image to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with the hand tracking module
        results = hands.process(frame_rgb)

        # Do something with the results (e.g., draw landmarks on hands)
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Hand Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

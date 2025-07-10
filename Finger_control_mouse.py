import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
import math
import warnings
warnings.filterwarnings('ignore')

# MediaPipe and PyAutoGUI 
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
pyautogui.FAILSAFE = False  

screen_w, screen_h = pyautogui.size()     #to increase size of screen 

def distance(p1, p2):
    return math.hypot(p2[0]-p1[0], p2[1]-p1[1])

# Main program
cap = cv2.VideoCapture(0)       #to open camera

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame to same view in window
        frame = cv2.flip(frame, 1)
        h, w, c = frame.shape

        # Convert the frame BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                landmarks = hand_landmarks.landmark

                # Get coordinates of index, middle, ring finger
                index_finger = landmarks[8]
                middle_finger = landmarks[12]
                ring_finger = landmarks[16]

                # Convert cordinates into pixal values
                ix, iy = int(index_finger.x * w), int(index_finger.y * h)
                mx, my = int(middle_finger.x * w), int(middle_finger.y * h)
                rx, ry = int(ring_finger.x * w), int(ring_finger.y * h)

                # Draw hand landmarks on screen
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Cursor movement using index finger
                screen_x = np.interp(ix, [0, w], [0, screen_w])
                screen_y = np.interp(iy, [0, h], [0, screen_h])
                pyautogui.moveTo(screen_x, screen_y, duration=0.01)

                # Check for left click using index & middle fingers together
                if distance((ix, iy), (mx, my)) < 30:    #if distance less than 30 left click event happen 
                    pyautogui.click()         
                    time.sleep(0.1)

                # Check for right click using middle & ring fingers together
                if distance((mx, my), (rx, ry)) < 30:    #if distance less than 30 right click event happen
                    pyautogui.click(button='right')
                    time.sleep(0.1)

        # Show the webcam frame
        cv2.imshow("Finger_Control_Mouse", frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

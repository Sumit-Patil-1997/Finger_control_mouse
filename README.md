# 🖱️ Finger Mouse Controller using OpenCV & MediaPipe

Control your mouse cursor using your **hand gestures** via webcam!  
Move your **index finger** to move the cursor, and perform mouse clicks using **finger combinations**.

---

## 🚀 Features

- 👉 Move mouse cursor using **index finger**
- 👆 **Left Click** by joining **index + middle fingers**
- 🤏 **Right Click** by joining **middle + ring fingers**
- 🖥️ Runs in real-time using webcam
- 🧠 Built using **OpenCV**, **MediaPipe**, and **PyAutoGUI**

---



## 📦 Requirements

Make sure you have **Python 3.7+** installed.



Install required libraries:

--bash
pip install opencv-python mediapipe pyautogui





finger_control_mouse/
│
├── Finger_control_mouse.py       # Main Python script
└── README.md             # Project documentation





🧠 How It Works
Uses MediaPipe to detect hand landmarks

Tracks the tip of the index finger to move the mouse

Detects distance between fingers:

Index + Middle → Left Click

Middle + Ring → Right Click

Uses pyautogui to control mouse movement and clicks




Controls:

Move index finger → Move cursor

Touch index + middle → Left click

Touch middle + ring → Right click

Press q → Quit




📄 License
MIT License – feel free to use and modify!



🙋‍♂️ Author
Developed by Sumit Patil




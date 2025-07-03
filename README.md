# 🖐️ Hand Gesture Volume Controller

Control your PC’s sound using hand gestures in front of your webcam.

This project uses **OpenCV**, **MediaPipe**, and **PyCaw** to track your hand and control the system volume based on the distance between your **thumb** and **index finger**.

---

## 🔥 Features

- 🖐️ Real-time hand detection using MediaPipe
- 🔊 Volume control using finger pinch distance
- 📊 Volume percentage + visual bar
- 🪟 Windows system volume integration via PyCaw

---

## 📽️ How It Works

- Show your hand to the webcam
- Pinch your thumb and index finger closer → decrease volume
- Spread them apart → increase volume
- Works in real time with smooth updates

---

## 🧰 Requirements

- Python 3.7 to 3.11
- Windows OS (for volume control with PyCaw)
- Webcam

---

## 📦 Installation

Clone this repository and install dependencies:

```bash
git clone https://github.com/1anasradwan1/hand-volume-control.git
cd hand-volume-control
pip install -r requirements.txt
# hand-volume-control
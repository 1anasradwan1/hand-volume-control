import cv2
import numpy as np
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, c = img.shape
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((cx, cy))

            if lmList:
                
                x1, y1 = lmList[4]
                x2, y2 = lmList[8]

                cv2.circle(img, (x1, y1), 10, (255, 0, 0), -1)
                cv2.circle(img, (x2, y2), 10, (255, 0, 0), -1)
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

                length = math.hypot(x2 - x1, y2 - y1)

               
                vol = np.interp(length, [20, 180], [minVol, maxVol])
                volBar = np.interp(length, [20, 180], [400, 150])
                volPercent = np.interp(length, [20, 180], [0, 100])

                volume.SetMasterVolumeLevel(vol, None)

                
                cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
                cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), -1)
                cv2.putText(img, f'{int(volPercent)} %', (40, 430),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Hand Volume Control", img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key to close the window
        break

cap.release()
cv2.destroyAllWindows()

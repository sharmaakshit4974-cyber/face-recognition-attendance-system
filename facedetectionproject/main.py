import cv2
import pandas as pd
from datetime import datetime
import pyttsx3
import os

engine = pyttsx3.init()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

label_map = {}

with open("labels.txt", "r") as f:
    for line in f:
        id_, name = line.strip().split(",")
        label_map[int(id_)] = name

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cam = cv2.VideoCapture(0)

attendance = []

while True:

    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        id_, conf = recognizer.predict(gray[y:y+h, x:x+w])

        if conf < 70:

            name = label_map[id_]

            if name not in attendance:

                attendance.append(name)

                time_now = datetime.now().strftime("%H:%M:%S")
                date_now = datetime.now().strftime("%d-%m-%Y")

                df = pd.DataFrame(
                    [[name, date_now, time_now]],
                    columns=["Name", "Date", "Time"]
                )

                df.to_csv(
                    "attendance.csv",
                    mode='a',
                    header=not os.path.exists("attendance.csv"),
                    index=False
                )

                engine.say(f"Welcome {name}")
                engine.runAndWait()

            text = f"{name} Marked"

        else:
            text = "Unknown"

        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.putText(frame, text, (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0,255,0), 2)

    cv2.imshow("Face Recognition", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
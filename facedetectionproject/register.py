import cv2
import os

name = input("Enter Name: ")
roll = input("Enter Roll Number: ")

dataset_path = "dataset"

if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

cam = cv2.VideoCapture(0)

detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

count = 0

while True:

    ret, frame = cam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:

        count += 1

        face = gray[y:y+h, x:x+w]

        filename = f"{name}_{roll}_{count}.jpg"

        cv2.imwrite(
            os.path.join(dataset_path, filename),
            face
        )

        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.putText(frame, str(count), (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0,255,0), 2)

    cv2.imshow("Register Face", frame)

    key = cv2.waitKey(1)

    if key == ord('q') or count >= 30:
        break

cam.release()
cv2.destroyAllWindows()

print("Registration Successful")
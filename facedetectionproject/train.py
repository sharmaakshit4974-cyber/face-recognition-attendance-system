import cv2
import os
import numpy as np
from PIL import Image

path = 'dataset'

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
ids = []

label_ids = {}
current_id = 0

y_labels = []

for file in os.listdir(path):

    if file.endswith("jpg"):

        name = file.split("_")[0]

        if name not in label_ids:
            label_ids[name] = current_id
            current_id += 1

        id_ = label_ids[name]

        image_path = os.path.join(path, file)

        pil_image = Image.open(image_path).convert("L")

        image_array = np.array(pil_image, "uint8")

        faces.append(image_array)
        ids.append(id_)

with open("labels.txt", "w") as f:
    for name, id_ in label_ids.items():
        f.write(f"{id_},{name}\n")

recognizer.train(faces, np.array(ids))
recognizer.save("trainer.yml")

print("Training Complete")
import face_recognition
import os
from PIL import Image

img_path = input("Please enter path to image file to check for faces:\n")
if os.path.exists(img_path):
    image = face_recognition.load_image_file(img_path)
    face_locations = face_recognition.face_locations(image)
    top, right, bottom, left = face_locations[0]
    image = image[top:bottom, left:right]
    face_image = Image.fromarray(image)
    face_image.save("output.jpg")
    input("Success! Press any key to exit")

else:
    input("File not found")
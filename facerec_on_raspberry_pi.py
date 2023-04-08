import face_recognition
import picamera
import numpy as np
import os
import csv
import pathlib
import datetime

# Get a reference to the Raspberry Pi camera.
# If this fails, make sure you have a camera connected to the RPi and that you
# enabled your camera in raspi-config and rebooted first.
camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

# Create arrays of known face encodings and their names
known_face_encodings = []
known_face_names = []

# Load a sample picture and learn how to recognize it.
print("Loading known face image(s)")

# Loop through all the images in the folder and compute their face encodings
for filename in os.listdir("/home/pi/dlib/face_recognition/examples/Test1"):
    image = face_recognition.load_image_file(os.path.join("/home/pi/dlib/face_recognition/examples/Test1", filename))
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(os.path.splitext(filename)[0])

# Initialize some variables
face_locations = []
face_encodings = []

# Create the CSV file on desktop
desktop = str(pathlib.Path.home()) + "/Desktop/"
date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
csv_path = desktop + "Register" + date + ".csv"
with open(csv_path, mode='a') as csv_file:
    fieldnames = ['Name']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

while True:
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    camera.capture(output, format="rgb")

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    # Loop over each face found in the frame to see if it's someone we know.
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "<Unknown Person>"

        # Find the first match
        for i, match in enumerate(matches):
            if match:
                name = known_face_names[i]
                break

        print("I see someone named {}!".format(name))
        # Append name to CSV file
        with open(csv_path, mode='a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'Name': name})

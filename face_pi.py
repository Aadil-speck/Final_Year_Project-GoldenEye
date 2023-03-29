import face_recognition
import picamera
import numpy as np


camera = picamera.PiCamera()
camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

# Load a picture and learn how to recognise it.
print("Loading known face image(s)")
aadil_image = face_recognition.load_image_file("Aadil.jpg")
aadil_face_encoding = face_recognition.face_encodings(aadil_image)[0]

# Initialise variables
face_locations = []
face_encodings = []

while True:
    print("Capturing image.")
    # Grab a single frame of video from the Raspberry Pi camera as a numpy array
    camera.capture(output, format="rgb")

    # Find all the faces and face encodings in the current video
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    # Loop over each face found in the frame to check if it's a known face.
    for face_encoding in face_encodings:
        # Check if the face matches the known face(s)
        match = face_recognition.compare_faces([aadil_face_encoding], face_encoding)
        name = "<Unknown Person>"

        if match[0]:
            name = "Aadil Ali"

        print("I see someone named {}!".format(name))

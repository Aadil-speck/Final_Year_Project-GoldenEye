import face_recognition
import os

# Load the images from a folder and get the face encodings for each person
folder_path = "/home/pi/dlib/face_recognition/examples/Test1"
known_faces = []
for filename in os.listdir(folder_path):
    image = face_recognition.load_image_file(os.path.join(folder_path, filename))
    try:
        face_encoding = face_recognition.face_encodings(image)[0]
        known_faces.append(face_encoding)
        print("Loaded {}'s face.".format(os.path.splitext(filename)[0]))
    except IndexError:
        print("I wasn't able to locate any faces in {}.".format(filename))

# Load the unknown image and get its face encoding
unknown_image = face_recognition.load_image_file("unknown.jpg")
try:
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in the unknown image. Aborting...")
    quit()

# Compare the unknown face encoding to the known face encodings
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

# Print the results
for i, result in enumerate(results):
    if result:
        print("The unknown face is a picture of {}.".format(os.path.splitext(os.listdir(folder_path)[i])[0]))
        break
else:
    print("The unknown face is not a picture of anyone in the folder.")

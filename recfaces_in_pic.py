import face_recognition

# Load the jpg picture files into numpy arrays
chris_image = face_recognition.load_image_file("Chris.jpg")
aadil_image = face_recognition.load_image_file("Aadil.jpg")
unknown_image = face_recognition.load_image_file("Diana.jpg")

try:
    chris_face_encoding = face_recognition.face_encodings(chris_image)[0]
    aadil_face_encoding = face_recognition.face_encodings(aadil_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    chris_face_encoding,
    aadil_face_encoding
]

# An array of True/False 
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Is the unknown face a picture of Chris? {}".format(results[0]))
print("Is the unknown face a picture of Aadil? {}".format(results[0]))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))

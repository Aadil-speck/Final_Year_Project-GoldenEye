import face_recognition

# Load images to compare against known
known_aadil_image = face_recognition.load_image_file("Aadil.jpg")
#known_dianna_image = face_recognition.load_image_file("Diana.jpg")

# Show the face encodings for the known images
aadil_face_encoding = face_recognition.face_encodings(known_aadil_image)[0]
#diana_face_encoding = face_recognition.face_encodings(known_diana_image)[0]

known_encodings = [
    aadil_face_encoding,
    #diana_face_encoding
]

# Load a test image and get encondings for it
image_to_test = face_recognition.load_image_file("Aadil2.jpg")
image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

# See how far apart the test image is from the known faces
face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)

for i, face_distance in enumerate(face_distances):
    print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()

import face_recognition
import os

# Load the known images and encodings
known_encodings = []
known_names = []
known_dir = '/home/pi/dlib/face_recognition/examples/Test1'

# Loop through all the files in the known_people folder
for file in os.listdir(known_dir):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        # Load the image and get the encoding for each face in the image
        image = face_recognition.load_image_file(os.path.join(known_dir, file))
        encodings = face_recognition.face_encodings(image)

        # Add the encodings and names to the lists
        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(file.split('.')[0])

# Load the test image and get the encoding for each face in the image
unknown_image = face_recognition.load_image_file('test_image.jpg')
unknown_encodings = face_recognition.face_encodings(unknown_image)

# Loop through all the unknown encodings and compare them to the known encodings
for unknown_encoding in unknown_encodings:
    # Compare the unknown encoding to all the known encodings
    matches = face_recognition.compare_faces(known_encodings, unknown_encoding)

    # Check if we have a match and get the name
    name = 'Unknown'
    if True in matches:
        first_match_index = matches.index(True)
        name = known_names[first_match_index]

    # Print the name for each face found in the image
    print('Found face with name:', name)


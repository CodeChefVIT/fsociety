import os
import face_recognition
import pickle
import cv2

fp = open("shared.pkl","rb")
shared = pickle.load(fp)

def take_picture():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            cv2.imwrite("temp.png", frame)
            break
    cap.release()
    cv2.destroyAllWindows()

images = os.listdir('images')
take_picture()
image_to_be_matched = face_recognition.load_image_file("temp.png")
image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
for image in images:
    curr_img = face_recognition.load_image_file("images/"+image)
    curr_img_enc = face_recognition.face_encodings(curr_img)[0]
    res = face_recognition.compare_faces([image_to_be_matched_encoded],curr_img_enc)
    if res[0]==True:
        print("Welcome "+image[:-4])
    else:
        import form
        form.mained()
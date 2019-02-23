from tkinter import *
import pickle
import cv2
import os

path = '~/Desktop/devsoc/images/'
shared = None

def take_picture():
    global path
    global shared
    #print("Out")
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            #print("Inside")
            #print(shared)
            #print(shared==None)
            cv2.imwrite("images/"+shared["fName"]+shared["lName"]+".png", frame)
            break

    cap.release()
    cv2.destroyAllWindows()

def run_next():
    pass
    
def run():
    global path
    global shared
    pic_form = Tk()
    pic_form.title("Lets take the picture")
    fp = open("shared.pkl","rb")
    shared = pickle.load(fp)
    take_picture()
    picture = PhotoImage(file=os.path.join(path,shared["fName"]+shared["lName"]+".png"))
    pic_label = Label(image=picture)
    pic_label.grid()
    pic_label.image = picture

    #Button(pic_form, text='Try Again', command=take_picture).grid(row=6, column=0, sticky=W, pady=4)
    Button(pic_form, text='Next', command=run_next).grid(row=6, column=1, sticky=W, pady=4)
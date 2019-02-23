from tkinter import *
from picture_ready import run
import pickle

master = None
e1 = None
e2 = None
can_speak = None
guesture_type = None

def show_entry_fields():
    global e1,e2
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    global guesture_type,can_speak
    if(can_speak.get()==1):
        print("You can speak")
    else:
        print("Cannot Speak")
    print("You selected ", guesture_type.get())

def ret_val():
    #global e1,e2
    shared = {"fName":e1.get(),"lName":e2.get(),"Speak":can_speak.get(),"Guesture":guesture_type.get()}
    fp = open("shared.pkl","wb")
    pickle.dump(shared,fp)
    fp.close()
    #return [e1.get(),e2.get(),can_speak.get(),guesture_type.get()]

def pict_ready():
    global master
    ret_val()
    master.destroy()
    run()
    
def mained():
    import sys
    master = Tk()
    master.title("Welcome to BayMax")

    guesture_type = IntVar()
    guesture_type.set(1)

    can_speak = IntVar()
    can_speak.set(1)

    Label(master, text="First Name").grid(row=0)
    Label(master, text="Last Name").grid(row=1)
    Label(master, text = "Can you speak", justify = LEFT, padx = 20).grid(row=2)
    Label(master, text = "Enter your prefrence", justify = LEFT, padx = 20).grid(row=4)

    e1 = Entry(master)
    e2 = Entry(master)
    Radiobutton(master, text = "Yes", padx = 20, variable = can_speak, value = 1).grid(row=3,column = 0, sticky =W)
    Radiobutton(master, text = "No", padx = 20, variable = can_speak, value = 0).grid(row=3,column = 1, sticky =W)
    Radiobutton(master, text = "Hand Guestures", padx = 20, variable = guesture_type, value = 1).grid(row=5,column = 0, sticky =W)
    Radiobutton(master, text = "Face Guestures", padx = 20, variable = guesture_type, value = 2).grid(row=5,column = 1,sticky=W)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)


    Button(master, text='Quit', command=master.quit).grid(row=6, column=0, sticky=W, pady=4)
    Button(master, text='Show', command=show_entry_fields).grid(row=6, column=1, sticky=W, pady=4)
    Button(master, text='Next', command=pict_ready).grid(row=6,column=2, sticky=W, pady=4)

    mainloop( )

mained()
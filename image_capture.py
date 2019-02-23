import cv2


def crop(img,x1,x2,y1,y2):
    crp=img[y1:y2,x1:x2]
    crp= cv2.resize(crp,(128,128))
    #resize
    return crp

cam = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

cv2.namedWindow("Gesture Capture")

img_counter = 0
redColor = (0, 0, 255)
lineThickness = 2

label = input("Enter the label of your gesture ")

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,1)
    cv2.rectangle(frame, (50,100), (306, 356), redColor, lineThickness)
    cv2.imshow("test", frame)
    
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        img_name = "{}_{}.png".format(label, img_counter)
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cropped = crop(grayscale,50,306,100,356)
        cv2.imwrite("pos/"+img_name, cropped)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()



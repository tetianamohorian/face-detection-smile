import cv2
import random
face_cascade_db = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")


cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade_db.detectMultiScale(img_gray, 1.1, 19)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)
        img_gray_face = img_gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(img_gray_face, 1.1,19)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (x+ex,y+ey), (x+ex+ew,y+ey+eh), (199,21,133), 2)

        smiles = smile_cascade.detectMultiScale(img_gray_face, 1.1, 19)

        if len(smiles) > 0:
            message = "You have a beautiful smile"
            cv2.rectangle(img, (x + smiles[0][0], y + smiles[0][1]),
                          (x + smiles[0][0] + smiles[0][2], y + smiles[0][1] + smiles[0][3]),
                          (0, 0, 255), 2)
        else:
            message = "Don't be sad bro :), keep smiling!"

        cv2.putText(img, message, (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        

    cv2.imshow('Result', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
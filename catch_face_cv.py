
import os
import cv2

cascPath = "/home/ace/anaconda3/pkgs/libopencv-3.4.2-hb342d67_1/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
output_dir = './myface'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# classifiers
faceCascade = cv2.CascadeClassifier(cascPath)

#camera
camera = cv2.VideoCapture(0)

index = 1
while True:
    if(index <=1000):
            # Read the image
        success,image = camera.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            image = image[y:y+h,x:x+w]
            image = cv2.resize(image,(64,64))
       
            cv2.imshow('image',image)
            cv2.imwrite(output_dir+'/'+str(index)+'.jpg',image)

        index +=1
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
camera.release()
cv2.destroyAllWindows()

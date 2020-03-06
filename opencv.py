#/home/ace/anaconda3/pkgs/libopencv-3.4.2-hb342d67_1/share/OpenCV/haarcascades

#The line below is necesary to show Matplotlib's plots inside a Jupyter Notebook

import cv2

imagePath = "cgjm.jpg"
cascPath = "/home/ace/anaconda3/pkgs/libopencv-3.4.2-hb342d67_1/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

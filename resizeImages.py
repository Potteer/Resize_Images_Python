import cv2
import glob
import os

inputFolder = 'images/Prip3Spoofs'
ouputFolder = 'images/resized/'

if inputFolder == 'images/Prip3Spoofs':
    nameImage = "prip"
    typeImage = ".png"
else:
    nameImage = "tpdne"
    typeImage = ".jpg"

if not os.path.exists(ouputFolder):
    os.mkdir(ouputFolder)

i = 0

for img in glob.glob(inputFolder + "/*" + typeImage):
    image = cv2.imread(img)
    imgResized = cv2.resize(image, (480,600))
    cv2.imwrite(ouputFolder + nameImage + "%i.jpg" %i, imgResized)
    i +=1
    cv2.imshow('image', imgResized)
    cv2.waitKey(30)

cv2.destroyAllWindows()

 

num_files = len([f for f in os.listdir(ouputFolder)if os.path.isfile(os.path.join(ouputFolder, f))])
print(num_files)

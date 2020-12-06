import cv2
import time
import imutils

cam = cv2.VideoCapture(0)
time.sleep(1)

while True:
    _,imge = cam.read()
    cv2.imshow("camera.jpg",imge)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        res,img = cam.read()
        image = 'img.jpg'
        cv2.imwrite(image, img)
        break


try:
    from PIL import Image
except ImportError:
    import Image


import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text


info = recText('img.jpg')
print(info)
file = open("result.txt","w")
file.write(info)
file.close()
print("successful")
cam.release()
cv2.destroyAllWindows()

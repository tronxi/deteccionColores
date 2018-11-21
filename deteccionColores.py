import cv2
import numpy as np
 
#Iniciamos la camara
captura = cv2.VideoCapture(0)

def nothing(x):
   pass
 
#Creamos una ventana llamada 'image' en la que habra todos los sliders
cv2.namedWindow('image')
cv2.createTrackbar('H Minimo','image',0,255,nothing)
cv2.createTrackbar('S Minimo','image',0,255,nothing)
cv2.createTrackbar('V Minimo','image',0,255,nothing)

cv2.createTrackbar('H Maximo','image',0,255,nothing)
cv2.createTrackbar('S Maximo','image',0,255,nothing)
cv2.createTrackbar('V Maximo','image',0,255,nothing)

cv2.setTrackbarPos('H Minimo', 'image', 49)
cv2.setTrackbarPos('S Minimo', 'image', 50)
cv2.setTrackbarPos('V Minimo', 'image', 50)

cv2.setTrackbarPos('H Maximo', 'image', 80)
cv2.setTrackbarPos('S Maximo', 'image', 255)
cv2.setTrackbarPos('V Maximo', 'image', 255)

while(captura.isOpened()):
     
    ret, imagen = captura.read()
    if ret == True:
        imagen = cv2.GaussianBlur(imagen ,(9,9),0)
        hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

        hMin = cv2.getTrackbarPos('H Minimo','image')
        hMax = cv2.getTrackbarPos('H Maximo','image')
        sMin = cv2.getTrackbarPos('S Minimo','image')
        sMax = cv2.getTrackbarPos('S Maximo','image')
        vMin = cv2.getTrackbarPos('V Minimo','image')
        vMax = cv2.getTrackbarPos('V Maximo','image')

        lower=np.array([hMin,sMin,vMin])
        upper=np.array([hMax,sMax,vMax])
    
        mask = cv2.inRange(hsv, lower, upper)
    
        moments = cv2.moments(mask)
        area = moments['m00']
    
        if(area > 2000000):
         
            x = int(moments['m10']/moments['m00'])
            y = int(moments['m01']/moments['m00'])
    
            cv2.rectangle(imagen, (x, y), (x+2, y+2),(0,0,255), 2)

        cv2.imshow('mask', mask)
        cv2.imshow('Camara', imagen)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
captura.release()
cv2.destroyAllWindows()
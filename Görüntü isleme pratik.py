#resimdeki siyah kısmı sarı yapan kod.
"""
import cv2
img = cv2.imread("images/cameramen.png")
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if all(img[i, j] == 0):
            img[i, j, 0] = 99
            img[i, j, 1] = 149
            img[i, j, 2] = 179
cv2.imshow("boyanmı hali", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# Konumları ve RGB si verilen sarı balonu siyaha boyama kodu.
"""
import cv2
from matplotlib import pyplot as plt
x = cv2.imread("images/balonlar.jpg")
plt.subplot(121) , plt.imshow(x)
for i in range(65,185):
    for j in range(14,118):
        if x[i,j,0]>20 and x[i,j,0]<100 and x[i,j,1]>150 and x[i,j,2]>180:
            x[i,j]=0
plt.subplot(122),plt.imshow(x),plt.title("son durum")            
"""

# bitwise ile görüntünün tersini alan kod.
"""
import cv2
from matplotlib import pyplot as plt
x=cv2.imread("images/bird.png")
bitwise = cv2.bitwise_not(x)
plt.subplot(121),plt.imshow(x),plt.title("Orijinal")
plt.subplot(122),plt.imshow(bitwise),plt.title("Rengi terslenmiş")
"""

#Video oynatma kodu. (calismiyor)
"""
import cv2
cap=cv2.VideoCapture("video.mvc")
while(cap.isOpened()):
    ret.frame=cap.read()
    if ret == True:
        cv2.imshow(frame)
        cv2.waitkey(0)
cap.release()
"""

#Izgaralı Kamera Görüntüsü
"""
import cv2  
cam = cv2.VideoCapture(0)  
while True:
    ret, x = cam.read()
    for i in range(0, x.shape[0], 90):
        for j in range(0, x.shape[1], 90):
            cv2.line(x, (j, i), (j, i + 90), (0, 0, 0), 1)
            cv2.line(x, (j, i), (j + 90, i), (0, 0, 0), 1)


    cv2.imshow('Girdi', x)
    c = cv2.waitKey(1)
    if c == 27:  
        break
cam.release()  
cv2.destroyAllWindows()
"""

#Kamera
"""
import cv2  
cam = cv2.VideoCapture(0) 
while True:
    ret, x = cam.read()  
    cv2.imshow('Girdi', x)
    c = cv2.waitKey(1)
    if c == 27:  
        break
cam.release()  
cv2.destroyAllWindows()
"""

# Örüntünün kaç kez geçtigini sol üst köşe kordinatlarını bulup ekrana yazdıran kod. Yan yana [11][22][33].
"""
import cv2 
img = cv2.imread("images/kareler.jpg")
imgray = cv2.cvtColor(img.cv2.COLOR_RGB2GRAY)
x.y = gray.shape
sayac = 0
for i in range(x):
    for j in range(y):
        if imgray[i,j] == 11 and imgray[i,j+1]== 22 and imgray[i,j+2]== 33:
            print(i,"örüntü bulundu.Değerleri : " ,  i,j)
            sayac += 1     
print(sayac)
"""

#Resimleri üst üste gösterme
"""
import cv2
img1 = cv2.imread("images/balonlar.jpg")
img2 = cv2.imread("images/bean.png")
img1 = cv2.resize(img1, (1000, 562))
img2 = cv2.resize(img2, (1000, 562))
topla = img1.copy()
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        topla[i, j] = img1[i, j] + img2[i, j]
toplam = cv2.add(img1, img2)
cv2.imshow("balonlar", img1)
cv2.imshow("Bean", img2)
cv2.imshow("Topla", topla)
cv2.imshow("Toplam", toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

#çerçeveli alanı diğer resime aktarma.
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
x = cv2.imread("images/balonlar.jpg")
y = cv2.imread("images/bean.png")
z = cv2.imread("images/bean.png")
for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        if (i >= 10) and (i <= 200) and (j >= 20) and (j <= 100):
            y[i, j] = x[i, j]
tum = cv2.hconcat([z, y])
cv2.imshow("tüm resim", tum)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
# Çerçeveli Kamera.
"""
import cv2
import numpy as np
cam = cv2.VideoCapture(0) # Kamera başlatma
while True:
    ret, frame = cam.read()    
    frame[0:10, :] = [0, 0, 255] #Kırmızı     
    frame[:, 0:10] = [0, 0, 255] #Siyah    
    frame[-10:, 0:] = [0, 0, 255] #Mavi    
    frame[0:, -10:] = [0, 0, 255] #Yeşil    
    cv2.imshow('Modified Image', frame)
    if cv2.waitKey(1) == 27:  # Çıkış için ESC tuşuna basma kontrolü
        break
cam.release()
cv2.destroyAllWindows()
"""
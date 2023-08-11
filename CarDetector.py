import cv2
car_cascade = cv2.CascadeClassifier('cars.xml')
image = cv2.imread('car.png')
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
carsDetect = car_cascade.detectMultiScale(grayscale, 1.05, 1)
print(f'{len(carsDetect)} cars found')
for (x,y,z,a) in carsDetect:
    cv2.rectangle(image,(x,y),(x+z,y+a),(0,0,255),4)
cv2.imshow('Detected Cars', image)
cv2.waitKey(0)
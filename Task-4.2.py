#Task-4.2: 
#Importing numpy and cv2
import cv2
import numpy as np

#Reading Image A and B
a = cv2.imread('a.PNG')
b = cv2.imread('b.PNG')

# Output of the both images
cv2.imshow('a1',a)
cv2.imshow('b2',b)
cv2.waitKey()
cv2.destroyAllWindows()


#Cropping some portion of the images
x = a[0:300, 0:150]
y = b[0:300, 0:150]

#Output of the cropped portion of the image
cv2.imshow('c-a1',x)
cv2.imshow('c-b2',y)
cv2.waitKey()
cv2.destroyAllWindows()


#Swapping
a = cv2.imread('a.PNG')
b = cv2.imread('b.PNG')

#Output of the Swap-Images
cv2.imshow('Task-2-swap_a1',a)
cv2.imshow('Task-2-swap_b2',b)
cv2.waitKey()
cv2.destroyAllWindows()

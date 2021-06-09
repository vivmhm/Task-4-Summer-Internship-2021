#Task-4.3:
#Importing cv2
import cv2

#Reading Image A and B
a = cv2.imread("a.PNG")
b = cv2.imread("b.PNG")

# Resizing and concatenating both the images and making it as collage horizontally 
a_resize = cv2.resize(a, (300,300))
b_resize = cv2.resize(b, (300,300))
h_concat = cv2.hconcat([ a_resize, b_resize])

#Output of the Collage Image
cv2.imshow("Collage-Task-4-4.3", h_concat)
cv2.waitKey()
cv2.destroyAllWindows()

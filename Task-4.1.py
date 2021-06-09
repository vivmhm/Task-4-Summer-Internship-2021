#Task-4.1: 
#Importing numpy and cv2
import numpy as np
import cv2 

#Storing the image with img variable.
img = np.zeros((300,300,3), np.uint8)

#Ellipse Creation  
cv2.ellipse(img,(150,150),(100,50),1,1,360,255,-1)
cv2.ellipse(img,(150,150),(100,50),0,0,180,255,-1)

#Font for the Text
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

#Text in the Image
cv2.putText(img,'Linux World',(70,160), font, 1,(255,255,255),1,cv2.LINE_AA)


#Displaying the Output of the Image
cv2.imshow('Task-4-4.1-Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

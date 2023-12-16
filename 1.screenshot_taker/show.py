"""
https://www.geeksforgeeks.org/reading-images-in-python/
"""
# importing OpenCV(cv2) module
import cv2
import os

# Save image in set directory
# Read RGB image
count = len(os.listdir('Screenshots/'))
img = cv2.imread('Screenshots/ScreenShot_'+str(count)+'.png') 
 
# Output img with window name as 'image'
cv2.imshow('image', img) 
 
# Maintain output window until
# user presses a key
cv2.waitKey(0)        
 
# Destroying present windows on screen
cv2.destroyAllWindows() 

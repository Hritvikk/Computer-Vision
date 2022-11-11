import cv2
import numpy as np
 
point_matrix = np.zeros((2,2),np.int)
 
counter = 0

# Capturing cropping points
def mousePoints(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix[counter] = x,y
        counter = counter + 1
img = cv2.imread('Task_1.jpg')
 
while True:
    for x in range (0,2):
        cv2.circle(img,(point_matrix[x][0],point_matrix[x][1]),3,(0,255,0),cv2.FILLED)
 
    if counter == 2:
        starting_x = point_matrix[0][0]
        starting_y = point_matrix[0][1]
 
        ending_x = point_matrix[1][0]
        ending_y = point_matrix[1][1]
        cv2.rectangle(img, (starting_x, starting_y), (ending_x, ending_y), (0, 255, 0), 3)

        #Cropping Image
        img_cropped = img[starting_y:ending_y, starting_x:ending_x]

        #Showing Output
        cv2.imshow("Cropped Image", img_cropped)

        #cv2.imwrite('/output.png',img_cropped)
    
    # Taking User Input
    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    print(point_matrix)
    cv2.waitKey(1)
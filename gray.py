import cv2

# 1. Load original image:
image = cv2.imread('prueba.png')

# 2. Convert image from BGR to B&N
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Show both images to compare:
cv2.imshow('Original image (Color)', image)
cv2.imshow('Modified image (Gray)', image_grey)
print(image_grey.shape) #This is to verify that the image no longer has 3 channels


#Saving the new image:
#First parameter: new file name, second parameter: matrix name
cv2.imwrite('prueba_gris.png', image_grey)

# 4. Pause and clean:
cv2.waitKey(0)
cv2.destroyAllWindows()
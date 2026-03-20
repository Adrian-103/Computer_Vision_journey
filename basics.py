import cv2

# 1. Read image from SSD:
# Warning: FIle name must match exactly
image = cv2.imread('prueba.png')



#====SHOW THE IMAGE MATRIX====
print("Pixel matrix:")
print(image)

#Prints the dimensions of the matrix:
print("\nImage dimensions:")
print(image.shape)
#=============================

# 2. Show the image in a new pop up window:
# First text is the title of the window

cv2.imshow("My first image", image)

# 3. Pause the program
# waitKey(0) makes the program wait for a key entered by the user.

cv2.waitKey(0)

# 4. Cleaning
# Whenever a key is pressed, we safely close the window:
cv2.destroyAllWindows()
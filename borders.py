import cv2

image = cv2.imread("sample.jpg")
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur:
# (5, 5) means the size of the blur brush. It must be an odd number, for example (3,3)

blur = cv2.GaussianBlur(grey, (5,5), 0)

# Canny border detection
# The numbers 50 and 150 are the sensibility tresholds:
# "Every light change minor to 50 is ignored, over 150 is a border for sure"

borders = cv2.Canny(blur, 50, 150)

#Show the process:
cv2.imshow('1. Original', image)
cv2.imshow('2. Desenfoque', blur)
cv2.imshow('3. Bordes (Canny)', borders)

cv2.waitKey(0)
cv2.destroyAllWindows()


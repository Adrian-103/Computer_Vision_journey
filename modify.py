import cv2

image = cv2.imread("prueba.png")


#First, we check the actual dimensions of the image so the calculations don't produce wrong results.
height, width = image.shape[:2]
print(f"The image is {width} pixels width and {height} pixels height")

#=====CUT (ROI)=====
# Format: image[y_start : y_final, x_start : x_final]
cut = image[200:700 , 500:1000]
#===================


#=====REDIMENSION=====
#Format: cv2.resize(original_image, (new_width, new_height))
image_half = cv2.resize(image, (width // 2, height // 2)) #This will reduce the image to its half.
#=====================


cv2.imshow('1. Original_image', image)
cv2.imshow('2. CUT (ROI)', cut)
cv2.imshow('3. HALF', image_half)

cv2.waitKey(0)
cv2.destroyAllWindows()

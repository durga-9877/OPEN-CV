import cv2 
img = cv2.imread(r"C:\Users\A.Durga sankar sai\OneDrive\Desktop\images.jpg") 
cv2.imshow("hitman", img) 
gray_image = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY) 
cv2.imshow("Grayscale", gray_image) 
cv2.waitKey(0)

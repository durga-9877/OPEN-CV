import cv2 
img = cv2.imread(r"C:\Users\A.Durga sankar sai\OneDrive\Desktop\images.jpg") 
cv2.imshow("hitman.jpg", img) 
cv2.imwrite("hitman.png", img) 
cv2.imwrite("hitman.tiff", img) 
cv2.imshow("hitman.png", img) 
cv2.imshow("hitman.tiff", img) 
cv2.waitKey(0) 

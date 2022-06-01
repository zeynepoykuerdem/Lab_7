import cv2
import numpy as np
img=cv2.imread("C:\\Users\\zeyne\\OneDrive\\Desktop\\acryclic.jpg")
cv2.imshow("",img)
cv2.waitKey(0)
B,G,R=cv2.split(img)
cv2.imshow("B",B)
cv2.waitKey(0)

cv2.imshow("G",G)
cv2.waitKey(0)

cv2.imshow("R",R)
cv2.waitKey(0)
cv2.destroyAllWindows()

merge=cv2.merge([B,G,R])
cv2.imshow("merge",merge)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
img[:,:,0] = np.zeros([img.shape[0], img.shape[1]])
cv2.imwrite('C:\\Users\\zeyne\\OneDrive\\Desktop\\no-blue-channel.jpg',img)
cv2.destroyAllWindows()
px=img[100,100]
print(px)
img[100,100]=[0,255,50]
print(img[100,100])
cv2.imshow("modify",img)
cv2.waitKey(0)




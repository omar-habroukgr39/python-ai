import cv2
import numpy as np

# orginal image
img = cv2.imread("img/m.png")
cv2.imshow("original project", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
zero =np.zeros(img.shape[:2] , dtype = 'uint8')

blue , green,red = cv2.split(img)

cv2.waitKey(0)

# cv2.imshow("split chanel" , green)
# # cv2.waitKey(0)
# cv2.imshow("split chanel" , blue)
# # cv2.waitKey(0)
# cv2.imshow("split chanel" , red)
# cv2.waitKey(0)


# merged = cv2.merge([blue,green,red])
# cv2.imshow("merged" , merged)

hstack = np.hstack([green , blue])

hstack1=  np.hstack([red , zero])

hvstack = np.vstack([hstack,hstack1])


cv2.imshow("merged all" , hvstack)
cv2.waitKey(0)  
cv2.destroyAllWindows


# array =[0,1,-1]

# # Flip the image horizontally
# flipped = cv2.flip(img,array[0])
# cv2.imshow("flipped project", flipped)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Flip the image vertically
# flipped1 = cv2.flip(img,array[1])
# cv2.imshow("flipped1 project", flipped1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Flip the image both vertically and horizontally
# flipped2 = cv2.flip(img,array[-1])
# cv2.imshow("flipped2 project", flipped2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# all = np.hstack([flipped , flipped1 , flipped2])
# cv2.imshow("all", all)
# cv2.waitKey(0)
# cv2.destroyAllWindows()





# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray image",gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("gray.jpeg",gray)

# HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow("HSV image",HSV)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("HCV.png",HSV)


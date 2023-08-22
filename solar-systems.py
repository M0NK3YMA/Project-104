import cv2
img=cv2.imread('solar-system.jpg')
cv2.putText(img,'Sun',(20,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=2,color=(0,0,255))
cv2.putText(img,'Mercury',(20,350),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.4,color=(0,0,0))
cv2.putText(img,'Venus',(20,400),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.4,color=(0,0,0))
cv2.putText(img,'Earth',(20,450),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.4,color=(0,0,0))
cv2.putText(img,'Mars',(20,500),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.4,color=(0,0,0))
cv2.putText(img,'Jupiter',(20,550),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.4,color=(0,0,0))
cv2.putText(img,'Uranus',(20,600),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.4,color=(0,0,0))
cv2.putText(img,'Neptune',(20,650),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.4,color=(0,0,0))

cv2.imshow('solar-system',img)





cv2.waitKey(0)
print(img)
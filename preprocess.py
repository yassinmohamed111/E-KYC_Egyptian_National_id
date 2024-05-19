import cv2 
import numpy as np

    
def thresholding(image,black):
        img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        _,thresh = cv2.threshold(img_gray,black,255,cv2.THRESH_BINARY_INV)
        
        return thresh
  


def dilation(thresh_img,v1=1,v2=1):
            
        kernel = np.ones((v1,v2), np.uint8)
        #(1,2),iter=2
        dilated = cv2.dilate(thresh_img, kernel, iterations = 2)
        return dilated
    



def save_threshold(image1 , image2 , image3 , image4):
        cv2.imwrite(r'C:\Users\yassi\Desktop\my_ocr\Ekyc-ocr\temp\output_name.jpg' , image1)
        cv2.imwrite(r'C:\Users\yassi\Desktop\my_ocr\Ekyc-ocr\temp\output_second_name.jpg' , image2)
        cv2.imwrite(r'C:\Users\yassi\Desktop\my_ocr\Ekyc-ocr\temp\output_locationn.jpg' , image3)
        cv2.imwrite(r'C:\Users\yassi\Desktop\my_ocr\Ekyc-ocr\temp\output_manf.jpg' , image4)
        


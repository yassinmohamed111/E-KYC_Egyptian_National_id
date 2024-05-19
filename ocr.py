import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2 
from ArabicOcr import arabicocr

from ultralytics import YOLO
import numpy as np


def egyptian_id_model(source):
        model = YOLO(r'C:\Users\yassi\Desktop\Ekyc-ocr\models\egy_id_new.pt')
        results = model(source, save=True, conf=0.6, imgsz=640 ,show=False , save_crop = True)



def arabic_numbers(national_image):
        model2 = YOLO(r'C:\Users\yassi\Desktop\Ekyc-ocr\models\arabic_numbers.pt')
        resultss = model2(national_image, save=True, conf=0.4, imgsz=480 ,show=True)
        for res in resultss:
        # Get the bounding box coordinates
            xyxy = res.boxes.xyxy.to('cpu').numpy()
            sorted_indices = np.argsort(xyxy[:, 0])
            sorted_classes = res.boxes.cls[sorted_indices]
            national_id = ''.join(map(str, sorted_classes.cpu().numpy().astype(int)))
        return national_id



def extract_one(image_path,out_image,filename):
        results=arabicocr.arabic_ocr(image_path,out_image)
        print(results)
        words=[]
        for i in range(len(results)):	
                word=results[i][1]
                words.append(word)
        with open (filename,'w',encoding='utf-8')as myfile:
                myfile.write(str(words))
        
        img = cv2.imread(out_image)
        return words




def get_second_name(image):
        res = pytesseract.image_to_string(image , lang='ara')
        return res
    


def get_manf_id(image):
        res = pytesseract.image_to_string(image)
        return res


def extract_data():
    out_image = r'C:\Users\yassi\Desktop\my_ocr\Ekyc-ocr\saved\result.jpg'
    first_name = extract_one(r'C:\Users\yassi\Desktop\my_ocr\Ekyc-ocr\temp\output_name.jpg', out_image, 'result.txt')
    secondname = get_second_name(r'C:\Users\yassi\Desktop\my_ocr\Ekyc-ocr\temp\output_second_name.jpg')
    location = extract_one(r'C:\Users\yassi\Desktop\my_ocr\Ekyc-ocr\temp\output_locationn.jpg', out_image, 'result.txt')
    loc = ' '.join(location) if location else "No text found" 
    full_name = ' '.join(first_name) if first_name else "No text found" 
    return full_name , secondname , loc



def get_gender_and_bday(national_id):
        century = national_id[0]
        year_born = national_id[1] + national_id[2]
        month = national_id[3]+national_id[4]
        day = national_id[5]+national_id[6]
        gender = national_id[12]
        

        birthdate = ""
        if century == "3" :
            birthdate = day + "-" + month  +"-"+"20"+year_born
        elif century == "2":
            birthdate =  day+"-"+month+"-"+"19"+year_born

        last_gender = None
        if int(gender)%2 == 0 :
                last_gender = 'انثى'
                print("gender : female ")
        else:
                last_gender  = "ذكر"
                print("gender : male ")

        return last_gender , birthdate



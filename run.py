import os
from ArabicOcr import arabicocr
from preprocess import save_threshold , dilation , thresholding
from ocr import get_gender_and_bday , get_manf_id , get_second_name , extract_data, arabic_numbers, egyptian_id_model
from check import  get_segements,get_national_id
from ultralytics import YOLO



#this function is made for the super app
def get_id_for_super_app():
   lst = os.listdir(r'runs/detect') 
   number_files = len(lst)
   source = r"id.jpg"
   file_name = os.path.basename(source)
   
   egyptian_id_model(source)

   
   
   file_path = rf'C:\Users\yassi\Desktop\my_ocr\runs\detect\predict{number_files+1}\crops\national_id\{file_name}'

   if not os.path.exists(file_path):
        list_ret = ["The picture is not clear enough , please take a close , high resolution and clear picture"]
        return list_ret
   

   national_image = get_national_id(number_files , file_name)
   
   national_id = arabic_numbers(national_image)
   return national_id
    

    






def get_ocr():
    lst = os.listdir(r'runs/detect') 
    number_files = len(lst)
    source = r"id.jpg"
    file_name = os.path.basename(source)

   
#first we run the model and we get the egyptian id segements 
    egyptian_id_model(source)
    
   
#second we check if all fields are detected
    
    file_path = rf'C:\Users\yassi\Desktop\my_ocr\runs\detect\predict{number_files+1}\crops\national_id\{file_name}'

    if not os.path.exists(file_path):
        list_ret = ["The picture is not clear enough , please take a close , high resolution and clear picture"]
        return list_ret




#if so we get the national_id segements  
    national_image = get_national_id(number_files , file_name)
    

#using arabic_numbers model to get national id 
    national_id = arabic_numbers(national_image)

    
#now we collect the other segements to start the image processing
    segments = get_segements(source, number_files)



#image processsing part ( researched on it through the internet and youtube )
    thresh_fname = thresholding(segments[0], 70)
    thresh_sname = thresholding(segments[1], 70)
    thresh_location = thresholding(segments[2], 70)
    thresh_manf = thresholding(segments[3], 70)
    dilated_fname = dilation(thresh_fname)
    dilated_sname = dilation(thresh_sname)
    dilated_location = dilation(thresh_location)
    dilated_manf = dilation(thresh_manf)


    
#save the processed images
    save_threshold(dilated_fname, dilated_sname, dilated_location, dilated_manf)
     
#extract the other data using open source pretrained models (tesseract ocr and arabicOCR)
    ocr_data = extract_data()

    #extract from the national id the gender and birthdate
    gender_bday = get_gender_and_bday(national_id)

    return ocr_data[0], ocr_data[1], national_id, gender_bday[1], ocr_data[2], gender_bday[0]

 





'''
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
#database conn ############
cluster = MongoClient("mongodb+srv://yassinmohamed022:1234@cluster0.iwtvhnq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster['ocr']
collection = db['ocrcollection']


#7ot al sora
def insert_image(filepath):
    with open(filepath, "rb") as f:
        image_data = f.read()
        image_dict = {"image": image_data}
        db.images.insert_one(image_dict)


def extract_image(image_id, output_path):
    image_dict = db.images.find_one({"_id": image_id})
    if image_dict:
        with open(output_path, "wb") as f:
            f.write(image_dict["image"])



def get_pic():
    cursor = db.images.find({})
    for image_dict in cursor:
        image_id = image_dict["_id"]
    extract_image(image_id, "id.jpg")

def upload_data(list_return):
    data = {"fistname": list_return[0], "secondname": list_return[1], "national_id": list_return[2] , "birthdate": list_return[3] , "address": list_return[4] , "gender": list_return[5] , "manfucturing_id": list_return[6]}
    db.data.insert_one(data)




'''





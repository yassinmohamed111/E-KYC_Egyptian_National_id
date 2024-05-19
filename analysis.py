import pandas as pd 
import numpy as np


df = pd.read_csv(r"C:\Users\yassi\Desktop\my_ocr\data.csv")


def search_for_a_name(fname, secondname):
    df_name = df[(df['fname'] == fname) & (df["sname"] == secondname)]
    if df_name.empty == True :
        print("not found")
    else:
        print(df_name)



def serachForAnyColumn(column , query):
    df_id = df[df[column] == query ]
    if df_id.empty == True:
        print("not found")
    else:
        print(df_id)
    


#get count of specific query in any column just add - > columnName and the specifc thing you want
def getCountOfAnyColumn(column , query):

    df_add = df[df[column] == query ] 
    count = df_add[column].count() 
    print(count)



#function to read the whole address and detect the governate and push it to the governate columns    
def automate_address():
    governates = [ 'cairo', 'giza', 'alexandria', 'luxor', 'southsinai', 'sharqia', 'gharbia', 'qalyubia', 'dakahlia', 'assiut', 'sohag', 'ismailia', 'benisuef', 'fayoum', 'minya', 'qena', 'menoufia', 'damietta', 'kafralsheikh', 'northsinai', 'matrouh', 'luxor', 'aswan', 'newvalley', 'sharkia', 'suez',  'portsaid', 'redsea', 'beheira']

    for gov in governates:
        for i  , row in df.iterrows():

            if gov in row['address'].lower():

                df.at[i, 'governate'] = gov
                df.to_csv("data.csv" , index=False)
            



number_mapping = {
    '01': "cairo",
    '02': "alexandria",
    '03': "portsaid",
    '04': "suez",
    '11': "damieta",
    '12': "dakahlya",
    '13': "elsharkya",
    '14': "elkalyobia",
    '15': "kafr elsheikh",
    '16': "elgharbia",
    '17': 'elmenofya',
    '18': "elbehira",
    '19': "elesmaalyaa",
    '21': "giza",
    '22': "beni suief",
    '23': "fayium",
    '24': "elmenya",
    '25': "assiut",
    '26': "sohag",
    '27': "qena",
    '28': "aswan",
    '29': "luxor",
    '31': "red sea governate",
    '32': "wadi el-gadid",
    '33': "matrouh",
    '34': "north sinai",
    '35': "south sinai",
    '88': "outside the country"
}
 


#add to the csv file the place of birth of each user using NID
def getPlaceOfBirth():
    for i , row in df.iterrows():
        national_id = str(row['national_id'])
        var_born = str(national_id[7]) + str(national_id[8])
        df.at[i , 'place_of_birth'] = number_mapping[str(var_born)]
        df.to_csv("data.csv" , index=False)


#get count of users in each governate 
def getCountOfUsersGovernates():
    df_govs = df['governate']
    print(pd.value_counts(df_govs))     




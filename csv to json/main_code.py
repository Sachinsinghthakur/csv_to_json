import csv
import json
import pandas as pd
import os
import faker
from faker import Faker



def writing_csv(path):
    fake = Faker()
    dict_list = []
    for i in range(1000):
        dct = {
                "id":i+1,   "name":fake.name(),    "age":fake.random_int(min = 14,max=80 , step=1) , 
               "city":fake.city(),  "postal_code":fake.zipcode(),  "street":fake.street_address()
              }
        dict_list.append(dct)
    file_name = os.path.abspath(os.path.join(path,"person_data.csv"))
    with open(file_name,"w",newline="") as f:
        writer = csv.DictWriter(f,fieldnames =  [ "id","name","age","city","postal_code","street"])
        writer.writeheader()
        writer.writerows(dict_list)

def csv_to_json(path):
    df = pd.read_csv(path)
    df.reset_index(drop=True,inplace=True)
    folder_path = os.path.abspath(os.path.dirname(path))
    os.chdir(folder_path)
    df.to_json("person_data.json",orient='records')

if __name__ == "__main__":
    writing_csv('C:\\Users\\Canopus-57\\csv to json\\data files')
    csv_to_json("C:\\Users\\Canopus-57\\csv to json\\data files\\person_data.csv")
import os
import pandas as pd
import csv

def create_info(item: dict):
    file_path = 'info.csv'
    head_filed = ['No','Name', 'Age', 'Education', 'Job', 'Hobby', 'ranking_list']

    def file_exist(file_path):
        return os.path.exists(file_path)
    
    def append_to_csv(file_path,data):
        with open(file_path, 'a' , newline= '') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    if not file_exist(file_path):
        append_to_csv(file_path,head_filed)
    
    def add_info(list_infor : list):
        append_to_csv(file_path,list_infor)

    value = []
    df = pd.read_csv('info.csv')
    row_count = len(df)
    value.insert(0,row_count + 1)
    value.insert(1,item["name"])
    value.insert(2,item["info"]["age"])
    value.insert(3,item["info"]["education"])
    value.insert(4,item["info"]["job"])
    value.insert(5,item["info"]["hobby"])
    value.insert(6,min(item["ranking_list"]))
    add_info(value)
    return "okok"
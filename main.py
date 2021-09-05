# -*- coding: utf-8 -*-
"""
Created on Sat May 29 09:49:16 2021

@author: Sepideh
"""

import time
from mysql.connector import Error
import numpy as np
import mysql.connector
from ML import my_classifier

host_name = "localhost"
user_name = "root"
password_string = ""
db = "test_realtime_insert"
Finnished = "False"
sample_rate = 256
chanels_num = 20
last_id_from_db = 0
all_remained_to_process = np.empty(shape=[0,chanels_num+1])

    
def getFromDb():  
    global last_id_from_db
    select_query = """SELECT * FROM eeg_data WHERE id> "%s" """%(last_id_from_db) 
    with mydb.cursor() as cursor:
        cursor.execute(select_query)
        result = cursor.fetchall()   
    result = np.array(result)
    if result.size != 0:
        last_id_from_db = result[-1,0]
    return result


def ML(new_data):
    global all_remained_to_process
    all_remained_to_process = np.concatenate([all_remained_to_process, new_data], axis=0)   
    while len(all_remained_to_process) >= sample_rate:
        data = all_remained_to_process[:sample_rate]
        all_remained_to_process = np.delete(all_remained_to_process, slice(sample_rate), axis=0)     
        print(all_remained_to_process.shape)
        predicted_label = my_classifier.Hi(data)
        insert_query = """INSERT INTO ml_results(`nn`)  VALUES("%s") """%(predicted_label)
        print(predicted_label)
        mycursor = mydb.cursor()
        mycursor.execute(insert_query)
        mydb.commit()

      
if __name__ == '__main__':  
    
    while Finnished == "False":
        try:
            mydb = mysql.connector.connect(
                    host=host_name,
                    user=user_name,
                    password=password_string,
                    database=db
                    )
        except Error as e:
            print(e)
        new_data = getFromDb()
        print(new_data.shape)
        if new_data.size != 0:   
            ML(new_data)
            time.sleep(1)
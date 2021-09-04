# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 10:06:50 2021

@author: sepideh
"""
import time
from mysql.connector import Error
import mysql.connector
import pandas as pd

host_name = "localhost"
user_name = "root"
password_string = ""
db = "test_RealTime_insert"
l = 0
num_chanels = 20
sample_rate = 256
time_to_continue = 120
try:
    mydb = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=password_string,
            database=db
            )
except Error as e:
    print(e)

df_data = pd.read_csv('EEG1.csv')
data = df_data.iloc[6:,1:-2]
sql = "INSERT INTO eeg_data(`Fp1`,`F7`,`F3`,`T3`,`C3`,`T5`,`P3`,`O1`,`Fp2`,`F8`,`F4`,`T4`,`C4`,`T6`,`P4`,`O2`,`Fz`,`Cz`,`Pz`,`ECG`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for t in range(time_to_continue):
    for i in range(sample_rate):
        mycursor = mydb.cursor()
        val_list = data[l]
        val = tuple(val_list)
        mycursor.execute(sql, val)
        mydb.commit()
        l += 1
    time.sleep(1)
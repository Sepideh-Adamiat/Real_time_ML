# Real_time_ML
![img](https://github.com/Sepideh-Adamiat/Real_time_ML/blob/main/images/Diagram.png)
This is a code for managing real-time data and processing them with some machine learning algorithms.
This project is developed to connect to a sensor that generates data in each second. Before accessing the device I simulate this event with realtime_insert_to_db.py. This code reads records from an already existing CSV file which is gathered from a previous experiment and inserts a fixed number of them (sample rate = 256) into the database in each second.

main.py file loads all records that already are inserted in the database and puts them on a queue to be processed, and the results will insert into another table of the database. ml.py file should contain all codes for preprocessing and prediction. Here I put a neural network written with Keras as an example. This network is pre-trained, and here I just load weights.

The user interface of the application is connected to DB to present the data and the result of machine learning’s prediction in real-time.

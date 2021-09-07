# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:48:30 2021

@author: sepideh
"""
from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model


model = Sequential()
model.add(Dense(500, activation='relu', input_dim=304))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(6, activation='softmax'))

model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

model = load_model('myModel.h5')



class classifiers():
    def neuralnetwork(x_input):
        return model.predict(x_input)

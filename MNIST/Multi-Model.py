#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:38:50 2017

@author: akashsrihari
"""

import pandas as pd
from sklearn.externals import joblib
import numpy as np
import time

rf = joblib.load('Random_Forest.pkl')
mlp = joblib.load('Neural_Network.pkl')

X_test = pd.read_csv("Test_Data_Table.csv")
y_test = X_test.label
X_test = X_test.drop(X_test.columns[0], axis=1)
X_test = X_test.drop(labels=['label'], axis=1)

X_train = pd.read_csv("Data_Table_Preprocessed.csv")
X_train = X_train.drop(X_train.columns[0], axis=1)

X_final_test = pd.DataFrame()

for i in X_train.columns:
    X_final_test[i] = X_test[i]

no_predict = 0
confusion = np.zeros([10,10])
correct = 0
for i in range(10000):
    print i
#    X = X_final_test.loc[i].reshape([1,-1])
#    y = y_test.loc[i]
    start = time.clock()
    x = X_final_test.loc[i].reshape([1,-1])
    op1 = mlp.predict(x)
    op2 = rf.predict(x)
    if mlp.predict_proba(x).max() > 0.9 and rf.predict_proba(x).max() > 0.6:
        if op1==op2:
            confusion[y_test.loc[i],op1] += 1
            total = time.clock() - start
            if y_test==op1:
                correct += 1
        else:
            no_predict += 1
            total = time.clock() - start
    else:
        no_predict += 1
        total = time.clock() - start
    print "Correct - ",correct
    print "time ",total
    print "No Predictions - ", no_predict
    
Output = pd.DataFrame(data=confusion)
print Output
Output.to_csv("Final_Output.csv")
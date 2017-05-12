import numpy as np
import pandas as pd

#Generate the basic dimension table for training dataset

X_train = np.load("X_train.npy")
y_train = np.load("y_train.npy")

X_train = X_train.reshape([60000,784])

col_list=[]
for i in range(784):
    col_list.append("col" + str(i))  
    
X_train = pd.DataFrame(data=X_train, columns=col_list)
    
X_train.to_csv("Data_Table.csv")

#Execute the file Data_Preprocess.py after this
#DO NOT FORGET to execute Test_Table_Gen.py
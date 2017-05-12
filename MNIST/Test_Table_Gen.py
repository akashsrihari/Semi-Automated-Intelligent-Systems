import numpy as np
import pandas as pd

X_test = np.load("X_test.npy")
y_test = np.load("y_test.npy")

X_test = X_test.reshape([10000,784])

col_list=[]
for i in range(784):
    col_list.append("col" + str(i))  
    
X_test = pd.DataFrame(data=X_test, columns=col_list)
X_test['label'] = y_test
X_test.to_csv("Test_Data_Table.csv")
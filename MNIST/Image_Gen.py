import pandas as pd
import numpy as np
import time
from pylab import *

X_train = pd.read_csv("Data_Table_Preprocessed.csv")
X_Org = pd.read_csv("Data_Table.csv")
X_Org = X_Org.drop(X_Org.columns[0],axis=1)

print "Loaded datasets"

arr1 = np.array(X_Org.loc[0]).reshape([28,28])
imshow(arr1,cmap=cm.gray)
show()

for i in range(784):
    str1 = "col" + str(i)
    if str1 not in X_train.columns:
        X_Org[str1] = 0.4

print "Begin printing"

arr1 = np.array(X_Org.loc[0]).reshape([28,28])
imshow(arr1,cmap=cm.gray)
show()
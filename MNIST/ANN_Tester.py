import pandas as pd
from sklearn.externals import joblib
import numpy as np
import time

mlp = joblib.load('Neural_Network.pkl')

X_test = pd.read_csv("Test_Data_Table.csv")
y_test = X_test.label
X_test = X_test.drop(X_test.columns[0], axis=1)
X_test = X_test.drop(labels=['label'], axis=1)

X_train = pd.read_csv("Data_Table_Preprocessed.csv")
X_train = X_train.drop(X_train.columns[0], axis=1)

y_train = np.load("y_train.npy")
X_train['label'] = y_train
y_train = X_train.label
X_train = X_train.drop(labels=['label'], axis=1)

X_final_test = pd.DataFrame()

for i in X_train.columns:
    print i
    X_final_test[i] = X_test[i]

confusion = np.zeros([10,10])

for i in range(10000):
    print i
    X = X_final_test.iloc[i].reshape(1,-1)
    y = y_test.loc[i]
    op = mlp.predict(X)
    confusion[y,op] = confusion[y,op] + 1

sum = 0

for i in range(10):
    sum+= confusion[i,i]
print sum

Output = pd.DataFrame(data=confusion)
print Output
Output.to_csv("ANN_Result.csv")
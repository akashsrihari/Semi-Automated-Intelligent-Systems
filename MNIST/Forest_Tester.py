import pandas as pd
from sklearn.externals import joblib
import numpy as np
rf = joblib.load('Random_Forest.pkl')

X_test = pd.read_csv("Test_Data_Table.csv")
y_test = X_test.label
X_test = X_test.drop(X_test.columns[0], axis=1)
X_test = X_test.drop(labels=['label'], axis=1)

X_train = pd.read_csv("Data_Table_Preprocessed.csv")
X_train = X_train.drop(X_train.columns[0], axis=1)

X_final_test = pd.DataFrame()

for i in X_train.columns:
    X_final_test[i] = X_test[i]

#print rf.score(X_final_test,y_test)

confusion = np.zeros([10,10])

for i in range(10000):
    print i
    X = X_final_test.iloc[i].reshape(1,-1)
    y = y_test.loc[i]
    op = rf.predict(X)
    confusion[y,op] = confusion[y,op] + 1

sum = 0

for i in range(10):
    sum+= confusion[i,i]
print sum

Output = pd.DataFrame(data=confusion)
print Output
Output.to_csv("Forest_Result.csv")
import pandas as pd
from sklearn.feature_selection import SelectKBest
import numpy as np

X_train = pd.read_csv("Data_Table.csv")
X_train = X_train.drop(X_train.columns[0], axis=1)
X_train['class_label'] = np.load("y_train.npy")
y_train = X_train.class_label
X_train = X_train.drop(labels=['class_label'],axis=1)

#Remove the extra columns which do not contribute to the analysis

sel = SelectKBest(k=500)
sel.fit_transform(X_train,y_train)
columns = X_train.columns
labels = [columns[x] for x in sel.get_support(indices=True) if x]
X_train = pd.DataFrame(sel.fit_transform(X_train,y_train), columns=labels)

X_train.to_csv("Data_Table_Preprocessed.csv")

#After this, execute Neural_Network.py and other classifiers to train them
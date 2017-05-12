import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

X_train = pd.read_csv("Data_Table_Preprocessed.csv")
print "Loaded dataset"
X_train = X_train.drop(X_train.columns[0], axis=1)
y_train = np.load("y_train.npy")
X_train['label'] = y_train
y_train = X_train.label
X_train = X_train.drop(labels=['label'], axis=1)
print "Creating Random Forest"
rf = RandomForestClassifier(n_estimators=500)
rf.fit(X_train,y_train)

from sklearn.externals import joblib
joblib.dump(rf, 'Random_Forest.pkl')
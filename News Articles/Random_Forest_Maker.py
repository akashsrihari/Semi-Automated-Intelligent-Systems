import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

X_train = pd.read_csv("Feature_Selected_Data.csv")
print "Loaded dataset"
X_train = X_train.drop(X_train.columns[0], axis=1)
y_train = X_train.class_label
y_train = y_train.map({'Sports':0, 'Tech':1, 'Entertainment':2})
X_train = X_train.drop(labels=['class_label'], axis=1)
print "Creating Random Forest"
rf = RandomForestClassifier(n_estimators=512)
rf.fit(X_train,y_train)

from sklearn.externals import joblib
joblib.dump(rf, 'Random_Forest.pkl')
import pandas as pd

X_train = pd.read_csv("Feature_Selected_Data.csv")
X_train = X_train.drop(X_train.columns[0], axis=1)
y_train = X_train.class_label
y_train = y_train.map({'Sports':0, 'Tech':1, 'Entertainment':2})
X_train = X_train.drop(labels=['class_label'], axis=1)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(alpha=1e-05, random_state=1, solver='lbfgs', max_iter=500, activation='logistic', hidden_layer_sizes=(100,100))
mlp.fit(X_train, y_train)

from sklearn.externals import joblib
joblib.dump(mlp, 'Neural_Network.pkl')
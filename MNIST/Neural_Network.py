import pandas as pd
import numpy as np

X_train = pd.read_csv("Data_Table_Preprocessed.csv")
print "Loaded dataset"
X_train = X_train.drop(X_train.columns[0], axis=1)
y_train = np.load("y_train.npy")
X_train['label'] = y_train
y_train = X_train.label
X_train = X_train.drop(labels=['label'], axis=1)
print "Creating ANN"
from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(alpha=1e-05, random_state=1, solver='adam', max_iter=500, activation='logistic', hidden_layer_sizes=(1500))
print "Training ANN"
mlp.fit(X_train, y_train)
print "ANN Done"
print "Hidden Layers - ",mlp.hidden_layer_sizes, mlp.n_layers_
from sklearn.externals import joblib
joblib.dump(mlp, 'Neural_Network.pkl')
import pandas as pd
from sklearn.externals import joblib
from Tokenizer_Test import tokenize
import time

rf = joblib.load('Random_Forest.pkl')

X = pd.read_csv("Feature_Selected_Data.csv")
X = X.drop(X.columns[0], axis=1)
X = X.drop(labels=['class_label'], axis=1)

num_sports = 0
num_tech = 0
num_enter = 0

for i in range(900):
    
    print "\nArticle number " + str(i)
    file_name = "Tech_Test/Tech" + str(i) + ".txt"
    tokens = tokenize(file_name)
    print "\nNumber of tokens - " + str(len(tokens))
    new_list = []
    
    for i in X.columns:
        if i in tokens:
            new_list.append(tokens.count(i))
        else:
            new_list.append(0)
            
    X_test = pd.DataFrame(columns=X.columns)
    X_test.loc[0] = new_list
              
    start = time.clock()
    op = rf.predict(X_test)
    if op[0] == 0:
        num_sports = num_sports + 1
    elif op[0] == 1:
        num_tech = num_tech + 1
    elif op[0] == 2:
        num_enter = num_enter + 1
    
    total = time.clock() - start
    
    print "\nNumber of sports classifications - ", num_sports
    print "\nNumber of tech classifications - ", num_tech
    print "\nNumber of enter classifications - ", num_enter
    print "\nTime taken - ", total
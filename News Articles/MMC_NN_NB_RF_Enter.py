#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:31:11 2017

@author: akashsrihari
"""

from Tokenizer_Test import tokenize
import time
import pandas as pd
from sklearn.externals import joblib
from Article_Probab import art_probab
from nltk.stem import WordNetLemmatizer

sports = 0
tech = 0
enter = 0
noclue = 0

df = pd.read_csv('Feature_Selected_Data.csv')
df = df.drop(df.columns[0], axis=1)
X = pd.DataFrame(df)

df1 = df[df.class_label == 'Sports']
df2 = df[df.class_label == 'Tech']
df3 = df[df.class_label == 'Entertainment']

df1 = df1.drop(labels = ['class_label'], axis=1)
df2 = df2.drop(labels = ['class_label'], axis=1)
df3 = df3.drop(labels = ['class_label'], axis=1)

#Calculate probabilities for Sports, Tech and Entertainment label by reading the saved dictionaries
    
word_probab_s = pd.read_csv("Sports_Dict_feature.csv")
word_probab_s = word_probab_s.drop(word_probab_s.columns[0], axis=1)
word_probab_s = word_probab_s.drop(df.index[0], axis=0)
word_probab_s = word_probab_s.set_index('0').to_dict()
word_probab_s = word_probab_s['1']
word_probab_t = pd.read_csv("Tech_Dict_feature.csv")
word_probab_t = word_probab_t.drop(word_probab_t.columns[0], axis=1)
word_probab_t = word_probab_t.drop(df.index[0], axis=0)
word_probab_t = word_probab_t.set_index('0').to_dict()
word_probab_t = word_probab_t['1']
word_probab_e = pd.read_csv("Enter_Dict_feature.csv")
word_probab_e = word_probab_e.drop(word_probab_e.columns[0], axis=1)
word_probab_e = word_probab_e.drop(df.index[0], axis=0)
word_probab_e = word_probab_e.set_index('0').to_dict()
word_probab_e = word_probab_e['1']

X = X.drop(labels=['class_label'], axis=1)

mlp = joblib.load('Neural_Network.pkl')
rf = joblib.load('Random_Forest.pkl')
wnl = WordNetLemmatizer()

for i in range(900):
    start = time.clock()
    print "Article number " + str(i)
    file_name = "Enter_Test/Enter" + str(i) + ".txt"
    tokens = tokenize(file_name)
    print "Number of tokens - " + str(len(tokens))
    
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    
    for i in range(len(tokens)):
        tokens[i] = wnl.lemmatize(tokens[i])
    
    s_count = 0
    t_count = 0
    e_count = 0
    
    #Create entry for ANN
    new_list = []
    
    for i in X.columns:
        if i in tokens:
            new_list.append(tokens.count(i))
        else:
            new_list.append(0)
            
    X_test = pd.DataFrame(columns=X.columns)
    X_test.loc[0] = new_list
    
    #Predict ANN
    op = mlp.predict(X_test)
    if mlp.predict_proba(X_test).max() > 0.9999:
        if op[0] == 0:
            s_count = s_count + 1
        elif op[0] == 1:
            t_count = t_count + 1
        elif op[0] == 2:
            e_count = e_count + 1
        
    #Predict RF
    op = rf.predict(X_test)
    if rf.predict_proba(X_test).max() > 0.8:
        if op[0] == 0:
            s_count = s_count + 1
        elif op[0] == 1:
            t_count = t_count + 1
        elif op[0] == 2:
            e_count = e_count + 1
    
    #Predict Naive Bayes
    prob_s = art_probab(df, df1, word_probab_s, 1, tokens)
    prob_t = art_probab(df, df2, word_probab_t, 1, tokens)
    prob_e = art_probab(df, df3, word_probab_e, 1, tokens)
    
    if prob_s > prob_t:
        if prob_s > prob_e:
            s_count += 1
        else:
            e_count += 1
    elif prob_t > prob_e:
        t_count += 1
    else:
        e_count += 1    
            
    if s_count == 3:
        sports += 1
    elif t_count == 3:
        tech += 1
    elif e_count == 3:
        enter += 1
    else:
        noclue += 1
        
    print "Sports - ", sports
    print "Tech - ", tech
    print "Enter - ", enter
    print "No prediction - ", noclue
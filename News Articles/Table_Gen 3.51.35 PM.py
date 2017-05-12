#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 21:28:33 2016

@author: akashsrihari
"""
import re
import pandas as pd
import numpy
from Tokenizer import make_tokens
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D
from Word_Probab import probab
import time

#Read files and generate tokens
start = time.clock()
s_file = 'Sports_data/Sports'
t_file = 'Tech_data/Tech'
e_file = 'Entertainment_data/Enter'
file_ext = '.txt'
all_tokens = []
individual_tokens_sport = []
individual_tokens_tech = []
individual_tokens_enter = []
num_sports = 2700
num_tech = 2700
num_enter = 2700

#Generate tokens for sports, tech and entertainment

all_tokens, individual_tokens_sport = make_tokens(num_sports, s_file, file_ext, all_tokens)
all_tokens, individual_tokens_tech = make_tokens(num_tech, t_file, file_ext, all_tokens)
all_tokens, individual_tokens_enter = make_tokens(num_enter, e_file, file_ext, all_tokens)

print "\nNumber of tokens read initially: "
print len(all_tokens)

#Remove capitalization

for i in range(len(all_tokens)):
    all_tokens[i] = all_tokens[i].lower()
print "\nRemoved Capitalization for all tokens"
for i in range(len(individual_tokens_sport)):
    for j in range(len(individual_tokens_sport[i])):
        individual_tokens_sport[i][j] = individual_tokens_sport[i][j].lower()
    for j in range(len(individual_tokens_tech[i])):
        individual_tokens_tech[i][j] = individual_tokens_tech[i][j].lower()
    for j in range(len(individual_tokens_enter[i])):
        individual_tokens_enter[i][j] = individual_tokens_enter[i][j].lower()
print "\nRemoved Capitalization for indi tokens"

#Lemma Reduction

wnl = WordNetLemmatizer()
for i in range(len(all_tokens)):
    all_tokens[i] = wnl.lemmatize(all_tokens[i])
print "\nApplied Lemma Reduction for indi tokens"
for i in range(len(individual_tokens_sport)):
    for j in range(len(individual_tokens_sport[i])):
        individual_tokens_sport[i][j] = wnl.lemmatize(individual_tokens_sport[i][j])
    for j in range(len(individual_tokens_tech[i])):
        individual_tokens_tech[i][j] = wnl.lemmatize(individual_tokens_tech[i][j])
    for j in range(len(individual_tokens_enter[i])):
        individual_tokens_enter[i][j] = wnl.lemmatize(individual_tokens_enter[i][j])
print "\nApplied Lemma Reduction for indi tokens"
    
#Removing duplicates

new_tokens = []

for i in all_tokens:
    if i not in new_tokens:
        new_tokens.append(i)
    
print "\nNumber of tokens after removing duplicates: "
#print new_tokens
print len(new_tokens)

all_tokens = list(new_tokens)

#Removing stop words

stop_words = open('english.txt','r')
stop_words = stop_words.read()
stop_words = stop_words.strip().split()
all_tokens = [x for x in all_tokens if x not in stop_words]

print "\nNumber of tokens after removing stop words: "
print len(all_tokens)

#Remove numbers from list of tokens
new_all_tokens = []

cur_len = len(all_tokens)
for i in range(cur_len):
    if(re.match("^\d+\w*",all_tokens[i]) == None):
        new_all_tokens.append(all_tokens[i])

all_tokens = list(new_all_tokens)

print "\nNumber of tokens after removing numbers: "
print len(all_tokens) 

#Create dataframe with tokens as column names
df = pd.DataFrame(numpy.zeros((num_sports + num_tech + num_enter,len(all_tokens))), columns = all_tokens)
label_list = [];

#Create Class_label column
for i in range(num_sports):
    label_list.append('Sports')   
for i in range(num_tech):
    label_list.append('Tech') 
for i in range(num_enter):
    label_list.append('Entertainment') 
df['class_label'] = pd.Series(data=label_list, index=df.index)

#Calculate word counts per individual document with respect to all tokens
all_columns = df.columns
print "\nCalculating word counts per document for sports"
for i in range(num_sports):
    cur_toks = individual_tokens_sport[i]
    for j in cur_toks:
        if j in all_columns:
            df.loc[i,j] = df.loc[i,j]+1

print "\nCalculating word counts per document for tech"

for i in range(num_tech):
    cur_toks = individual_tokens_tech[i]
    for j in cur_toks:
        if j in all_columns:
            df.loc[i + num_sports,j] = df.loc[i + num_sports,j]+1

print "\nCalculating word counts per document for enter"

for i in range(num_enter):
    cur_toks = individual_tokens_enter[i]
    for j in cur_toks:
        if j in all_columns:
            df.loc[i + num_sports + num_tech,j] = df.loc[i + num_sports + num_tech,j]+1

#Save entire table

print "\nSaving word counts table..."

df.to_csv('Data_Table.csv')

#Generate probability dictionaries
"""
print "\nGenerating probability dictionaries..."

df1 = df[df.class_label == 'Sports']
df2 = df[df.class_label == 'Tech']
df3 = df[df.class_label == 'Entertainment']

df1 = df1.drop(labels = ['class_label'], axis=1)
df2 = df2.drop(labels = ['class_label'], axis=1)
df3 = df3.drop(labels = ['class_label'], axis=1)

print "\nGenerating probability dictionary for sports"
word_probab_s, min_s, max_s = probab(df1)
print "\nGenerating probability dictionary for tech"
word_probab_t, min_t, max_t = probab(df2)
print "\nGenerating probability dictionary for enter"
word_probab_e, min_e, max_e = probab(df3)

df1 = pd.DataFrame(word_probab_s.items())
df2 = pd.DataFrame(word_probab_t.items())
df3 = pd.DataFrame(word_probab_e.items())

#Save the dictionaries here

print "\nSaving word dictionaries"

df1.to_csv("Sports_Dict.csv")
df2.to_csv("Tech_Dict.csv")
df3.to_csv("Enter_Dict.csv")

print "Time taken to generate word dictionaries of probabilities:"
print time.clock() - start

#Apply PCA on dataframe

print "\nStarting data reduction..."

df = df.drop(labels = ['class_label'], axis=1)

print "\nApplying PCA..."

from sklearn.decomposition import PCA
pca = PCA(n_components=3)
pca.fit(df)
PCA(copy=True, n_components=3, whiten=False)
T = pca.transform(df)

df = pd.DataFrame(T)
df['class_label'] = pd.Series(data=label_list, index=df.index)
df.columns = ['col1', 'col2', 'col3', 'class_label']

print "\nCreating scatter plot"

fig = pylab.figure()
ax = Axes3D(fig)

df1 = df[df.class_label == 'Sports']
df2 = df[df.class_label == 'Tech']
df3 = df[df.class_label == 'Entertainment']

ax.scatter(df1.col1, df1.col2, df1.col3, c='b', label='Sports')
ax.scatter(df2.col1, df2.col2, df2.col3, c='r', label='Tech')
ax.scatter(df3.col1, df3.col2, df3.col3, c='g', label='Entertainment')

plt.show()
"""
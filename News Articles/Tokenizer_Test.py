#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 16:15:46 2016

@author: akashsrihari
"""
import string
from string import punctuation
import re
from nltk.stem import WordNetLemmatizer

def tokenize(file_name):
    
    #Read test file
    file1 = open(file_name,'r')
    test_file = file1.read()
    file1.close()
    test_file = ''.join([i if ord(i) < 128 else ' ' for i in test_file]) 
    table = string.maketrans("","")
    test_file = test_file.translate(table, punctuation)
    tokens = test_file.strip().split()
        
    #Remove capitalization
        
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
        
    #Lemma Reduction
        
    wnl = WordNetLemmatizer()
    for i in range(len(tokens)):
        tokens[i] = wnl.lemmatize(tokens[i])
        
    #Remove stop words
    stop_words = open('english.txt','r')
    stop_words = stop_words.read()
    stop_words = stop_words.strip().split()
    tokens = [x for x in tokens if x not in stop_words]
    
    #Remove duplicates
    tokens = list(set(tokens))
    #print len(tokens)
        
    #Remove numbers from list of tokens
    new_tokens = []
        
    cur_len = len(tokens)
    for i in range(cur_len):
        if(re.match("\d+",tokens[i]) == None):
            new_tokens.append(tokens[i])
           
    tokens = list(new_tokens)
    return tokens
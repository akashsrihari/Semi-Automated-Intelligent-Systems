#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 10:40:56 2016

@author: akashsrihari
"""
import string
from string import punctuation

def make_tokens(num_files, file_name, file_ext, all_tokens):
    
    individual_tokens = []

    for i in range(num_files):
        full_file_name = file_name + str(i) + file_ext
        review=open(full_file_name,'r')
        review=review.read()
        review = ''.join([i if ord(i) < 128 else ' ' for i in review])  
        
        #Remove punctuation and generate tokens
        table = string.maketrans("","")
        review = review.translate(table, punctuation)
        tokens = review.strip().split()
              
        #Make separate list of tokens for all
        individual_tokens.append(tokens)
        
        #Merge all tokens
        all_tokens = all_tokens + tokens
        
    return all_tokens, individual_tokens
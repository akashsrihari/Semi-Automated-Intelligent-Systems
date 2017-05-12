#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:23:05 2016

@author: akashsrihari
"""

def art_probab(df, sub_df, word_probab, min_val, tokens):
    naive_prob = len(sub_df)/float(len(df)-1)
    
    for i in tokens:
        if (i not in word_probab):
            naive_prob = naive_prob * min_val
        else:
                naive_prob = naive_prob * word_probab[i]

    return naive_prob
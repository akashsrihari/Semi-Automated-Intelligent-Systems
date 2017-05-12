#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:06:16 2016

@author: akashsrihari
"""

#Define word probability function

def probab(df):
    word_probab = {}
    
    x = sum(sum(df.as_matrix()))
    y = len(df)
    
    for i in df.columns:
        word_probab[i] = sum(sum(df[[i]].as_matrix())) + 1.0
        word_probab[i] /= (x + y)

    return word_probab, 0, 0
    
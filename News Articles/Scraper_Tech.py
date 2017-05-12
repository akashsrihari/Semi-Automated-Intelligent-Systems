#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 21:38:33 2016

@author: akashsrihari
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("Tech1.html"),"lxml")

letters = soup.find_all(attrs={"itemprop":"articleBody"})

paragraph = []

for x in letters:
    paragraph.append(str(x))
    
print len(paragraph)

file_start = "Tech_data/Tech"
file_ext = ".txt"

for i in range(2700):
    print i
    paragraph[i] = paragraph[i].replace("<div itemprop=\"articleBody\">", "")
    paragraph[i] = paragraph[i].replace("</div>", "")
    file_name = file_start + str(i) + file_ext
    fp = open(file_name, "w")
    fp.write(paragraph[i])
    fp.close()

file_start = "Tech_Test/Tech"

for i in range(2700,3600):
    print i
    paragraph[i] = paragraph[i].replace("<div itemprop=\"articleBody\">", "")
    paragraph[i] = paragraph[i].replace("</div>", "")
    file_name = file_start + str(i-2700) + file_ext
    fp = open(file_name, "w")
    fp.write(paragraph[i])
    fp.close()
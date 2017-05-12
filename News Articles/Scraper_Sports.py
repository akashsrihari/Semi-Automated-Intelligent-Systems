#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:33:07 2016

@author: akashsrihari
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("Sports1.html"), "lxml")

letters = soup.find_all(attrs={"itemprop":"articleBody"}, id=False)

paragraph = []

for x in letters:
    paragraph.append(str(x))

file_start = "Sports_data/Sports"
file_ext = ".txt"

print len(paragraph)

for i in range(2700):
    print i
    paragraph[i] = paragraph[i].replace("<div itemprop=\"articleBody\">", "")
    paragraph[i] = paragraph[i].replace("</div>", "")
    file_name = file_start + str(i) + file_ext
    fp = open(file_name, "w")
    fp.write(paragraph[i])
    fp.close()
    
file_start = "Sports_Test/Sports"

for i in range(2700,3600):
    print i
    paragraph[i] = paragraph[i].replace("<div itemprop=\"articleBody\">", "")
    paragraph[i] = paragraph[i].replace("</div>", "")
    file_name = file_start + str(i-2700) + file_ext
    fp = open(file_name, "w")
    fp.write(paragraph[i])
    fp.close()

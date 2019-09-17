# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 17:50:13 2019

@author: Ahmed khaled
"""
"""
This code to get the first result "URL link" found on google
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

start_time = time.time()
    
df = pd.read_csv('EgyptUniversities.csv', encoding = "ISO-8859-1") #Replace it with your country file.csv
Institution_Name = df['Institution Name']
links = []
for row in Institution_Name:
    # if u need fb page, twitter page or linkedin remove the hashtag 
    goog_search = "https://www.google.co.uk/search?sclient=psy-ab&client=ubuntu&hs=k5b&channel=fs&biw=1366&bih=648&noj=1&q=" + row #+"linkedin" OR #"facebook" OR #"twitter"
    r = requests.get(goog_search)
    soup = BeautifulSoup(r.text, "html.parser")
    text = soup.find('cite').text
    print(soup.find('cite').text)
    links.append(text)
    
    #print("https://www.google.com/maps/search/"+row) # -> to get google maps URL
#

#
#
#end_time = time.time()
#print(end_time - start_time)


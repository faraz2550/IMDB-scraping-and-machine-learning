# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 08:26:51 2016

@author: Faraz Fattah
"""

import os
os.chdir('D:\DataScience\Data Wrangling with MongoDB\practice\All imdb pages')
import urllib
import urllib2
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd

###########
# aquiaring title's serial code
pagesimdb500=data1

data=[]
def get_titles_links(p1,p2):
    search='http://www.imdb.com/search/title?groups=oscar_nominees&page='
    for i in range(p1,p2):
        check=True
        page_num=i
        print 'Downloading Page ' + str(page_num) + '\n'
        search_url=search + str(page_num)
        while check:
            try:
                urllib.urlretrieve(search_url, "search_url%s.html" %i)
                search_page='search_url%s.html' %i
                with open(search_page,'r') as page:
                    soup=BeautifulSoup(page,'lxml')
                    for q in soup.find_all('h3'):
                        for j in q.find_all('a'):
                            if len(j.get('href'))==32:
                                a=[0,0]
                                a[0]= j.text
                                a[1]= j.get('href').split('?')[0]
                                data.append(a)
                print 'Page %d is Done \n' %page_num
                check=False
            except IOError:
                print 'IOError Occured, trying again...'
                time.sleep(3)
                pass
    dataf.to_csv('all_nominated.csv',index=False)
    return

get_titles_links(1,95)



##################
# this is gathering data with current files downloaded with previous function
data=[]
def get_titles_links(p1,p2):
    search='http://www.imdb.com/search/title?groups=oscar_nominees&page='
    for i in range(p1,p2):
        check=True
        page_num=i
        print 'Downloading Page ' + str(page_num) + '\n'
        search_url=search + str(page_num)
        while check:
            try:
                search_page='search_url%s.html' %i
                with open(search_page,'r') as page:
                    soup=BeautifulSoup(page,'lxml')
                    for q in soup.find_all('h3'):
                        for j in q.find_all('a'):
                            if len(j.get('href'))==32:
                                a=[0,0]
                                a[0]= j.text.encode('utf-8')
                                a[1]= j.get('href').split('?')[0]
                                data.append(a)
                print 'Page %d is Done \n' %page_num
                check=False
            except IOError:
                print 'IOError Occured, trying again...'
                time.sleep(3)
                pass
    return 

get_titles_links(1,95)
dataf=pd.DataFrame(data)
dataf.to_csv('all_nominated.csv',index=False)

##      now im gonna download all the pages, 1.35 GB !!! :(

data=[]
with open('all_nominated.csv','r') as f:
    reader=csv.reader(f)
    for r in reader:
            data.append(r)
    data=data[1:]
    dataf=pd.DataFrame(data)  
def get_pages(p1,p2):
    search='http://www.imdb.com'    
    for i in range(p1,p2):
        check=True
        page_num=i
        print 'Downloading Page ' + str(page_num)
        search_url=search + dataf.iloc[i][1]
        while check:
            try:
                urllib.urlretrieve(search_url, "%d-%s.html"  %(i,dataf.iloc[i][0].replace(':','').replace('?','').replace('/','')))
                print 'Page %d is Done' %page_num
                check=False
            except IOError:
                print 'IOError Occured, trying again...'
                time.sleep(1)
                pass
    return

get_pages(4522,4688)









                               
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                













# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 08:26:51 2016

@author: Faraz Fattah
"""

import os
os.chdir('D:\Coursera\Data Wrangling with MongoDB\practice\All imdb pages')
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

os.chdir('D:\Coursera\Data Wrangling with MongoDB\practice\All imdb pages')

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


############   mining the html's

data=[]
with open('all_nominated.csv','r') as f:
        the_list=[]
        for i in csv.reader(f):
            the_list.append(i)  
the_list=the_list[1:]
data=pd.DataFrame()

def web_scraper(p1,p2):
    for i in range(p1,p2):
        page_num=i
        print 'Scraping Page ' + str(page_num) 
        search_page='%s-%s.html' %(i,the_list[i][0].replace(':','').replace('?','').replace('/',''))
        data[i][0]=the_list[i][1]
        data[i][1]=the_list[i][0].replace(':','').replace('?','').replace('/','')
        with open(search_page,'r') as page:
            soup=BeautifulSoup(page,'lxml')
            for q in soup.find(itemprop='ratingValue'):
                data[i][2]=q
            for q in soup.find(itemprop='ratingCount'):
                data[i][3]=q.replace(',','')
            
                for j in q.find_all('a'):
                    if len(j.get('href'))==32:
                        a=[0,0]
                        a[0]= j.text
                        a[1]= j.get('href').split('?')[0]
                        data.append(a)
            print 'Page %d is Done \n' %page_num
            check=False
    dataf.to_csv('all_nominated.csv',index=False)
    return

get_titles_links(1,95)


web_scraper(0,4)
search_page='1-The Revenant.html'
search_page='%s-%s.html' %(i,the_list[i][0].replace(':','').replace('?','').replace('/',''))
        with open(search_page,'r') as page:
            soup=BeautifulSoup(open(search_page),'lxml')
            print soup.h1
            for q in soup.find(itemprop="ratingCount"):
                print q.replace(',','')








                               
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                













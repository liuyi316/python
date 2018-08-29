#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import pandas as pd

rank = 1
def write_one_page(soup):
    global rank
    for k in soup.find('div',class_='article').find_all('div',class_='info'):
        name = k.find('div',class_='hd').find_all('span')
        score = k.find('div',class_='star').find_all('span')
        inq = k.find('p',class_='quote').find('span')
        
        #抓取年份、国家
        actor_infos_html = k.find(class_='bd')
        #strip() 方法用于移除字符串头尾指定的字符（默认为空格）
        actor_infos = actor_infos_html.find('p').get_text().strip().split('\n')
        actor_infos1 = actor_infos[0].split('\xa0\xa0\xa0')
        director = actor_infos1[0][3:]
        #print(movie_director)
        role = actor_infos[1]
        year_area = actor_infos[1].lstrip().split('\xa0/\xa0')
        year = year_area[0]
        #print(movie_year)
        country = year_area[1]
        #print(movie_country)
        type = year_area[2]
        
        print(rank,name[0].string,score[1].string,inq.string,year,country,type)
        #写txt
        write_to_file(rank,name[0].string,score[1].string,year,country,type,inq.string)
        
        rank=rank+1
        
def main(a):
    url = "https://movie.douban.com/top250?start="+str(a)+"&filter="
    f = requests.get(url)               
    soup = BeautifulSoup(f.content, "lxml")
    write_one_page(soup)

def write_to_file(rank,name,score,year,country,type,quote):
    with open('Top_250_movie.txt', 'a', encoding='utf-8') as f:
        f.write(str(rank)+';'+str(name)+';'+str(score)+';'+str(year)+';'+str(country)+';'+str(type)+';'+str(quote)+'\n')
        f.close()

def save_csv():
    data = list()
    with open('Top_250_movie.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(';')
            data.append(line[:])
        name=['rank','name','score','year','country','type','quote']
        test=pd.DataFrame(columns=name,data=data)
        test.to_csv('Top_250_movie.csv')
    
if __name__ == '__main__':
    for i in range(10):
        main(a=i*25)
    save_csv()

    


 
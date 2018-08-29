#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy as np
import sys, os
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import csv

plt.rcParams['font.sans-serif']=['Arial Unicode MS']

#得分与年份
def plot_score_year():
    
    year = list()
    score = list()
    
    with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        year_str = [row['year'] for row in reader ]
    with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        score_str = [row['score'] for row in reader ]
    
    for x in year_str:
        year.append(int(x))

    for y in score_str:
        score.append(float(y))
        
    plt.style.use('ggplot')
    plt.scatter(year,score)
    plt.xlabel('year')
    plt.ylabel('score')
    plt.title('电影年份')
    plt.show()

#得分与排名
def plot_score_rank():
    rank = list()
    score = list()
    
    with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        rank_str = [row['rank'] for row in reader ]
    with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        score_str = [row['score'] for row in reader ]
    
    for x in rank_str:
        rank.append(int(x))

    for y in score_str:
        score.append(float(y))
        
    plt.gca().invert_yaxis()   #反转y轴
    plt.style.use('ggplot')
    plt.scatter(score,rank)
    plt.xlabel('score')
    plt.ylabel('rank')
    plt.title('得分和排名')
    plt.show()
    
#电影类型统计
def plot_type():
    
    type = list()
    
    with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        type_str =' '.join([row['type'] for row in reader ])
        type_list = type_str.split(' ')
    #统计
    fan_zui = type_list.count('犯罪')
    ju_qing = type_list.count('剧情')
    ai_qing = type_list.count('爱情')
    dong_zuo = type_list.count('动作')
    xi_ju = type_list.count('喜剧')
    dong_hua = type_list.count('动画')
    ke_huan = type_list.count('科幻')
    ying_yue = type_list.count('音乐')
    zhan_zheng = type_list.count('战争')
    li_shi = type_list.count('历史')
    zai_nan = type_list.count('灾难')
    mao_xian = type_list.count('冒险')
    jing_song = type_list.count('惊悚')
    xuan_yi = type_list.count('悬疑')
    wu_xia = type_list.count('武侠')
    tong_xing = type_list.count('同性')
    
    #画图
    plt.rcParams['savefig.dpi'] = 300 #图片像素
    plt.rcParams['figure.dpi'] = 100 #分辨率
    plt.xlabel('movie type')
    plt.ylabel('count')
    plt.title('电影类型分析')
    data = [fan_zui, ju_qing, ai_qing, dong_zuo, xi_ju, dong_hua, ke_huan, ying_yue, zhan_zheng, li_shi, 
            zai_nan, mao_xian, jing_song, xuan_yi, wu_xia, tong_xing]
    labels = ['犯罪', '剧情', '爱情', '动作', '喜剧', '动画', '科幻', '音乐', '战争', '历史', '灾难', '冒险', '惊悚', '悬疑', '武侠', '同性']
    #排序
    mydict = dict(zip(data,labels))
    mydict_sort = sorted(mydict.items(), key=lambda e:e[0], reverse=True)
    mydict_sort = dict(mydict_sort)
    plt.bar(list(mydict_sort.values()), list(mydict_sort.keys()),color='darkred')
    plt.show()
    
#电影国家统计
def plot_country():
    
    country = list()
    with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        country_str =' '.join([row['country'] for row in reader ])
        country_list = country_str.split(' ')
    
    #统计
    America = country_list.count('美国')
    China = country_list.count('中国大陆')
    Japan = country_list.count('日本')
    Hongkong = country_list.count('香港')
    France = country_list.count('法国')
    Taiwan = country_list.count('台湾')
    Italy = country_list.count('意大利')
    Korea = country_list.count('韩国')
    England = country_list.count('英国')
    Germany = country_list.count('德国')
    India = country_list.count('印度')
    Espan = country_list.count('西班牙')
    
    #画图
    plt.rcParams['savefig.dpi'] = 300 #图片像素
    plt.rcParams['figure.dpi'] = 100 #分辨率
    plt.xlabel('country')
    plt.ylabel('count')
    plt.title('国家分析')
    data = [America, China, Japan, Hongkong, France, Taiwan, Italy, Korea, England, Germany, India, Espan]
    labels = ['美国','中国','日本','香港','法国','台湾','意大利',' 韩国','英国','德国','印度','西班牙']
    #排序
    mydict = dict(zip(data,labels))
    mydict_sort = sorted(mydict.items(), key=lambda e:e[0], reverse=True)
    mydict_sort = dict(mydict_sort)
    plt.bar(list(mydict_sort.values()), list(mydict_sort.keys()),color='lightblue')
    plt.show()
    
#统计优化
def plot_country_opt():
    
    country = list()
    
    with open('Top_250_movie.csv','r',encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        country_str =' '.join([row['country'] for row in reader ])
        country_list = country_str.split(' ')
    
    #统计
    country_set = set(country_list)
    for item in country_set:
        country.append(country_list.count(item))
    country_set = list(country_set)
    
    #排序和画图
    plt.rcParams['savefig.dpi'] = 300 #图片像素
    plt.rcParams['figure.dpi'] = 200 #分辨率
    plt.xlabel('country')
    plt.ylabel('count')
    plt.title('国家分析')
    plt.tick_params(labelsize=7)   #字体设置
    
    mydict = dict(zip(country,country_set))
    mydict_sort = sorted(mydict.items(), key=lambda e:e[0], reverse=True)
    mydict_sort = dict(mydict_sort)
    plt.bar(list(mydict_sort.values()), list(mydict_sort.keys()),color='lightblue')
    plt.show()
    

if __name__ == '__main__':
    plot_score_year()   #得分与年份
    plot_type()     #电影类型统计
    plot_country()      #电影国家统计
    plot_country_opt()      #统计优化算法
    plot_score_rank()       #得分与排名
    




from selenium import webdriver
from pandas import *
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import *
import re

path_to_chromedriver = 'C:/Users/Keatn/Desktop/Keaton\'s Files/CSULB/Classes 18-19/CECS 456/Term Project/chromedriver.exe' # Path to access a chrome driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

url = 'https://stats.nba.com/players/defense/?sort=DEF_WS&dir=-1&Season=2017-18&SeasonType=Regular%20Season'
browser.get(url)

browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[3]/div/div/select/option[1]').click()

table = browser.find_element_by_class_name('nba-stat-table__overflow')

#print(table.text)

player_ids = []
player_names = []
player_stats = []

#f = open('tableTest.txt', 'w')
#for lines in enumerate(table.text.split('\n')):
#    f.write(str(lines))
#f.close()

for line_id, lines in enumerate(table.text.split('\n')):
    if line_id < 10:
        print(lines)
    else:
        if line_id % 3 == 1:
            player_ids.append(lines)
            #('player_id', player_ids)
        if line_id % 3 == 2:
            player_names.append(lines)
            #print('player_name', player_names)
        if line_id % 3 == 0:
            #s = lines.split(' ', 1)[1]
            #re.split('[a-z]+', lines)
            #print('player_stats', lines)
            player_stats.append( [i for i in lines.split(' ')] )
            #player_stats.append( [float(i) for i in s])
            
            
db = pandas.DataFrame({'PLAYER': player_names,
                       'TEAM': [i[0] for i in player_stats],
                       'AGE': [i[1] for i in player_stats],
                       'GP': [i[2] for i in player_stats],
                       'W': [i[3] for i in player_stats], 
                       'L': [i[4] for i in player_stats],
                       'MIN': [i[5] for i in player_stats],
                       'DEF_RTG': [i[6] for i in player_stats],
                       'DREB': [i[7] for i in player_stats],
                       'DREB%': [i[8] for i in player_stats],
                       '%DREB': [i[9] for i in player_stats],
                       'STL': [i[10] for i in player_stats],
                       'STL%': [i[11] for i in player_stats],
                       'BLK': [i[12] for i in player_stats],
                       '%BLK': [i[13] for i in player_stats],
                       'OPP_PTS_OFF_TOV': [i[14] for i in player_stats],
                       'OPP_PTS_2ND_CHANCE': [i[15] for i in player_stats],
                       'OPP_PTS_FB': [i[16] for i in player_stats],
                       'OPP_PTS_PAINT': [i[17] for i in player_stats],
                       'DEF_WS': [i[18] for i in player_stats]
                       }
                     )


db = db[
        [
        'PLAYER',
         #'TEAM',
         #'AGE',
         #'GP',
         #'W',
         #'L',
         #'MIN',
         'DEF_RTG',
         #'DREB',
         #'DREB%',
         #'%DREB',
         #'STL',
         #'STL%',
         #'BLK',
         #'%BLK',
         #'OPP_PTS_OFF_TOV',
         #'OPP_PTS_2ND_CHANCE',
         #'OPP_PTS_FB',
         #'OPP_PTS_PAINT',
         'DEF_WS'
         ]
      ]
        
db.to_csv('performance.csv')
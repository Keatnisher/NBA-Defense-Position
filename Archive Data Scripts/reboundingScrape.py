from selenium import webdriver
from pandas import *
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import *
import re

path_to_chromedriver = 'C:/Users/Keatn/Desktop/Keaton\'s Files/CSULB/Classes 18-19/CECS 456/Term Project/chromedriver.exe' # Path to access a chrome driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

url = 'https://stats.nba.com/players/defensive-rebounding/?Season=2017-18&SeasonType=Regular%20Season'
browser.get(url)

browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select/option[1]').click()

table = browser.find_element_by_class_name('nba-stat-table__overflow')

#print(table.text)

player_ids = []
player_names = []
player_stats = []

#f = open('rebounding.txt', 'w')
#for lines in enumerate(table.text.split('\n')):
#    f.write(str(lines))
#f.close()


for line_id, lines in enumerate(table.text.split('\n')):
    if line_id < 8:
        print(lines)
    else:
        if line_id % 2 == 0:
            player_names.append(lines)
            #print('player_name', player_names)
        if line_id % 2 == 1:
            #s = lines.split(' ', 1)[1]
            #re.split('[a-z]+', lines)
            #print('player_stats', lines)
            player_stats.append( [i for i in lines.split(' ')] )
            #player_stats.append( [float(i) for i in s])
            

db = pandas.DataFrame({'PLAYER': player_names,
                       'TEAM': [i[0] for i in player_stats],
                       'GP': [i[1] for i in player_stats],
                       'W': [i[2] for i in player_stats],
                       'L': [i[3] for i in player_stats], 
                       'MIN': [i[4] for i in player_stats],
                       'DREB': [i[5] for i in player_stats],
                       'CONTESTED_DREB': [i[6] for i in player_stats],
                       'CONTEST_DREB%': [i[7] for i in player_stats],
                       'DREB_CHANCES': [i[8] for i in player_stats],
                       'DREB_CHANCE%': [i[9] for i in player_stats],
                       'DEFER_DREB_CHANCE': [i[10] for i in player_stats],
                       'ADJ_DREB_CHANCE%': [i[11] for i in player_stats], 
                       'AVG_DREB_DIST': [i[12] for i in player_stats]
                       }
                     )

db = db[
        [
        'PLAYER',
         #'TEAM',
         #'GP',
         #'W',
         #'L',
         #'MIN',
         'DREB',
         #'CONTESTED_DREB',
         'CONTEST_DREB%',
         #'DREB_CHANCES',
         #'DREB_CHANCE%',
         'DEFER_DREB_CHANCE',
         #'ADJ_DREB_CHANCE%',
         'AVG_DREB_DIST'
         ]
      ]
        
db.to_csv('reboundStats_Min.csv')
from selenium import webdriver
from pandas import *
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import *
import re

path_to_chromedriver = 'C:/Users/Keatn/Desktop/Keaton\'s Files/CSULB/Classes 18-19/CECS 456/Term Project/chromedriver.exe' # Path to access a chrome driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

url = 'https://stats.nba.com/players/defense-dash-overall/?Season=2017-18&SeasonType=Regular%20Season'

browser.get(url)

browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select/option[1]').click()

table = browser.find_element_by_class_name('nba-stat-table__overflow')

#print(table.text)

player_ids = []
player_names = []
player_stats = []

#f = open('shotStats.txt', 'w')
#for lines in enumerate(table.text.split('\n')):
#    f.write(str(lines))
#f.close()


for line_id, lines in enumerate(table.text.split('\n')):
    if line_id < 1:
        print(lines)
    else:
        if line_id % 2 == 1:
            player_names.append(lines)
            #print('player_name', player_names)
        if line_id % 2 == 0:
            #s = lines.split(' ', 1)[1]
            #re.split('[a-z]+', lines)
            #print('player_stats', lines)
            player_stats.append( [i for i in lines.split(' ')] )
            #player_stats.append( [float(i) for i in s])
            

db = pandas.DataFrame({'PLAYER': player_names,
                       'TEAM': [i[0] for i in player_stats],
                       'AGE': [i[1] for i in player_stats],
                       'POSITION': [i[2] for i in player_stats],
                       'GP': [i[3] for i in player_stats],
                       'G': [i[4] for i in player_stats], 
                       'FREQ': [i[5] for i in player_stats],
                       'DFGM': [i[6] for i in player_stats],
                       'DFGA': [i[7] for i in player_stats],
                       'DFG%': [i[8] for i in player_stats],
                       'FG%': [i[9] for i in player_stats],
                       'DIFF%': [i[10] for i in player_stats]
                       }
                     )

db = db[
        [
        'PLAYER',
         #'TEAM',
         #'AGE',
         #'POSITION',
         #'GP',
         #'G',
         'FREQ',
         'DFGM',
         'DFGA',
         'DFG%',
         #'FG%',
         #'DIFF%'
         ]
      ]
        
db.to_csv('shotStats.csv')
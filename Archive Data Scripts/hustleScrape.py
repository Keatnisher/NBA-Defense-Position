from selenium import webdriver
from pandas import *
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import *
import re

path_to_chromedriver = 'C:/Users/Keatn/Desktop/Keaton\'s Files/CSULB/Classes 18-19/CECS 456/Term Project/chromedriver.exe' # Path to access a chrome driver
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

url = 'https://stats.nba.com/players/hustle/?Season=2017-18&SeasonType=Regular%20Season'
browser.get(url)

browser.find_element_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select/option[1]').click()
                               
table = browser.find_element_by_class_name('nba-stat-table__overflow')

#print(table.text)

player_ids = []
player_names = []
player_stats = []

#f = open('tableTestHustle.txt', 'w')
#for lines in enumerate(table.text.split('\n')):
#    f.write(str(lines))
#f.close()

for line_id, lines in enumerate(table.text.split('\n')):
    if line_id < 7:
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
                       'GP': [i[2] for i in player_stats],
                       'MIN': [i[3] for i in player_stats], 
                       'SCREEN_AST': [i[4] for i in player_stats],
                       'DEFL': [i[5] for i in player_stats],
                       'LB_REC': [i[6] for i in player_stats],
                       'CHARGES_DRAWN': [i[7] for i in player_stats],
                       'CONT_2PT': [i[8] for i in player_stats],
                       'CONT_3PT': [i[9] for i in player_stats],
                       'CONT_ALL': [i[10] for i in player_stats]
                       }
                     )


db = db[
        [
        'PLAYER',
         'TEAM',
         'AGE',
         'GP',
         'MIN',
         'SCREEN_AST',
         'DEFL',
         'LB_REC',
         'CHARGES_DRAWN',
         'CONT_2PT',
         'CONT_3PT',
         'CONT_ALL'
         ]
      ]
        
db.to_csv('hustleStats.csv')

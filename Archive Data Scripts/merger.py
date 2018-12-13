from selenium import webdriver
from pandas import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import *
import re


path1 = 'C:/Users/Keatn/Desktop/Keaton\'s Files/CSULB/Classes 18-19/CECS 456/Term Project/baseTable.csv'
table1 = pd.read_csv(path1)

path2 = 'C:/Users/Keatn/Desktop/Keaton\'s Files/CSULB/Classes 18-19/CECS 456/Term Project/hustleStats.csv'
table2 = pd.read_csv(path2)

newTable = table1.merge(table2, how='left', on='PLAYER')

#newTable.to_csv('crazyShit.csv')

path3 = 'C:/Users/Keatn/Desktop/Keaton\'s Files/CSULB/Classes 18-19/CECS 456/Term Project/SpeedStats.csv'

path4 = 'C:/Users/Keatn/Desktop/Keaton\'s Files/CSULB/Classes 18-19/CECS 456/Term Project/reboundStats_Min.csv'

table3 = pd.read_csv(path3)

table4 = pd.read_csv(path4)

newNewTable = newTable.merge(table3, how='left', on='PLAYER')

#newNewTable.to_csv('crazierShit.csv')

newNewNewTable = newNewTable.merge(table4, how='left', on='PLAYER')

#newNewNewTable.to_csv('craziestShit.csv')

###################################################################
#Shot Stats Merger Here
###################################################################

path5 = 'C:/Users/Keatn/Desktop/Keaton\'s Files/CSULB/Classes 18-19/CECS 456/Term Project/shotStats.csv'
path6 = 'C:/Users/Keatn/Desktop/Keaton\'s Files/CSULB/Classes 18-19/CECS 456/Term Project/shotStats6ft.csv'
path7 = 'C:/Users/Keatn/Desktop/Keaton\'s Files/CSULB/Classes 18-19/CECS 456/Term Project/shotStats10ft.csv'
path8 = 'C:/Users/Keatn/Desktop/Keaton\'s Files/CSULB/Classes 18-19/CECS 456/Term Project/shotStats15ft.csv'

table5 = pd.read_csv(path5, header=0)
table6 = pd.read_csv(path6, header=0)
table7 = pd.read_csv(path7, header=0)
table8 = pd.read_csv(path8, header=0)

six10 = table6.merge(table7, how='left', on='PLAYER')
tempMerge = table5.merge(table7, how='left', on='PLAYER')
tenTo15 = tempMerge.merge(table8, how='left', on='PLAYER')

six10['10FREQ'] = six10['10FREQ'].str.replace('\%', '')
six10['6FREQ'] = six10['6FREQ'].str.replace('\%', '')

six10['10FREQ'] = pd.to_numeric(six10['10FREQ'])
six10['6FREQ'] = pd.to_numeric(six10['6FREQ'])

six10['6to10FREQ'] = six10['10FREQ'] - six10['6FREQ']
six10['6to10DFGM'] = six10['10DFGM'] - six10['6DFGM']
six10['6to10DFGA'] = six10['10DFGA'] - six10['6DFGA']
six10['6to10DFG%'] = six10['6to10DFGM'] / six10['6to10DFGA']

six10.drop(['Unnamed: 0_x','6FREQ','6DFGM','6DFGA','6DFG%','Unnamed: 0_y','10FREQ','10DFGM','10DFGA','10DFG%'], axis=1, inplace=True)

six10.to_csv('shotStats6_10ft.csv')

tenTo15['FREQ'] = tenTo15['FREQ'].str.replace('\%', '')
tenTo15['10FREQ'] = tenTo15['10FREQ'].str.replace('\%', '')
tenTo15['15FREQ'] = tenTo15['15FREQ'].str.replace('\%', '')

tenTo15['FREQ'] = pd.to_numeric(tenTo15['FREQ'])
tenTo15['10FREQ'] = pd.to_numeric(tenTo15['10FREQ'])
tenTo15['15FREQ'] = pd.to_numeric(tenTo15['15FREQ'])

tenTo15['10to15FREQ'] = tenTo15['FREQ'] - tenTo15['10FREQ'] - tenTo15['15FREQ']
tenTo15['10to15DFGM'] = tenTo15['DFGM'] - tenTo15['10DFGM'] - tenTo15['15DFGM']
tenTo15['10to15DFGA'] = tenTo15['DFGA'] - tenTo15['10DFGA'] - tenTo15['15DFGA']
tenTo15['10to15DFG%'] = tenTo15['10to15DFGM'] / tenTo15['10to15DFGA']

tenTo15.drop(['Unnamed: 0_x','FREQ','DFGM','DFGA','DFG%','Unnamed: 0_y','10FREQ','10DFGM','10DFGA','10DFG%','Unnamed: 0', '15FREQ','15DFGM','15DFGA','15DFG%'], axis=1, inplace=True)

tenTo15.to_csv('shotStats10_15ft.csv')

###################################################################
#Merge Shot Stats with main
#table6, six10, tenTo15, table8
###################################################################

new4Table = newNewNewTable.merge(table6, how='left', on='PLAYER')
new5Table = new4Table.merge(six10, how='left', on='PLAYER')
new6Table = new5Table.merge(tenTo15, how='left', on='PLAYER')
new7Table = new6Table.merge(table8, how='left', on='PLAYER')

new7Table.drop(['Unnamed: 0_x','Unnamed: 0_y','TEAM','AGE','SCREEN_AST','Unnamed: 0_x','Unnamed: 0_y','Unnamed: 0_x','Unnamed: 0_y'], axis=1, inplace=True)

cols = list(new7Table.columns.values)
print(cols)

new7Table = new7Table[
        [
        'PLAYER', 'GP', 'MIN', 'DREB%', '%DREB', 'STL%', '%BLK', 'DEFL', 'LB_REC', 'CHARGES_DRAWN', 'CONT_2PT', 'CONT_3PT', 'CONT_ALL', 'DIST_MI_DEF', 'AVG_SPEED_DEF', 'DREB', 'CONTEST_DREB%', 'DEFER_DREB_CHANCE', 'AVG_DREB_DIST', '6FREQ', '6DFGM', '6DFGA', '6DFG%', '6to10FREQ', '6to10DFGM', '6to10DFGA', '6to10DFG%', '10to15FREQ', '10to15DFGM', '10to15DFGA', '10to15DFG%', '15FREQ', '15DFGM', '15DFGA', '15DFG%']
        ]


new7Table.to_csv('craziesterShit.csv')
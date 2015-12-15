# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 10:55:20 2015

@author: Kem
"""

import pandas as pd
import numpy as np
import re
from tabulate import tabulate

df = pd.read_csv('ool_pds.csv', low_memory = False) #loading data into dataframe

print (len(df)) #number of rows
print(len(df.columns)) #number of columns 

#Did you vote the last election?
#1-Yes, 2-No , -1-No answer
#c_voted = df.groupby('W1_A4').size()
c_voted = df['W1_A4'].value_counts(sort = True,dropna=False)
p_voted = df['W1_A4'].value_counts(sort = True, normalize = True,dropna=False)
print('Did you vote the last election?')
#print (c_voted, p_voted)

#frequency table
c_voted = str(c_voted)
p_voted = str(p_voted)
#print (c_class)
l = re.findall('^([0-9]?)', c_voted)
m = re.findall('\n([0-9]?)', c_voted)
m2 = l + m
n = re.findall('\s+([0-9][0-9]*)\n', c_voted)
o = re.findall('\s+([0-9].[0-9]*)\n', p_voted)
#t2 = ['Thoughts ', 'Counts', 'Percents']
#print (l, m, m2, n, o)

print (tabulate({"Thoughts": m2,
                "Counts":  n,
                "Percents": o}, headers="keys"))

#How much do you affect what the government does?
#1-A great deal, 2-A lot, 3-Moderately, 4-A little, 5-Not at all, -1-No answer
c_affect = df['W1_B2'].value_counts(sort = True,dropna=False) #how much do people affect gov
p_affect = df['W1_B2'].value_counts(sort = True, normalize = True,
dropna=False) 
print ('\nHow much do you affect what the government does?\n')
#print (c_affect, p_affect)


#frequency table
c_affect = str(c_affect)
p_affect = str(p_affect)
#print (c_class)
l = re.findall('^([0-9]?)', c_affect)
m = re.findall('\n([0-9]?)', c_affect)
m2 = l + m
n = re.findall('\s+([0-9][0-9]*)\n', c_affect)
o = re.findall('\s+([0-9].[0-9]*)\n', p_affect)
#t2 = ['Thoughts ', 'Counts', 'Percents']
#print (l, m, m2, n, o)

print (tabulate({"Thoughts": m2,
                "Counts":  n,
                "Percents": o}, headers="keys"))
                
#How often does the government do what Americans want?
#1-Always, 2-Most of the time, 3-half the time, 4-Once in a while, 5-Never, -1-No answer
c_awant = df['W1_B3'].value_counts(sort = True,dropna=False) #fed do what Americans want
p_awant = df['W1_B3'].value_counts(sort = True, normalize = True,dropna=False)
print ('\nHow often does the government do what Americans want?\n')
#print (c_awant, p_awant)

#frequency table
c_awant = str(c_awant)
p_awant = str(p_awant)
#print (c_class)
l = re.findall('^([0-9]?)', c_awant)
m = re.findall('\n([0-9]?)', c_awant)
m2 = l + m
n = re.findall('\s+([0-9][0-9]*)\n', c_awant)
o = re.findall('\s+([0-9].[0-9]*)\n', p_awant)
#t2 = ['Thoughts ', 'Counts', 'Percents']
#print (l, m, m2, n, o)

print (tabulate({"Thoughts": m2,
                "Counts":  n,
                "Percents": o}, headers="keys"))

#How well does Congress represent all Americans?
#1-Extremely well, 2-Very well, 3-Moderately, 4-A little, 5-Not well, -1-No answer
c_repream = df['W1_G2'].value_counts(sort = True,dropna=False) #Congress represent all Americans
p_repream = df['W1_G2'].value_counts(sort = True, 
normalize = True,dropna=False) 
print ('\nHow well does Congress represent all Americans?\n')
#print (c_repream, p_repream)
#frequency table
c_repream = str(c_repream)
p_repream = str(p_repream)
#print (c_class)
l = re.findall('^([0-9]?)', c_repream)
m = re.findall('\n([0-9]?)', c_repream)
m2 = l + m
n = re.findall('\s+([0-9][0-9]*)\n', c_repream)
o = re.findall('\s+([0-9].[0-9]*)\n', p_repream)
#t2 = ['Thoughts ', 'Counts', 'Percents']
#print (l, m, m2, n, o)

print (tabulate({"Thoughts": m2,
                "Counts":  n,
                "Percents": o}, headers="keys"))  

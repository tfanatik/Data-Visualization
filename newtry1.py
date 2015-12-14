# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 10:55:20 2015

@author: Kem
"""

import pandas as pd
import numpy as np

df = pd.read_csv('ool_pds.csv', low_memory = False) #loading data into dataframe

print (len(df)) #number of rows
print(len(df.columns)) #number of columns 

#Did you vote the last election?
#1-Yes, 2-No , -1-No answer
#c_voted = df.groupby('W1_A4').size()
c_voted = df['W1_A4'].value_counts(sort = True,dropna=False)
p_voted = df['W1_A4'].value_counts(sort = True, normalize = True,dropna=False)
print('Did you vote the last election?')
print (c_voted, p_voted)

#How much do you affect what the government does?
#1-A great deal, 2-A lot, 3-Moderately, 4-A little, 5-Not at all, -1-No answer
c_affect = df['W1_B2'].value_counts(sort = True,dropna=False) #how much do people affect gov
p_affect = df['W1_B2'].value_counts(sort = True, normalize = True,
dropna=False) 
print ('How much do you affect what the government does?')
print (c_affect, p_affect)

#How often does the government do what Americans want?
#1-Always, 2-Most of the time, 3-half the time, 4-Once in a while, 5-Never, -1-No answer
c_awant = df['W1_B3'].value_counts(sort = True,dropna=False) #fed do what Americans want
p_awant = df['W1_B3'].value_counts(sort = True, normalize = True,dropna=False)
print ('How often does the government do what Americans want?')
print (c_awant, p_awant)

#How well does Congress represent all Americans?
#1-Extremely well, 2-Very well, 3-Moderately, 4-A little, 5-Not well, -1-No answer
c_repream = df['W1_G2'].value_counts(sort = True,dropna=False) #Congress represent all Americans
p_repream = df['W1_G2'].value_counts(sort = True, 
normalize = True,dropna=False) 
print ('How well does Congress represent all Americans?')
print (c_repream, p_repream)







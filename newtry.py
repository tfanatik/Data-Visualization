# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 10:55:20 2015

@author: Kem
"""

import pandas as pd
import numpy as np

df = pd.read_csv('ool_pds.csv', low_memory = False)


data = df[['W1_A4', 'W1_B2', 'W1_B3', 'W1_F1', 'W1_I1', 'W1_I2', 'W1_P2', 
'W1_P13', 'W1_P13A', 'W1_P13B', 'PPAGECAT', 'PPEDUCAT', 
'PPSTATEN']]
old_names = ['W1_A4', 'W1_B2', 'W1_B3', 'W1_F1', 'W1_I1', 'W1_I2', 'W1_P2', 
'W1_P13', 'W1_P13A', 'W1_P13B', 'PPAGECAT', 'PPEDUCAT', 
'PPSTATEN'] 
new_names1 = ['People', 'People', 'Optimistic/', 'Congress', 'Represent',
'Social', ' ', 'US', 'US Citizen', ' ', ' ', ' ']
new_names2 = ['Voted', 'PAffect', 'AWant', 'Opt-Pestimist', 'Represent Am', 
'RepresentU', 'Class', 'Citizen','USBorn', 'When', 'Age', 'Education', 'State']

data.rename(columns=dict(zip(old_names, new_names2)), inplace=True)
print(type(data))

states = [21, 23, 31, 33, 58, 59,74, 84, 93] #a number of large states that affect elections
ages = [1, 2, 3, 4,  5] #older than age 64 has been left off
educ = [3, 4] #only picked at least a BA degree 
cit = [1, 2, 3, 4, 5] #became US citizen 1961-1999 for 'experience time'


age_tst = data[data['Age'].isin(ages)]
educ_tst = age_tst[age_tst['Education'].isin(educ)]
test1 = educ_tst.sort('State', ascending=True)
st_test = test1[test1['State'].isin(states)]
st_tst = st_test.copy()
print ('rows: ', len(st_tst)) #number of rows
print ('columns: ', len(st_tst.columns)) #number of columns
#print(type(st_tst))


#setting variables to numeric
st_tst['Voted'] = st_tst['Voted'].convert_objects(convert_numeric=True)
st_tst['PAffect'] = st_tst['PAffect'].convert_objects(convert_numeric=True)
st_tst['AWant'] = st_tst['AWant'].convert_objects(convert_numeric=True)
st_tst['Opt-Pestimist'] = st_tst['Opt-Pestimist'].convert_objects(convert_numeric=True)
st_tst['Represent Am'] = st_tst['Represent Am'].convert_objects(convert_numeric=True)
st_tst['Class'] = st_tst['Class'].convert_objects(convert_numeric=True)
print(type(st_tst))
#c_vtd = st_tst['Voted'] = st_tst['Voted'].replace(-1, numpy.nan)
#p_vtd = st_tst['Voted'] = st_tst['Voted'].replace (-1, numpy.nan)

#Did you vote the last election?
#1-Yes, 2-No , -1-No answer
c_vt = st_tst['Voted'] = st_tst['Voted'].replace(-1, np.NaN)
#print (type(c_vt))
c_vtd = pd.DataFrame(c_vt)
#print (type(c_vtd))
c_aft = st_tst['PAffect'] = st_tst['PAffect'].replace(-1, np.NaN)
c_afct = pd.DataFrame(c_aft)
c_wan = st_tst['AWant'] = st_tst['AWant'].replace(-1, np.NaN)
c_wnt = pd.DataFrame(c_wan)
c_pess = st_tst['Opt-Pestimist'] = st_tst['Opt-Pestimist'].replace(-1, np.NaN)
c_opss = pd.DataFrame(c_pess)
c_rep = st_tst['Represent Am'] = st_tst['Represent Am'].replace(-1, np.NaN)
c_rept = pd.DataFrame(c_rep)
c_cl = st_tst['Class'] = st_tst['Class'].replace(-1, np.NaN)
c_cls = pd.DataFrame(c_cl)



c_voted = c_vtd['Voted'].value_counts(sort = False,dropna=True) 
print (c_voted)
p_vtd = st_tst['Voted'] = st_tst['Voted'].replace (-1, np.nan)
p_voted = c_vtd['Voted'].value_counts(sort = False, normalize = True,dropna=True) 
#p_voted = p_vtd['Voted'] = p_vtd['Voted'].replace (-1, numpy.nan)
print('Did you vote the last election?')
print (c_voted, p_voted)

#How much do you affect what the government does?
#1-A great deal, 2-A lot, 3-Moderately, 4-A little, 5-Not at all, -1-No answer
c_affect = c_afct['PAffect'].value_counts(sort = False,dropna=True) #how much do people affect gov
p_affect = c_afct['PAffect'].value_counts(sort = False, normalize = True,
dropna=True) 
print ('How much do you affect what the government does?')
print (c_affect, p_affect)

#How often does the government do what Americans want?
#1-Always, 2-Most of the time, 3-half the time, 4-Once in a while, 5-Never, -1-No answer
c_awant = c_wnt['AWant'].value_counts(sort = False,dropna=True) #fed do what Americans want
p_awant = c_wnt['AWant'].value_counts(sort = False, normalize = True,dropna=True)
print ('How often does the government do what Americans want?')
print (c_awant, p_awant)

#Are you optimistic, pestimistic, or neither about your future?
#1-Optimistic, 2-Pessimistic, 3-Neither
c_opt = c_opss['Opt-Pestimist'].value_counts(sort = False,dropna=True) 
p_opt = c_opss['Opt-Pestimist'].value_counts(sort = False, 
normalize = True,dropna=True) 
print('Are you optimistic, pestimistic, or neither about your future?')
print (c_opt, p_opt)

#How well does Congress represent all Americans?
#1-Extremely well, 2-Very well, 3-Moderately, 4-A little, 5-Not well, -1-No answer
c_repream = st_tst['Represent Am'].value_counts(sort = False,dropna=True) #Congress represent all Americans
p_repream = st_tst['Represent Am'].value_counts(sort = False, 
normalize = True,dropna=True) 
print ('How well does Congress represent all Americans?')
print (c_repream, p_repream)

#Which class do you belong to?
#1-Poor, 2-Working, 3-Middle, 4-Upper Middle, 5-Upper
c_class = c_cls['Class'].value_counts(sort = False,dropna=True) #respondents social class
p_class = c_cls['Class'].value_counts(sort = False, normalize = True,
dropna=True)
print ('Which class do you belong to?')
print (c_class, p_class)




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 19:42:13 2024

@author: magironza
"""

import pandas as pd

data_file_folder =  '/Users/stephaniecardona/Documents/ALEJANDRO/python'

df = pd.read_excel('master_file_to_clean.xlsx')

df.drop_duplicates(inplace= True)

print(len(df))

df.columns = ['UNSPSC', 
              'Description',
              'ExpectedStartDate',
              'ExpectedDueDateReplies',
              'ExpectedDurationTime',
              'ExpectedDurationInterval',
              'Type',
              'BudgetOrigin',
              'ExpectedTotalValue',
              'ExpecteValueInActualBudget',
              'FutureBudgetRequiered',
              'FutureBudgetState',
              'BOReference',
              'Location',
              'ResponsableName',
              'ResponsablePhone',
              'ResponsableEmail',
              'Will_the_tender_be_associated_to_SMEs',
              'Will_the_lots_be_associated_to_SMEs',
              'Does_it_comply_with_the_minimum_30',
              'Goods'
                     
              ]	



df.drop(index=0, axis=0, inplace=True)


df.drop(columns = ['UNSPSC',
                   'Will_the_tender_be_associated_to_SMEs',
                   'Will_the_lots_be_associated_to_SMEs',
                   'Does_it_comply_with_the_minimum_30',
                   'Goods'], inplace= True)

print(df.columns)

print('-------')

print(df.head(20))

df['Description'].str.capitalize()

df.to_excel('cleaned_data.xlsx', index=False)




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 10:12:21 2024

@author: magironza
"""

import os 
import pandas as pd

data_file_folder =  '/Users/stephaniecardona/Documents/ALEJANDRO/RawData'

df = []

for file in os.listdir(data_file_folder):

    if file.endswith('.xlsx'):
        print('Loading file {0}...'.format(file))
        df.append(pd.read_excel(os.path.join(data_file_folder, file)))
        
print(len(df))

df_master = pd.concat(df, axis=0)
df_master.to_excel('master_file_to_clean.xlsx', index=False)
#!/usr/bin/python

import sys
import csv
import numpy as np
import pandas as pd

# test mode looks at default files
test_mode = False
if (len(sys.argv) < 2): test_mode = True
if test_mode:
    file_1 = open('test_files/test_1.csv', 'r')
    file_2 = open('test_files/test_2.csv', 'r')
else:
    file_1 = open(sys.argv[1], 'r')
    file_2 = open(sys.argv[2], 'r')

# build a dataframe for each file
df1 = pd.read_csv(file_1)
df2 = pd.read_csv(file_2)
print('\n1: {0}\n2: {1}'.format(file_1.name, file_2.name))

mutual_cols = [c for c in df1.columns.values 
               if c in df2.columns.values]

print('...comparing the following mutual variables:\n', mutual_cols)
df1, df2 = df1[mutual_cols], df2[mutual_cols]

intersection = pd.merge(df1, df2)
union = pd.concat([df1, df2], ignore_index=False).drop_duplicates()

df_all = df1.merge(df2, on=mutual_cols, how='left', indicator=True)
df1_only = df1[df_all['_merge'] == 'left_only']

df_all = df2.merge(df1, on=mutual_cols, how='left', indicator=True)
df2_only = df2[df_all['_merge'] == 'left_only']


print('... N(1) = {0}'.format(df1.shape[0]))
print('... N(2) = {0}'.format(df2.shape[0]))
print('... N(intersection) = ', intersection.shape[0])
print('... N(union) = ', union.shape[0])
print('... N(1_only) = {0}'.format(df1_only.shape[0]))
print('... N(2_only) = {0}'.format(df2_only.shape[0]))


if not test_mode:
    df1_only.to_csv('output_files/'+file_1.name.split('/')[-1])
    df2_only.to_csv('output_files/'+file_2.name.split('/')[-1])

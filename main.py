import pandas as pd
import numpy as np

data1 = {'Колонка1': np.random.randint(1, 100, 10)}
data2 = {'Колонка1': np.random.randint(1, 100, 10)}
data3 = {'Колонка1': np.random.randint(1, 100, 10)}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

df1.to_excel('file1.xlsx', index=False)
df2.to_excel('file2.xlsx', index=False)
df3.to_excel('file3.xlsx', index=False)


df1 = pd.read_excel('file1.xlsx')
df2 = pd.read_excel('file2.xlsx')
df3 = pd.read_excel('file3.xlsx')


all_data = pd.concat([df1, df2, df3], ignore_index=True)

sorted_data = all_data.sort_values(by='Колонка1', ascending=False)

sorted_data.to_excel('sorted_data.xlsx', index=False)
import pandas as pd

#10G线路板 1口-8口

data1=pd.read_excel('10G-line-standard.xlsx',header=None)
data1.fillna(method='pad')
data1.head()
print(data1)
import mytree as mt
import pandas as pd
import string
from tools import parsenode

xl=pd.ExcelFile('line.xlsx',header=None)
xl.parse()
trees={}
for i in xl.sheet_names:
    # print(i)
    data=xl.parse(i,header=None).fillna(method='ffill')
    # print(data)
    root=mt.TreeNode(i)
    for row in data.iterrows():
        root.find_child(' '.join('%s' %id for id in row[1]),create=True)
    root.dump()
    trees[i]=root

print(trees.keys())
xlink=pd.ExcelFile('link.xlsx',header=0)
xlink.parse()


links = xlink.parse(xlink.sheet_names[0],header=0)
print(links.groupby(['源网元']))

source='关中环四'
des='关中环四'
df=links[links['源网元'].str.contains(source) & links['宿网元'].str.contains(des)]

print(df)
print(df.iloc[0])
for i in range(0,len(df)):
    # df.iloc[0]
    pass
#搜索M40,D40对应对端的M40,D40   区分奇数波\偶数波


source='1120-关中环四锦业路-子架0-34-58NS4-1(IN/OUT)'



def searchLine(str):
    pass

# print(links1.astype)

# data1=pd.read_excel('线路交叉.xlsx',header=None)
# data1.fillna(method='pad')
# data1.head()
# print(data1)
# for i in data1.

# root = mt.TreeNode('71(ODU2LP1/ODU2LP1)-1') # root name is ''
# root.find_child('')
# a1 = root.add_child('51(ODU1LP1/ODU1LP1)-1')
# a1.add_child('161(ODU0LP1/ODU0LP1)-1')
# a1.add_child('161(ODU0LP1/ODU0LP1)-2')
#
# a2 = root.add_child('51(ODU1LP1/ODU1LP1)-2')
# a2.add_child('162(ODU0LP1/ODU0LP1)-1')
# a2.add_child('162(ODU0LP1/ODU0LP1)-2')
#
# a3 = root.add_child('51(ODU1LP1/ODU1LP1)-3')
# a3.add_child('163(ODU0LP1/ODU0LP1)-1')
# a3.add_child('163(ODU0LP1/ODU0LP1)-2')
#
# a4 = root.add_child('51(ODU1LP1/ODU1LP1)-4')
# a4.add_child('164(ODU0LP1/ODU0LP1)-1')
# a4.add_child('164(ODU0LP1/ODU0LP1)-2')
# root.dump()


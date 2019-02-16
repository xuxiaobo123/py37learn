import pandas as pd

lemon=pd.read_excel('python1116.xlsx',sheet_name='login')#
# print(df.values)
# print(lemon['data'])

#print(lemon.ix[1,3])
#print(lemon.loc[[1,3]])#读取指定的行

# print(lemon.ix[1,['title','data']].values)#列表
# print(lemon.ix[:,['title','data']].values)#列表  获取所有的数据
test_data=[]
for i in lemon.index.values:
    row_data=lemon.loc[i,['title','data']].to_dict()
    test_data.append(row_data)
print("最后获取到的数据",test_data)
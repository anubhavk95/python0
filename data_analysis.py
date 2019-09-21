import pandas as pd

ak_web1 = {'day':[1,2,3,4,5,6], 'visitor':[90,80,70,60,50,40], 'Bounce':[10,20,30,40,50,60]}
#ak_web2 = {'day':[1,2,3,4,5,6], 'visitor':[9,8,7,6,5,4], 'Bounce':[100,200,300,400,500,600]}


df1 = pd.DataFrame(ak_web1, index = [1,2,3,4,5,6])
df2 = pd.DataFrame(ak_web2, index = [1,2,3,4,5,7])
merge = pd.merge(df1, df2)
print(merge)
print(df1)
print(df2)

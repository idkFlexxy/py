import pandas as pd
df1=pd.DataFrame({'name':['aa','bb','cc'],'age':[20,19,18],'grade':['A','B','C']},index=[1,2,3])
df2=pd.DataFrame({'name':['dd','ee','ff'],'age':[17,16,15],'grade':['a','b','c']},index=[4,5,6])
result=pd.concat([df1,df2])
print(result)

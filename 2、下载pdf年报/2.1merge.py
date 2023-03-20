import pandas as pd

pd.options.display.max_colwidth= 300
pd.options.display.max_columns = 300
#df1=pd.read_excel('aim_data.xlsx',dtype={'code':str})
df2=pd.read_excel('all_url_data.xlsx',dtype={'code':str})

df3=pd.merge(df2,on=['code','year'],how='left')

df4=df3.loc[:,['code','firm','year','pdf_url']]
df4.to_excel('merged_data.xlsx',index=False)

print(df4)



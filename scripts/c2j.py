import pandas as pd
import json

df = pd.read_csv('./lecture_list.csv',encoding='utf-8',index_col=0)
df.to_json('../src/mixins/classWeekInfo.js', force_ascii=False,orient='index')
print(df['weektime'])
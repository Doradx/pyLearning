from bs4 import BeautifulSoup
import pandas as pd
print('Reading Started')
html_id=2
html=BeautifulSoup(open('Ma-%s-statistics.html'%html_id,'r').read())
tables=html.find_all('table',class_='Data')
print('Reading Finished')
SHEETS=[]
for i in range(8):
    SHEETS.append(pd.DataFrame())
for i,table in enumerate(tables):
    df = pd.read_html(str(table))[0]
    if i/8<1:
        SHEETS[i%8]=df
    else:
        SHEETS[i%8]=SHEETS[i%8].append(df)
    print('Handling %s/%s'%(i,len(tables)))

writer = pd.ExcelWriter('output-%s.xlsx'%html_id)
for i in range(8):
    SHEETS[i%8].to_excel(writer,'Sheet%s'%i,index=False)
    print('Saving %s/%s'%(i,8))
writer.save()
print('Finished')
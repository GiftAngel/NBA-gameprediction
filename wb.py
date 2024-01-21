from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')

big_comp = soup.find_all('table')[1]
bg_co = big_comp.find_all('th')
biggest_com = [title.text.strip() for title in bg_co]
df = pd.DataFrame(columns=biggest_com)
print(df)

row = big_comp.find_all('tr')

for rows in row[1:]:
 rowed=rows.find_all('td')
 biggest_rowed = [data.text.strip() for data in rowed]
 lenght=len(df)
 df.loc[lenght] = biggest_rowed
print(df)
df.to_csv(r'c:\Users\-GIFT IKECHUKWU-\Desktop\DATA\webscrapped Data.csv',index=False)




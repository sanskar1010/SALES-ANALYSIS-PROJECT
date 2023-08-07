import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# dir=r'C:\Users\DELL\Downloads\SalesData (1)\SalesData'
# list=os.listdir(dir)
# df=pd.DataFrame()
# for i in list:
#     data=pd.read_csv(fr'C:\Users\DELL\Downloads\SalesData (1)\SalesData\{i}')
#     df=pd.concat([df,data])

# df.to_csv(r'C:\Users\DELL\Desktop\sales_data.csv',index=False)

# Task1--what was the best month for sales?how much was earned that month?

df=pd.read_csv('sales_data.csv')
df=df.dropna().reset_index(drop=True)
df=df.loc[df['Order Date']!='Order Date']
df['Order Date']=pd.to_datetime(df['Order Date'])
df['month']=df['Order Date'].dt.month_name()
df[['Quantity Ordered','Price Each']]=df[['Quantity Ordered','Price Each']].apply(pd.to_numeric)
df['tsv']=df['Quantity Ordered']*df['Price Each']
month_grouped=df.groupby('month')['tsv'].sum().reset_index()
a=month_grouped['tsv'].argmax()
best_month_for_sales=month_grouped['month'][a]
best_month_sale_earning=month_grouped['tsv'][a]

# print(best_month_for_sales,best_month_sale_earning)
# plt.bar(month_grouped['month'],month_grouped['tsv'])
# plt.title('sales per month')
# plt.xlabel('month')
# plt.ylabel('total sales')
# plt.show()

# Task2--What city sold the most product?

df['city']=df['Purchase Address'].str.split(',',expand=True)[1]
grouped_city=df.groupby('city')['tsv'].sum().reset_index()
a=grouped_city['tsv'].argmax()
best_city_sale=grouped_city['city'][a]

# print(best_city_sale)
# plt.bar(grouped_city['city'],grouped_city['tsv'])
# plt.xlabel('city')
# plt.ylabel('tsv')
# plt.title('sales according to city')
# plt.show()

# Task3--What time should be display advertisments to maximise the livelihood of custommer's buying product?

df['hour']=df['Order Date'].dt.hour
grouped_time=df.groupby('hour')['Quantity Ordered'].sum().reset_index()
grouped_time=grouped_time.sort_values('Quantity Ordered').reset_index(drop=True)
a=grouped_time['Quantity Ordered'].argmax()
time_for_advertisment=grouped_time['hour'][a]

# plt.plot(grouped_time['hour'],grouped_time['Quantity Ordered'])
# plt.xlabel('time(in hours)')
# plt.ylabel('Quantity')
# plt.show()


# Task4- What product sold the most?Why do you think it sold the most?

grouped_product=df.groupby('Product')['Quantity Ordered'].sum().reset_index()
a=grouped_product['Quantity Ordered'].argmax()
most_sold_product=grouped_product['Product'][a]
# print(most_sold_product)

# plt.bar(grouped_product['Product'],grouped_product['Quantity Ordered'])
# plt.title('Product acc to Quantity')
# plt.xlabel('product')
# plt.ylabel('Quantity')
# plt.xticks(rotation=90)
# plt.show()

# Task5--what products are most often sold together?

df['grouped_products']=df.groupby('Order ID')['Product'].transform(lambda x : ','.join(x))
from itertools import combinations
from collections import Counter
count=Counter()
for i in df['grouped_products']:
    l=i.split(',')
    count.update(Counter(combinations(l,2)))
print(count.most_common(10))

#*************************** THE END ********************************************************





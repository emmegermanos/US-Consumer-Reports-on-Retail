#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv

#open file
with open ('2016-2020.csv') as csv_file:

#read csv file
    csv_reader= csv.reader(csv_file, delimiter=',')

#loop through data
    for row in csv_reader:
        print(row)


# In[1]:


#The average of one type of business across all years in the database

#import necessary libraries
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

#Python installation script to read my SQL work bench
cnx = mysql.connector.connect(user='root',
                           password='Breckco21',
                           host='127.0.0.1',
                           database='usretail',
                           auth_plugin='mysql_native_password')
cursor=cnx.cursor()

Months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

#Call out a user input for NAICS code to display
code=input('What Kind of Business(insert NAICS code)? ')

query= (f'''SELECT AVG(Sales), Month 
FROM mrtsdata 
WHERE code={code} 
GROUP BY Month''')

cursor.execute(query)

month=[]
sales=[]

#print all the rows
for row in cursor.fetchall():
        sales.append(row[0])
        month.append(row[1])

KB=cursor.execute(f"SELECT KB FROM mrtsdata WHERE code={code};")

for KB in cursor.fetchall():
    KB=KB[0]

plt.plot(month,sales)
plt.title(f'Average Sales by Month for {KB} 2016-2020')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(np.arange(1,13,1),labels=Months)
plt.show


# In[ ]:


code=input('What Kind of Business(insert NAICS code)? ')
year=input('What year do you want analyze?(2016-2020) ')

query=(f'''
SELECT Sales , Month, Year, KB
FROM mrtsdata
WHERE code={code} AND Year={year}
''')

cursor.execute(query)

month=[]
sales=[]

#print all the rows
for row in cursor.fetchall():
        sales.append(row[0])
        month.append(row[1])

plt.plot(month,sales)
plt.title(f'Sales in {row[2]} for {row[3]}')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(np.arange(1,13,1),labels=Months)
plt.show


# In[ ]:


code_1=input('First Business to compare(insert NAICS code)? ')
code_2=input('Next business(insert NAICS code)? ')

query1=(f'''
SELECT AVG(Sales), Month 
FROM mrtsdata 
WHERE code={code_1} 
GROUP BY Month''')

cursor.execute(query1)

month1=[]
sales1=[]

#print all the rows
for row in cursor.fetchall():
        sales1.append(row[0])
        month1.append(row[1])

query2=(f'''
SELECT AVG(Sales), Month
FROM mrtsdata
WHERE code={code_2}
GROUP BY Month
''')

cursor.execute(query2)

month2=[]
sales2=[]

#print all the rows
for row in cursor.fetchall():
        sales2.append(row[0])
        month2.append(row[1])
        
KB1=cursor.execute(f"SELECT KB FROM mrtsdata WHERE code={code_1};")

for KB1 in cursor.fetchall():
    KB1=KB1[0]
    
KB2=cursor.execute(f"SELECT KB FROM mrtsdata WHERE code={code_2};")

for KB2 in cursor.fetchall():
    KB2=KB2[0]

line1, =plt.plot(month1,sales1)
line2, =plt.plot(month2,sales2)
plt.title(f'Average Sales by Month \n {KB1} vs. \n {KB2} 2016-2020', fontsize=10)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(np.arange(1,13,1),labels=Months)
plt.legend([line1, line2], [f'{KB1}', f'{KB2}'])
plt.show


# In[ ]:


#Compare as many business as desired based on average of all years in database
while True:
    code=input('Business to compare(insert NAICS code)? (press q to quit)')
    
    if code == 'q':
        break
    else:
        query=(f'''
        SELECT AVG(Sales), Month 
        FROM mrtsdata 
        WHERE code={code} 
        GROUP BY Month''')

        cursor.execute(query)

        month=[]
        sales=[]

        #print all the rows
        for row in cursor.fetchall():
                sales.append(row[0])
                month.append(row[1])
        KB=cursor.execute(f"SELECT KB FROM mrtsdata WHERE code={code};")

        for KB in cursor.fetchall():
            KB=KB[0]

        plt.plot(month,sales, label=f'{KB}')
        plt.xlabel('Month')
        plt.ylabel('Sales')
        plt.xticks(np.arange(1,13,1),labels=Months)
        plt.title(f'Average Sales by Month for Select Businesses (2016-2020)' )
        plt.show
        plt.legend()


# In[ ]:


#Compare one business across multiple years based on user input
code=input('Business to compare(insert NAICS code)? ')

while True:
    year=input('First year to compare(2016-2020)? (press q to quit) ')
    
    if year == 'q':
        break
    else:

        query=(f'''
        SELECT Sales , Month, KB
        FROM mrtsdata
        WHERE code={code} AND Year={year}
        ''')

        cursor.execute(query)

        month=[]
        sales=[]

        #print all the rows
        for row in cursor.fetchall():
                sales.append(row[0])
                month.append(row[1])
    
        line =plt.plot(month,sales, label=f'{year}')
        plt.xlabel('Month')
        plt.ylabel('Sales')
        plt.xticks(np.arange(1,13,1),labels=Months)
        plt.legend()
        plt.title(f'Sales by Month for {KB}')
        plt.show


# In[ ]:


#Compare multiple business in one year based on user input
year=input('What year do you want to look at(2016-2020)? (press q to quit) ')

while True:
    code=input('Business to compare(insert NAICS code)?(press q to quit) ')
    
    if code == 'q':
        break
    else:

        query=(f'''
        SELECT Sales , Month, KB
        FROM mrtsdata
        WHERE code={code} AND Year={year}
        ''')

        cursor.execute(query)

        month=[]
        sales=[]

        #print all the rows
        for row in cursor.fetchall():
                sales.append(row[0])
                month.append(row[1])
        
        KB=cursor.execute(f"SELECT KB FROM mrtsdata WHERE code={code};")
        for KB in cursor.fetchall():
            KB=KB[0]

        line =plt.plot(month,sales, label=f'{KB}')
        plt.xlabel('Month')
        plt.ylabel('Sales')
        plt.xticks(np.arange(1,13,1),labels=Months)
        plt.legend()
        plt.title(f'Sales by Month for Select Businesses in {year}' )
        plt.show


# 

# In[ ]:


#Call out a user input for NAICS code to display
import pandas as pd
code_1=input('First Business to compare(insert NAICS code)? ')
code_2=input('Next business(insert NAICS code)? ')

query1=(f'''
SELECT AVG(Sales), Month 
FROM mrtsdata 
WHERE code={code_1} 
GROUP BY Month''')

cursor.execute(query1)

month1=[]
sales1=[]

#print all the rows
for row in cursor.fetchall():
        sales1.append(row[0])
        month1.append(row[1])
        
#calculate percent change
ssales1 = pd.DataFrame(sales1) 
pct_change1=ssales1.pct_change(fill_method='ffill')
pct_change1=pct_change1.fillna(0)
pct_change1=pct_change1*100
pct_change1=pct_change1[0].tolist()
pct_change1=[ '%.2f' % pct for pct in pct_change1]
pct_change1= [eval(pct) for pct in pct_change1]
colors=['grey' if pct >= 0 else 'r' for pct in pct_change1]

query2=(f'''
SELECT AVG(Sales), Month
FROM mrtsdata
WHERE code={code_2}
GROUP BY Month
''')

cursor.execute(query2)

month2=[]
sales2=[]

#print all the rows
for row in cursor.fetchall():
        sales2.append(row[0])
        month2.append(row[1])
        
#calculate percent change
ssales2 = pd.DataFrame(sales2) 
pct_change2=ssales2.pct_change(fill_method='ffill')
pct_change2=pct_change2.fillna(0)
pct_change2=pct_change2*100
pct_change2=pct_change2[0].tolist()
pct_change2=[ '%.2f' % pct for pct in pct_change2]
pct_change2= [eval(pct) for pct in pct_change2]
colors=['grey' if pct >= 0 else 'r' for pct in pct_change2]


KB1=cursor.execute(f"SELECT KB FROM mrtsdata WHERE code={code_1};")

for KB1 in cursor.fetchall():
    KB1=KB1[0]
    
KB2=cursor.execute(f"SELECT KB FROM mrtsdata WHERE code={code_2};")

for KB2 in cursor.fetchall():
    KB2=KB2[0]
        
X_axis = np.arange(len(Months)) 
  
plot1=plt.bar(X_axis - 0.2, sales1, 0.4, label = f'{KB1}', color='dodgerblue') 
plt.bar_label(plot1,labels= [f'+{pct}%' if pct>0 else f'-{pct}%' for pct in pct_change1],
              fontsize=8, rotation=90, padding=1) 

plot2=plt.bar(X_axis + 0.2, sales2, 0.4, label = f'{KB2}', color='hotpink',) 
plt.bar_label(plot2,labels= [f'+{pct}%' if pct>0 else f'-{pct}%' for pct in pct_change2], 
              fontsize=8, rotation=90, padding=1) 
plt.xticks(X_axis, Months)
plt.ylim([1, max(sales1)+10000])
plt.legend(loc='upper left')
plt.title(f'% Change in Sales by Month for Select Businesses(2016-2020)')


# In[ ]:


#Call out a user input for NAICS code to display
import pandas as pd
code_1=input('First Business to compare(insert NAICS code)? ')
code_2=input('Next business(insert NAICS code)? ')
year=input('What year do you want analyze?(2016-2020) ')

query1=(f'''
SELECT Sales, Month
FROM mrtsdata 
WHERE code={code_1} and Year={year}''')

cursor.execute(query1)

month1=[]
sales1=[]

#print all the rows
for row in cursor.fetchall():
        sales1.append(row[0])
        month1.append(row[1])
        
#calculate percent change
ssales1 = pd.DataFrame(sales1) 
pct_change1=ssales1.pct_change(fill_method='ffill')
pct_change1=pct_change1.fillna(0)
pct_change1=pct_change1*100
pct_change1=pct_change1[0].tolist()
pct_change1=[ '%.2f' % pct for pct in pct_change1]
pct_change1= [eval(pct) for pct in pct_change1]
colors=['grey' if pct >= 0 else 'r' for pct in pct_change1]

query2=(f'''
SELECT Sales, Month
FROM mrtsdata
WHERE code={code_2} and Year={year}
''')

cursor.execute(query2)

month2=[]
sales2=[]

#print all the rows
for row in cursor.fetchall():
        sales2.append(row[0])
        month2.append(row[1])
        
#calculate percent change
ssales2 = pd.DataFrame(sales2) 
pct_change2=ssales2.pct_change(fill_method='ffill')
pct_change2=pct_change2.fillna(0)
pct_change2=pct_change2*100
pct_change2=pct_change2[0].tolist()
pct_change2=[ '%.2f' % pct for pct in pct_change2]
pct_change2= [eval(pct) for pct in pct_change2]
colors=['grey' if pct >= 0 else 'r' for pct in pct_change2]


KB1=cursor.execute(f"SELECT KB FROM mrtsdata WHERE code={code_1};")

for KB1 in cursor.fetchall():
    KB1=KB1[0]
    
KB2=cursor.execute(f"SELECT KB FROM mrtsdata WHERE code={code_2};")

for KB2 in cursor.fetchall():
    KB2=KB2[0]
        
X_axis = np.arange(len(Months)) 
  
plot1=plt.bar(X_axis - 0.2, sales1, 0.4, label = f'{KB1}', color='dodgerblue') 
plt.bar_label(plot1,labels= [f'+{pct}%' if pct>0 else f'-{pct}%' for pct in pct_change1],
              fontsize=8, rotation=90, padding=1) 

plot2=plt.bar(X_axis + 0.2, sales2, 0.4, label = f'{KB2}', color='hotpink',) 
plt.bar_label(plot2,labels= [f'+{pct}%' if pct>0 else f'-{pct}%' for pct in pct_change2],
              fontsize=8, rotation=90, padding=1) 
plt.xticks(X_axis, Months)
plt.ylim([1, max(sales1)+10000])
plt.legend(loc='upper left')
plt.title(f'% Change in Sales by Month for Select Businesses for {year}')


# In[3]:


import pandas as pd
import csv

#open file
with open ('2016-2020.csv') as csv_file:

#read csv file
    csv_reader= csv.reader(csv_file, delimiter=',')


# In[4]:


#turn into dataframe
df = pd.read_csv("2016-2020.csv")
df['Day']=1
df['Date']=pd.to_datetime(df[['Year', 'Month', 'Day']])


# In[5]:


df=df.sort_values('Date')
print(df)


# In[69]:


#create data frame with NAICS code and sort it by date
df_shoes=df[df.Code=='4482']
df_shoes=df_shoes.sort_values('Date')

#find the rolling mean and median of the data frame
df_shoes['SalesRollingMedian']=df_shoes.rolling(window=3, on='Date').Sales.median()
df_shoes['SalesRollingMean']=df_shoes.rolling(window=3, on='Date').Sales.mean()

df_shoes.head()


# In[105]:


plt.plot(df_shoes['Date'],df_shoes['SalesRollingMedian'],color='deeppink',linewidth=3.0, label = 'Rolling Median')
plt.plot(df_shoes['Date'],df_shoes['SalesRollingMean'],color='deepskyblue',linewidth=3.0, label = 'Rolling Mean')

plt.scatter(df_shoes['Date'],df_shoes['Sales'],label = 'Sales',color='limegreen')

plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Shoe Sales vs. Rolling Median and Mean')
legend=plt.legend(fontsize=6,loc='upper right')
legend.get_frame().set_linewidth(1)
legend.get_frame().set_edgecolor('black')
plt.show


# In[73]:


#create data frame with NAICS code and sort it by date
df_liquor=df[df.Code=='4453']
df_liquor=df_liquor.sort_values('Date')

#find the rolling mean and median of the data frame
df_liquor['SalesRollingMedian']=df_liquor.rolling(window=6, on='Date').Sales.median()
df_liquor['SalesRollingMean']=df_liquor.rolling(window=6, on='Date').Sales.mean()

df_liquor.tail()


# In[109]:


plt.scatter(df_liquor['Date'],df_liquor['Sales'],label = 'Sales',color='limegreen')
plt.plot(df_liquor['Date'],df_liquor['SalesRollingMedian'],color='deeppink',linewidth=3.0, label = 'Rolling Median')
plt.plot(df_liquor['Date'],df_liquor['SalesRollingMean'],color='deepskyblue',linewidth=3.0, label = 'Rolling Mean')

plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Beer, Wine, and Liquor Sales vs. Rolling Median and Mean')
legend=plt.legend(fontsize=6,loc='upper left')
legend.get_frame().set_linewidth(1)
legend.get_frame().set_edgecolor('black')
plt.show


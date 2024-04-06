#!/usr/bin/env python
# coding: utf-8

# # Final Project

# # Exploring Sales Trends of MRST Data through ETL Process
# 
# **Emme Germanos**
# 

# # Index
# 
# - [Abstract](#Abstract)
# - [1. Introduction](#1.-Introduction)
# - [2. Extract-Transform-Load](#2.-Extract-Transform-Load)
#     - [2.1 The ETL Process](#2.1-The-ETL-Process)
#     - [2.2 Data Exploration](#2.2-Data-Exploration)
#     - [2.3 Data Preparation](#2.3-Data-Preparation)
#     - [2.4 Read the Data Using Python](#2.4-Reading-the-Data-Using-Python)
#          - [2.4.1 Reading Sample Data](#2.4.1-Reading-Sample-Data)
#          - [2.4.2 Reading the MRST Data](#2.4.2-Reading-the-MRST-Data)
#     - [2.5 Writing an Installation Script](#2.5-Writing-an-Installation-Script)
# - [3. Analysis and Visualization](#3.-Project-Description)
#     - [3.1 Running Queries in MySQL Workbech](#3.1-Running-Queries-in-MySQL-Workbech)
#     - [3.2 Running Queries From Python](#3.2-Running-Queries-From-Python)
#     - [3.3 Explore Trends](#3.3-Explore-Trends)
#     - [3.4 Explore Percentage Change](#3.4-Explore-Percentage-Change)
#     - [3.5 Explore Rolling Time Windows](#3.5-Explore-Rolling-Time-Windows)
# - [Conclusion](#Conclusion)
# - [References](#References)

# [Back to top](#Index)
# 
# 
# ##  Abstract
# 
# This model looks at various sales trends on data collected by Labor Bureau regarding monthly sales of several types of business. First, the raw data will be cleaned and transformed to be analyzed using the ETL process. Then the data will be imported in Python by both a CSV file as well as using MySQL. Finally, various queries will be performed on the data to analyze and visualize trends in sales for various businesses. Conclusions will then be drawn from this analysis'.

# [Back to top](#Index)
# 
# 
# ## 1. Introduction
# 
# Introduce your project using 300 words or less. Describe all the processes you followed to create your ETL, Analysis, and Visualization project. Start by summarizing the steps that you intend to perform and then elaborate on this section after you have completed your project.
# 
# >This project followed 3 main parts. First, I performed ETL on a raw data set. The data came from a census MRTS survey which is sent out to 13,000 business across the U.S. and collects sales information regarding their business. I cleaned and prepared this data data to be analyzed through the ETL process. Once cleaned, I then uploaded the data to SQL, which I connected with Python to analyze and visualize the data. I first checked the data to ensure it was properly imported through several different SQL queries. Then I created several different plots through Python functions and MatplotLib. The functions and plots I used to analyze this data are shown below.

# [Back to top](#Index)
# 
# ## 2. Extract-Transform-Load
# 
# 

# [Back to top](#Index)
# 
# ### 2.1 The ETL Process
# 
# Describe, using your own words, the key steps to perform ETL on the provided MRTS dataset.
# 
# >ETL stands for extract, load and transform. This is a process that takes raw data from a sources and cleans and organizes it to be combined into a data warehouse. For this particular project, the raw data was MRTS data. The data set we had included data from 1992 to 2021. For the extraction part of the ETL process, I chose what years I would use and placed them all in one sheet on excel. I chose 5 years of data for my data set. Since 2021 data set was not complete I chose to exclude it, and then I collected the data from 2020,2019,2018,2017, and 2016. Next for step 2 of the ETL process, I filtered the data. I did this through several steps which I get into more detail about below. Finally, Step 3 of the ETL process, once the data set was cleaned, I loaded in onto MySQl workbench to be analyzed. 

# [Back to top](#Index)
# 
# ### 2.2 Data Exploration
# 
# >MRTS stands for Monthly Retail Trade Survey and it is a survey sent out each year by the Census Bureau to collect data from companies across the US regarding their sales information. This data is grouped by month and kind of business. A business is classified based on by the type of it largest source of sales. For this project we had data from every month from 1992 to 2021 both adjusted and not adjusted.The adjusted data is adjusted by seasonal trends. Each year had data for each kind of business which was classified by a specific North American Indication Classification System code or a NAICS code. If a category did meet a specific standard of quality for data that is considered sufficient enough to be accurate it was marked by an *(s)*.

# [Back to top](#Index)
# 
# ### 2.3 Data Preparation
# 
# >For step 2 of the ETL process, I filtered the data. First, I removed all the adjusted data, since I chose to only explore the unadjusted data for the data set. I also removed the total columns, leaving only the columns for each month. Then I filled in every blank value or insufficient value with a zero. Next, I removed any type of data that was not indicated by a NAICS code, since I would use that as a primary key in my data set. Finally, I unstacked the data so that it appeared as it does below. The columns would include the NAICS code as Code, the kind of business as KB, the sales, the month labeled 1-12 and then finally the year.
# 
# ![alt text](plot11.png)
# 

# [Back to top](#Index)
# 
# ### 2.4 Read the Data Using Python
# 
# Python can be used to read CSV files. First you import CSV, which is used to read and write CSV files. Then, the code uses csv to call and import the needed file as a csv_file. The code then reads in the file and then calls out a delimiter to as a boundary to separate on, which in this case is a comma. Then using a loop, Python reads and prints out each row of the CSV file. 

# [Back to top](#Index)
# 
# ### 2.4.1 Reading Sample Data
# 
# |<img src="plot10.png" width="3400">|First, I converted the MRTS excel file to a comma separted value file. Then using the Python script below, I uploaded, read and printed out the data. As mentioned above, this code calls and imports the file, then uses a loop and the delimiter of a comma to read and print out the data.|
# |:-|:-|

# [Back to top](#Index)
# 
# ### 2.4.2 Reading the MRTS Data
# 
# |<img src="plot12.png" width="4000">|After reading the CSV file in, below shows how it Python print the data out. The first row shows a list all the columns in the table separated by commas. The columns are Code, KB, Sales, Month, and Year. Then each data row is printed as a list to follow in the same column order. So each row prints out as a list containing data for Code, KB, Sales, Month and Year, in that order separated by commas.|
# |:-|:-|

# [Back to top](#Index)
# 
# ### 2.5 Writing an Installation Script
# 
# 
# |<img src="plot9.png" width="4000">|First, I imported the connector to connect the MySQL server, as well as the necessary libraries I will use for my analysis, so matplotlib and numpy. Then, I added the installation script to connect to MySQL Workbench and then opened a cursor so that it can read the select statements that will be used to analyze the data.|
# |:-|:-|

# 
# [Back to top](#Index)
# 
# ## 3. Analysis and Visualization
# 
# For each of the sections below, make sure you include a description of the steps you followed. Whenever possible, include screenshots of your code or program windows to demonstrate your steps.
# 
# >I created 3 plots to visualize the data. At first when I created these plots, they were limited on how many years or Kinds of Businesses that you could compare. However, I then realized that with a While loop, I was able to compare as many years(within the data set) and as many Kinds of Business(again, within the data set) that I wanted to. 
# 
# Here, describe the differences, advantages, and disadvantages of running *queries* against your dataset using the MySQL Workbench or a Python environment.
# 
# >There are a lot of advantages to using MySQL for database management. Specifically, the organization of data and tables is much clearer and easier to be read then say a CSV file. Especially with a larger database that has maybe hundreds of tables and rows of data, MySQL is much clearer and user friendly than through another file. Using MySQL is also much more secure and also protects the integrity of data. This would be extremely important to companies with secure data as well as companies with limited access to databases. Addionally, beyond Python there are many other databases that can utilize MySQL databases. Finally, in terms of writing queries against the data set, MySQL is pretty user friendly and standard in how to access the database using Python. The main disadvantages to the program is that MySQL is not very efficient with large databases and not very proactive with devloping and debugging tools.
# 
# |<img src="plot8.png" width="5000">|The first query I created allows the user to select as many Kinds of Businesses at they would like and the plot displays the month by month averages of sales on the user selected Kinds of Businesses. Within the While loop the user can input as many NAICS code as they would like, until they select q. For each kind of business, the SELECT query takes the average of all the sales for the code groupped by month. Then inputs each average by month into a list that is then plotted on the graph. The code also uses a SELECT statement to call out the Kind of Business for each code inserted to be used for the legend. This repeats for each code.|
# |:-|:-|
# 
# |<img src="plot7.png" width="5000">|The next query is very similar to the first. However, first the user inputs a desired NAICS code for the corresponding Kind of Business that they want to look at. This is outside of the loop so it is constant for each loop. Then the user inputs as many years (within the database) as desired to be plotted on the graph. Same as before, the user enters q to quit. The SELECT statement selects all the data for that NAICS code based on the user inputted year and groups it by month. Then the query inputs each sale for that month and year into a list that is then plotted onto the graph. This repeats for each year entered by the user.
# |:-:|:-|
# 
# |<img src="plot6.png" width="4500">|The last query, again is similar to the first two. However, this time the year is constant for each loop and is therefore outside of the while loop. Then, the user can enter as many NAICS codes as desired until they enter q. The SELECT statement selects all the sales data for that NAICS code based on the user inputted year and groups it by month. Then the query inputs each sale for that month and year into a list that is then plotted onto the graph. The code also uses a SELECT statement to call out the Kind of Business for each code inserted to be used for the legend. This repeats for each year entered by the user.
# |:-:|:-|

# [Back to top](#Index)
# 
# ### 3.2 Running Queries From Python
# 
# Same as before, I used various *SELECT* statements to compare data. I used the same *SELECT* statement in Python as I would in the SQL workbench, then I would compare the results to ensure that they were the same. I used several different statements to display different NAICS values, years, month and columns in the table. 

# [Back to top](#Index)
# 
# ### 3.3 Explore Trends
# 
# Describe which *queries* you wrote the explore the differences in trends between various categories in your data.
# 
# In your submission make sure to answer the following:
# 
# - What is an economic trend and why is it considered an important measure to predict quantities, like spending patterns?
#     * An economic trend is the decrease/increase or general behavior of a business economy. It is important to look at these trends for many reasons such as to understand seasonal increases in sales or to plan for larger inventories during specific times. 
# - What is the trend of the retail and food services categories? Can this data be displayed clearly or do you need to adjust some parameters to reduce extraneous details and be able to visualize a clean trend?
#     * I chose to only look at data that contained NAICS numbers, as it was a primary key in my data set. So, multiple businesses within the overarching category of retail and food services can be looked at using my queries and plot that are displayd below. 
# - When comparing businesses like bookstores, sporting goods stores, and hobbies, toys, and games stores, what is the highest trend of all of these options? Which one grew faster? Which one is higher? Is there a seasonal pattern? Were there any changes in 2020? Which is better, monthly or yearly? 
#     * Based on the averages of the years in the database (2016-2020), the highest trending business during holiday season is hobby, toy and game stores. However, the more consistantly higher trend throughout the year regardless of season is Sporting goods stores. This is visualized in the first plot below as compared to the other other two businesses, Sporting goods stores has a flatter curve indicating that is more consistent than compared to the other two business which display sharp curves during the holiday season as well as back to school season. 
#     * Hobby, toy and game stores also appear to grow at the quickest and highst rate also indicated below in the first plot with the Hobby, toy and game stores having the sharpest curve.
#     * In 2020 it is seen that book stores had the sharpest curve and thus increase in sales, followed by Sporting goods stores, then hobby, toy and game stores. When comparing the averages plot of all the years and the plot for 2020, the sporting good stores and hobby, toy and game stores sales all seem to be a bit lower than usual, this could be because of COVID-19.
#     * Overall, I think that it is good to look at both monthly and annual trends. By looking at the sales by month graph for each kind of business, you can see how sales and trends have differed over there. Looking at the average of sales across many years can help to plan things like inventory and employee schedules based on multiple data sets.

# |<img src="plot1.png" width="5000">|The plot to the left shows the average montly sales of all the years that are included in the data set for each business. This plot compared three different kinds of businesses. However, with this query, you are able to visualize just one kind of business or every business within the database.
# |:-:|:-|
# 
# |<img src="plot2.png" width="5000">|The plot to the left selects a year within the database and then allows the user to input as many kinds of businesses as they would like to see that data for that year. For this plot the user selected the year 2020 and 3 kinds of businesses, Sporting goods, Hobby, toy and game stores, and Book stores.
# |:-:|:-|
# 
# |<img src="plot3.png" width="500">| <img src="plot13.png" width="500">| <img src="plot14.png" width="500">|
# |:-:|:-:|:-:|
# 
# |This query allows the user to select one kind of business and as many years as they would like to select to be displayed on the plot. For the 3 plots above, the user selected bookstore as the kind of business and selected to see the years 2016, 2017, 2018, 2019 and 2020. Then the user selected Hobby, toy and game stores, and then Sporting goods stores, again for the same years.|
# |:-|

# [Back to top](#Index)
# 
# ### 3.4 Explore Percentage Change
# 
# Describe which *queries* you wrote to explore the differences in trends between various categories in your data.
# 
# In your submission make sure to answer the following:
# 
# - In economics, what is the percentage change and why is it considered an important measure to predict quantities like spending patterns?
#     * Percent Change most simply shows the percent that data changes overtime. In economics there are many uses for percent change such as percent change in sale prices, stock values, purchase prices etc. It is important to measure quantities such as percent change to help futher illustrate trends and changes overtime and through seasons, just to name a few. 
# - Consider the women's clothing and men's clothing businesses and their percentage change. How are these two businesses related? For each of the two businesses, what is the percentage of contribution to the whole and how does it change over time?
#     * The two plots below illustrate percent changes by month for both women's and men's clothing businesses. The first plot shows the two kinds of business in the specific year of 2020, and the second plot shows the percent change in the averages of the sales for the years in the database.
#     * These two businesses are related in the fact that they are very similar markets and therfore should follow very similar trends. The plots below illustrate this observation, as it is seen the sharp increase in sales from August to December in comparison to January to July.
#     * Looking at the first plot, which displays data from a specific year. This plot could be beneficial in looking at trends that occurred for the year and potentially making conclusions for these trends. For example, a change in trends or maybe a decrease in sales could be explained by COVID-19.
#     * Looking at the second plot, this displays the average of the sales data for the years included in the database. This plot could be beneficial in visualizing consistent trends in the business and planning for inventory during times where there may be more or less sales on average.
# 
# ![Plot 15](plot15.png)|![Plot 16](plot16.png)
# |:-:|:-:|

# [Back to top](#Index)
# 
# ### 3.5 Explore Rolling Time Windows
# 
# 
# Describe which *queries* you wrote to explore the differences in trends between various categories in your data.
# 
# In your submission, make sure to answer the following:
# 
# - In economics, what is the rolling time window and why is it considered an important measure to predict quantities like spending patterns?
#     * In economics a rolling time window is a fixed time window for which a computation is performed. This is an important concept in economics in testing the stability of a model overtime and ot determine whether or not trends are time sensitive or a consistent trend over time. Specifically, calculating the rolling average and median is important process in smoothing data overtime and handling outliers in data. Both the rolling mean and median are used in similar ways on time series data, however the median seems to be less sensitive to outliers. However, they are both successful in predicting more accurate trends than data alone. 
# - Consider at least two businesses of your own from the MRTS data. Which *queries* did you write to analyze and produce graphs of rolling time windows for the chosen categories?
# 
#     * I chose to look at Beer, Wine and Liquor stores, as well as shoes stores. I did the same queries on both kind of businesses. For Shoe stores, I chose to look at the mean and median every 3 months. I plotted all the data on the graph. When comparing the mean line in blue to the median line in pink, they are very close, so it would be fair to use either for smoothing out the data and anticipating trends. For Beer, Wine and Liquor stores, I chose to take a rolling mean and median every 6 months. Since the data for this kind of business has such sharp uptrends and downtrends, the mean data seems to be at bit less acurrate. So for this query, I would use the rolling median to predict trends. 
# 
# ![Plot 15](plot17.png)|![Plot 16](plot18.png)
# |:-:|:-:|
# ![Plot 15](plot19.png)|![Plot 16](plot20.png)
# |:-:|:-:|
# 

# [Back to top](#Index)
# 
# ## Conclusion
# 
# Describe your conclusions. Which one of the businesses considered seems like it's going to attract the least spending? Which business seems likely to attract the most spending? 
# 
# Through all the queries ran in this model, various conclusions can be made about the data. When comparing Book stores, Hobby, game and toy stores, and Sporting goods stores, the differing seasonal trends can be seen. Additionally, we can conclude that Hobby game and toy stores attract the most spending while Sporting goods stores seem to attract the least amount of spending. When analyzing the Mens Clothing stores in comparison to Womens clothing stores, the sharp uptrend in sales for the months of August to December is displayed. Additionally when comparing the two types of businesses, it is seen that male clothing stores attract more spending than womens clothing stores. Finally, when looking at the Shoe sales data, either mean or median can be used to smooth the data, while when looking at Beer, Wine and Liquour stores, the median data seems to smooth the data more accurately. 

# 
# [Back to top](#Index
# )
# ## References
# 
# Use this format for websites:
# - GfG. “Create a Grouped Bar Plot in Matplotlib.” GeeksforGeeks, GeeksforGeeks, 17 Dec. 2020, www.geeksforgeeks.org/create-a-grouped-bar-plot-in-matplotlib/. 
# - GfG. “Create a Grouped Bar Plot in Matplotlib.” GeeksforGeeks, GeeksforGeeks, 17 Dec. 2020, www.geeksforgeeks.org/create-a-grouped-bar-plot-in-matplotlib/. 
# - “How to Parse Dates in Different Columns with Pandas’ Read_csv().” Saturn Cloud Blog, 14 Nov. 2023, saturncloud.io/blog/how-to-parse-dates-in-different-columns-with-pandas-readcsv/. 
# - “How to Split a Date Column into Separate Day Month Year Columns in Pandas.” Saturn Cloud Blog, 2 Nov. 2023, saturncloud.io/blog/how-to-split-a-date-column-into-separate-day-month-year-columns-in-pandas/. 
# - “Matplotlib.Pyplot.Bar_label#.” Matplotlib.Pyplot.Bar_label - Matplotlib 3.8.3 Documentation, matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar_label.html. Accessed 12 Mar. 2024. 
# - Mezzetti, David. “How to Work with Dates in Python.” Medium, Better Programming, 8 Feb. 2020, betterprogramming.pub/how-to-work-with-dates-in-python-dafa47d5cb3e. 
# - “Pandas.Dataframe.Rolling#.” Pandas.DataFrame.Rolling - Pandas 2.2.1 Documentation, pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html. Accessed 12 Mar. 2024. 
# - Rick Wicklin on The DO Loop. “The Running Median as a Time Series Smoother.” The DO Loop, 26 May 2021, blogs.sas.com/content/iml/2021/05/26/running-median-smoother.html. 
# - Writer, Stats. “What Is the Rolling Median in Pandas?” PSYCHOLOGICAL SCALES, 15 Nov. 2023, scales.arabpsychology.com/stats/what-is-the-rolling-median-in-pandas/. 

# In[ ]:





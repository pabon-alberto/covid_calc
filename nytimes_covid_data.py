from pandas import read_csv
import matplotlib.pyplot as plt
import matplotlib as mpl

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
ny_df = read_csv(url, index_col = 0, engine = 'pyarrow')

day_1 = ny_df[ny_df['state'].str.contains('Puerto Rico')].tail(7).iloc[0] #Cases seven days ago
day_6 = ny_df[ny_df['state'].str.contains('Puerto Rico')].tail(7).iloc[5] #Cases day before yesterday
day_7 = ny_df[ny_df['state'].str.contains('Puerto Rico')].tail(7).iloc[6] #Cases yesterday

wcases = day_7['cases'] - day_1['cases'] #Cases yesterday - cases seven days ago
dcases  = day_7['cases'] - day_6['cases'] #Cases yesterday - cases day before yesterday
ddeaths = day_7['deaths'] - day_6['deaths']
wdeaths = day_7['deaths'] - day_1['deaths']

#print(ny_df[ny_df['state'].str.contains('Puerto Rico')].tail(7)) #Prints only PR stats
# print('Stats for the lasts seven days:\n')
# print('Cases this week: '+ str(wcases))
# print('Deaths this week: '+ str(wdeaths) + '\n')

# print('Daily Stats:\n')
# print('Cases yesterday: '+ str(dcases))
# print('Deaths yesterday: ' + str(ddeaths) + '\n\n' + 'Remember that that the total number of cases can only be found when the day is over.\nThis is why there are no stats for the current day.')

c_array = []
pr_len = len(ny_df[ny_df['state'].str.contains('Puerto Rico')].cases) #The total amount of entries recorded in Puerto Rico. 
for i in range(29, -1, -1): #Entering the entries in the past week to the x-axis. Change first parameter to 29 to find entries for the past month. Change first parameter to pr_len for all-time data.
    c_array.append(ny_df[ny_df['state'].str.contains('Puerto Rico')].tail(30).iloc[i].cases) #Change .tail(...) to the amount of entries the graph will consider.

fig, ax = plt.subplots()

ax.plot(c_array)

ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}')) #Add commas to y-axis values for readability.
ax.invert_xaxis() #To organize the data for display.

plt.ylabel('Cases')
plt.xlabel('Days before Yesterday')
plt.title('Total Amount of Cases since Start of Pandemic')
plt.show()
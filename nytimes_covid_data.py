import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
ny_df = pd.read_csv(url, index_col = 0)

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
for i in range(6):
    c_array.append(ny_df[ny_df['state'].str.contains('Puerto Rico')].tail(7).iloc[i].cases)
    

plt.plot(c_array)
plt.ylabel('Cases')
plt.show()
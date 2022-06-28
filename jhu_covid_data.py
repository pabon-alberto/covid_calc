import pandas as pd

url = 'https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/testing_data/time_series_covid19_US.csv'
jh_df = pd.read_csv(url, index_col = 0)
pr_df = jh_df[jh_df['state'].str.contains('PR')].tail(7)

#For finding important columns
#print(pr_df[['cases_conf_probable','cases_confirmed','cases_probable', 'tests_viral_positive','tests_viral_negative','tests_viral_total', 'tests_antigen_positive','tests_antigen_total','people_viral_positive']]) #Prints only PR stats

day1 = pr_df.iloc[0] #Stats from a week ago
yesterday = pr_df.iloc[6] #Yesterday Stats


y_pcrtests = int(yesterday['tests_viral_total'] - day1['tests_viral_total']) #Weekly completed PCR Tests or other approved nucleic acid amplification test (NAAT).
y_pcrpos = int(yesterday['tests_viral_positive'] - day1['tests_viral_positive']) #Weekly PCR Tests or other approved nucleic acid amplification test (NAAT) that resulted positive.
y_atests = int(yesterday['tests_antigen_total'] - day1['tests_antigen_total']) #Weekly completed Antigen Tests.
y_apos = int(yesterday['tests_antigen_positive'] - day1['tests_antigen_positive']) #Weekly Antigen Tests that resulted positive.

pcrpos_rate = round((y_pcrpos/y_pcrtests)*100, 2) #Positivity rate in PCR Tests or other approved nucleic acid amplification test (NAAT).
apos_rate = round((y_apos/y_atests)*100, 2) #Positivity rate in Antigen Tests.

#Source for how to calculate positivity rate: https://www.coronavirus.in.gov/map/positive-test-rate.pdf

print('Stats for the last seven days:\n')

print('PCR Tests: ' + str(y_pcrtests)) #Weekly completed PCR Tests or other approved nucleic acid amplification test (NAAT).
print('PCR Tests Resulted Positive: '+ str(y_pcrpos)) #Weekly PCR Tests or other approved nucleic acid amplification test (NAAT) that resulted positive.
print('Positivity Rate with PCR Tests: ' + str(pcrpos_rate) + '%\n') #Positivity rate in PCR Tests or other approved nucleic acid amplification test (NAAT).

print('Antigen Tests: ' + str(y_atests)) #Weekly completed Antigen Tests.
print('Antigen Tests Resulted Positive: ' + str(y_apos)) #Weekly Antigen Tests that resulted positive.
print('Positivity Rate with Antigen Tests: ' + str(apos_rate) + '%\n') #Positivity rate in Antigen Tests.

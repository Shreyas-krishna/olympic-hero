# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

data = pd.read_csv(path)

data.rename(columns = {'Total':'Total_Medals'}, inplace = True)

#Code starts here

data.head(10)


# --------------
#Code starts here





data['Better_Event'] = np.where(data['Total_Summer']>data['Total_Winter'], 'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer']==data['Total_Winter'],'Both',data['Better_Event'])

data['Better_Event']

better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here

cols = data[['Country_Name','Total_Summer','Total_Winter','Total_Medals']]
top_countries = pd.DataFrame(cols)

top_countries.drop(top_countries.tail(1).index,inplace=True)

def top_ten(data, col):
    country_list = []
    country_list = list((data.nlargest(10,col)['Country_Name']))
    return country_list


top_10_summer=top_ten(top_countries,'Total_Summer')
print("Top 10 Summer:\n",top_10_summer, "\n")

top_10_winter=top_ten(top_countries,'Total_Winter')
print("Top 10 Winter:\n",top_10_winter, "\n")

top_10=top_ten(top_countries,'Total_Medals')
print("Top 10:\n",top_10, "\n")

common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print('Common Countries :\n', common, "\n")



# --------------
#Code starts here

summer_df = data[data['Country_Name'].isin(top_10_summer)]

winter_df = data[data['Country_Name'].isin(top_10_winter)]

top_df = data[data['Country_Name'].isin(top_10)]

summer_df.groupby('Country_Name')[['Total_Summer']].plot(kind='bar')


# --------------
#Code starts here

summer_df['Golden_Ratio'] = data['Gold_Summer']/data['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
print(summer_country_gold)

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/data['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
print(top_country_gold)


# --------------
#Code starts here

data_1=data[:-1]
data_1['Total_Points']= data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1
most_points = data_1['Total_Points'].max()
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']



# --------------
#Code starts here

best = data[data['Country_Name']==best_country]
best.reset_index(drop=True,inplace=True)
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
l=plt.legend()
l.get_texts()[0].set_text('Gold_Total :' + str(best['Gold_Total'].values))
l.get_texts()[1].set_text('Silver_Total :' + str(best['Silver_Total'].values))
l.get_texts()[2].set_text('Bronze_Total :' + str(best['Bronze_Total'].values))



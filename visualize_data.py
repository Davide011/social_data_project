import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
sns.set_theme(style="darkgrid")

# Read in the data
df = pd.read_csv('data_life.csv')
# print(df['Indicator'], df['Location'] , df['Period'], df['Value'])
df = df[['Indicator', 'Location', 'Period', 'Value', 'Dim1', 'Dim2']]
# print(df.head(20))
print(df['Indicator'].unique(), df['Location'].unique(), df['Period'].unique(), df['Dim1'].unique(), df['Dim2'].unique())

# print(df[df['Indicator'] == 'ex - expectation of life at age x'].head(20))
print(df)

df_2019 = df[df['Period'] == 2019]
age_groups = ['1-4 years', '5-9 years', '10-14 years', '20-24 years', '25-29 years', '30-34 years', '35-39 years', '40-44 years', '45-49 years', '50-54 years', '55-59 years', '60-64 years', '65-69 years', '70-74 years', '75-79 years', '80-84 years', '85+ years']

locations = df_2019['Location'].unique()
vals = dict()
for location in locations:
    temp = []
    df_male = df_2019[df_2019['Dim1'] == 'Male']
    df_location = df_male[df_male['Location'] == location]
    df_lx = df_location[df_location['Indicator'] == 'lx - number of people left alive at age x']

    # df_new = df_lx['Value']
    # print(df_lx)
    # print(df_lx)
    [temp.append(int(df_lx[df_lx['Dim2'] == x]['Value'].to_string().replace(u'\xa0', u'').split()[-1])/100000) for x in age_groups]
    # [vals.append(df_lx[df_lx['Dim2'] == x]['Value'].to_string()[-10:]) for x in age_groups]
    temp.insert(3, (temp[2] + temp[3])/2)
    vals[location] = temp

    # df_location_numpy = df_location['Value'].to_numpy()
    # df_born = df_location[df_location['Dim2'] == '<1 year']
    # df_lx = df_born[df_born['Indicator'] == 'lx - number of people left alive at age x']
    # print(df_lx)

print(vals)

ages = ['1', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80', '85+']


for key, val in vals.items():
    plt.plot(ages, val, label=key)
    plt.legend()
plt.ylabel('Fraction of people surviving to age x')
plt.xlabel('Age')
plt.title('Survival to age x by location in 2019')
plt.show()






# i = 0
# print(countries)
# countries = ['Denmark', 'Japan', 'Afghanistan', 'Australia', 'Brazil', 'United States']
# for country in countries:
#     df_country = df[df['country_name'] == country]
#     df_country_numpy = df_country['value'].to_numpy()
#     plt.plot(np.arange(1960, 2021), df_country_numpy, label=country)
#     plt.legend()
# plt.ylabel('Life Expectancy')
# plt.xlabel('Year')
# plt.title('Life Expectancy by Country')
# plt.show()

# for i in range(len(df_numpy)):
#     plt.plot(df_numpy[, 1:])
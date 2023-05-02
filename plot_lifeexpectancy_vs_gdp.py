import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from sklearn.linear_model import LinearRegression
sns.set_theme()

# load data
df = pd.read_csv('life_expectancy_by_country_with_GDP.csv')
# only keep data from 1980, 1990 and 2020
# df = df.loc[df['year'].isin([1980, 1990, 2020]), :]
# plot
# make markers circles and choose good colors

df = df.loc[df['year'].isin([1980, 1990, 2019]), :]

# remove Hong Kong and Macao from data
df = df.loc[~df['country_name'].isin(['Hong Kong SAR, China', 'Macao SAR, China']), :]
# remove rows with any nan values from data
df = df.loc[~df.isna().any(axis=1), :]

# conditional plot for the year 1980
df_1980 = df.loc[df['year'] == 1980, :]
# plt.scatter(data=df_1980, x='GDP', y='value', c='blue', marker='o', s=10, alpha=0.5, label='1980')
# fit a linear model between log GDP and life expectancy
reg = LinearRegression().fit(np.log(df_1980['GDP']).values.reshape(-1, 1), df_1980['value'].values.reshape(-1, 1))
# plot the linear model
x = np.linspace(start=4, stop=11, num=100)
y = reg.coef_[0][0] * x + reg.intercept_[0]
# plt.plot(np.exp(x), y, c='blue', alpha=0.5)

# conditional plot for the year 1990
df_1990 = df.loc[df['year'] == 1990, :]
# plt.scatter(data=df_1990, x='GDP', y='value', c='red', marker='o', s=10, alpha=0.5, label='1990')
# fit a linear model between log GDP and life expectancy
reg = LinearRegression().fit(np.log(df_1990['GDP']).values.reshape(-1, 1), df_1990['value'].values.reshape(-1, 1))
# plot the linear model
x = np.linspace(start=4, stop=11, num=100)
y = reg.coef_[0][0] * x + reg.intercept_[0]
# plt.plot(np.exp(x), y, c='red', alpha=0.5)

# conditional plot for the year 2020
df_2020 = df.loc[df['year'] == 2019, :]
plt.scatter(data=df_2020, x='GDP', y='value', c='green', marker='o', s=10, alpha=0.5, label='2020')
# fit a linear model between log GDP and life expectancy
reg = LinearRegression().fit(np.log(df_2020['GDP']).values.reshape(-1, 1), df_2020['value'].values.reshape(-1, 1))
# plot the linear model
x = np.linspace(start=4, stop=12, num=100)
y = reg.coef_[0][0] * x + reg.intercept_[0]
plt.plot(np.exp(x), y, alpha=0.5, c='darkgreen')

# annotate Japan with country name, make point bigger
df = df.loc[df['year'].isin([2019]), :]
for row in df.index:
    if df.loc[row, 'country_name'] in ['Japan', 'Germany', 'Italy']:
        plt.scatter(data=df.loc[row, :], x='GDP', y='value', c='black', marker='o', s=10, alpha=1)
        plt.text(x=df.loc[row, 'GDP'] + 0.2, y=df.loc[row, 'value'] + 0.3 - 1.6*(df.loc[row, 'country_name'] == 'Germany'), s=df.loc[row, 'country_name'], fontsize=8)

    




# plt.legend(title='Year')  
plt.title('Life expectancy vs GDP for countries in 2019')
# plt.xscale('log')
# make y axis go from 0 to 100
plt.ylim(40, 90)
plt.xlabel('GDP (in USD)')
plt.ylabel('Life expectancy (years)')
plt.show()
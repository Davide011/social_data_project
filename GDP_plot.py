# import data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
sns.set_theme(style="darkgrid")

# Read in the data for GDP
df_GDP = pd.read_csv('GDP_data/data.csv')

# read in the data for life expectancy
df = pd.read_csv('life_expectancy_by_country.csv')
df['GDP'] = np.nan

# loop over rows in df
for row in df.index:
    # get the country name
    country = df.loc[row, 'country_name']
    # get the year of the row
    year = df.loc[row, 'year']
    # get the GDP value for the country
    GDP = df_GDP.loc[df_GDP['Country Name'] == country, str(year)].values[0]
    # set the GDP value in df
    df.loc[row, 'GDP'] = GDP

# save new data frame
df.to_csv('life_expectancy_by_country_with_GDP.csv')
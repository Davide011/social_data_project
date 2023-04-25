import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
sns.set_theme(style="darkgrid")

# Read in the data
df = pd.read_csv('life_expectancy_by_country.csv')
for col in df.columns:
    print(col)
df_2019 = df[df['year'] == 2019]

# make barplot of values by country_name sorted
shortened_list = [
    'Hong Kong: China',
    'Sweden',
    'Gibraltar',
    'Greece',
    'Post-DD',
    'US Virgin Isl.',
    'Antigua/B.',
    'Slovakia',
    'E. Asia/Pac.',
    'Iran',
    'Romania',
    'Grenada',
    'Nicaragua',
    'Kazakhstan',
    'El Salvador',
    'Ukraine',
    'Uzbekistan',
    'S. Asia',
    'Other S. States',
    'Pakistan',
    'Botswana',
    'Africa E/S',
    'Zambia',
    'Sub-Saharan', 
    'Sierra Leone', 
    'Chad'
]

df_2019 = df_2019.sort_values(by=['value'], ascending=False).iloc[::10, :]
df_2019['country_name'] = shortened_list

print(df_2019.country_name.to_list())
plt.figure(figsize=(12, 5))
sns.barplot(x='country_name', y='value', data=df_2019)
plt.ylabel('Life expectancy at birth (years)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.title('Life expectancy by country in 2019')
plt.show()
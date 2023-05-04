import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

import plotly.graph_objects as go
import numpy as np

# countries: 'Japan', 'Denmark', 'Deutchland', 'Brazil', 'USA', 'Sweden', 'Bolivia', 'South_Africa'

# make dict with countries and years
all_data = dict()

country = "Japan"
# Make plot for Japan 1960
year = 1960
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot for Japan 2019
year = 2019
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

country = "Denmark"
# Make plot for Denmark 1960
year = 1960
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == 1961]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot for Denmark 2019
year = 2019
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot of Denmark 1901
year = 1901
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df



country = "Deutchland"
# Make plot for Deutchland 1960
year = 1960
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot for Deutchland 2019
year = 2019
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot for Brazil 1960
country = "Brazil"
year = 1960
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df


# Make plot for Brazil 2019
year = 2019
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot for USA 1960
country = "USA"
year = 1960
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot for USA 2019
year = 2019
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot for Sweden 1960
country = "Sweden"
year = 1960
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot for Sweden 2019
year = 2019
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot of Sweden 1751
year = 1751
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df
# Make plot for South Africa 1960
country = "South_Africa"
year = 1960
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot for South Africa 2006
year = 2006
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[df['TypeLT'] == 1]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot of India 1961
country = "India"
year = 1961
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['TypeLT'] == 1]
df = df[df['Year1'] == year]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df

# Make plot of India 2014
year = 2014
df = pd.read_csv('life_tables/' + country + '.csv')
df = df[df['Year1'] == year]
df = df[["Age", "l(x)", "Sex"]]
df = df.groupby(['Age']).sum()
df = df[['l(x)']]
all_data[(country, year)] = df









for key, val in all_data.items():
     divisor = val.head(1).values[0][0]
     for i in range(len(val)):
          val.iloc[i] = val.iloc[i] / divisor * 100
fig = go.Figure()

colors = ['firebrick', 'royalblue', 'green', 'orange', 'purple', 'red', 'black', 'deepskyblue']
styles = ['solid', 'dash', 'dot', 'dashdot']
for i, country in enumerate(['Japan', 'Denmark', 'Deutchland', 'Brazil', 'USA', 'Sweden', 'South_Africa', 'India']):
     for j, year in enumerate([2019, 2014, 2006, 1961, 1960, 1901, 1751]):
          if year > 2000:
               j = 0
          elif year < 2000 and year > 1950:
               j = 1
          else:
               j = 2

          if (country, year) in all_data:
               vis = 'legendonly'
               if country in ['India', 'Japan']:
                    vis = None
               fig.add_trace(go.Scatter(x=list(all_data[(country, year)].index.values), y=all_data[(country, year)].to_numpy()[:,0].tolist(), name=str(country + ' ' + str(year)).replace('_', ' '),
                                        line=dict(color=colors[i], width=2, dash=styles[j]), opacity=1, mode='lines', visible=vis, showlegend=True))

# Edit the layout
fig.update_layout(title='Chance of surviving till age for various countries and times',
                   xaxis_title='Age',
                   yaxis_title='Chance of surviving to this age (%)',
                   yaxis_range=[0,100],
                   xaxis_range=[0,100])


fig.show()
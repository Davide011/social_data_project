import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

df = px.data.gapminder().query("continent=='Oceania'")

# print(df)

# open life_tables folder and read in the data
countries = ['Japan', 'Denmark', 'Deutchland', 'Brazil', 'USA', 'Sweden', 'Bolivia', 'South_Africa']
colors = ['rgb(255, 0, 0)', 'rgb(0, 255, 0)', 'rgb(0, 0, 0)', 'rgb(0, 0, 255)', 'rgb(165, 42, 42)', 'rgb(255, 255, 0)', 'rgb(0, 255, 255)', 'rgb(255, 0, 255)']
years = [1960, 2019]
final_df = pd.DataFrame()
for country in countries:
    # check which years each coyntry has:
    df = pd.read_csv('life_tables/' + country + '.csv')
    print(country, df['Year1'].unique(), df['Year2'].unique())
    # for year in years:
    #     df = pd.read_csv('life_tables/' + country + '.csv')

        

        # df = df[df['Year1'] == year]
        # df = df[df['TypeLT'] == 1]
        # df = df[['Age', 'l(x)', 'Sex']]
        # df = df.groupby(['Age']).sum()
        # df = df[['l(x)']]
        # df['country'] = country
        # df['year'] = year
        # # add df to final_df
        # final_df = pd.concat([final_df, df], axis=0)

# print(final_df)


# make a plot that has the same color fr 1960 and 2019, but different line styles.
# The plot should have a legend that shows the country name and the year, and the countries are toggleable.


# fig = go.Figure()
# for country in countries:
#     for year in years:
#         df = final_df[final_df['country'] == country]
#         df = df[df['year'] == year]
#         fig.add_trace(go.Scatter(x=df.index, y=df['l(x)'], name=country + ' ' + str(year), line=dict(color='rgb(204, 204, 204)')))
# fig.show()


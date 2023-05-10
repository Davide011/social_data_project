import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set_theme()

oldest = pd.read_csv('GDP_data/life_cap.csv')
print(oldest)


# Make plot of India 1961
# country = "India"
# year = 1961
# df = pd.read_csv('life_tables/' + country + '.csv')
# df = df[df['TypeLT'] == 1]
# df = df[df['Year1'] == year]
# df = df[["Age", "l(x)", "Sex"]]
# df = df.groupby(['Age']).sum()
# df = df[['l(x)']]
# all_data[(country, year)] = df

japan_life_table = pd.read_csv('life_tables/Japan.csv')
for col in japan_life_table.columns:
    print(col)
japan_life_table = japan_life_table[japan_life_table['TypeLT'] == 1]
japan_life_table = japan_life_table[["Age", "l(x)", "Sex", "Year1", "e(x)Orig", "e(x)"]]

# find all values of year in data
years = japan_life_table['Year1'].unique()
all_lx = []
all_ex = []

for year in years:
    # Make plot for Japan 1960
    df = japan_life_table[japan_life_table['Year1'] == year]
    # df = df[["Age", "l(x)", "Sex"]]

    df = df.groupby(['Age']).sum()
    all_lx.append(df[['l(x)']].to_numpy().flatten() / 2)
    all_ex.append(df[['e(x)']].to_numpy().flatten() / 2)

all_lx = [x / x[0] for x in all_lx]

for i in [1, 0.1]:
    years_of_oldest_quantile = [np.argmax(x <= i) for x in all_lx]
    LE_at_years_of_oldest_quantile = [all_ex[i][years_of_oldest_quantile[i]] for i in range(len(years_of_oldest_quantile))]
    LE_at_quantile = np.array(years_of_oldest_quantile) + np.array(LE_at_years_of_oldest_quantile)
    only_years_after_1960 = [x for x in years if x >= 1964]
    only_LE_after_1960 = [x for i, x in enumerate(LE_at_quantile) if years[i] >= 1964]
    if i == 0.1:
        plt.plot(only_years_after_1960, only_LE_after_1960, label="Life expectancy of 10 percent oldest in Japan")
    else:
        plt.plot(only_years_after_1960, only_LE_after_1960, label="Life expectancy in Japan")
    
plt.plot(oldest['year'][1:], oldest['age'][1:], label="Oldest human in the world")
plt.legend()
plt.title("Age of oldest human compared to life expectancy in Japan")
plt.xlabel("Year")
plt.ylabel("Life expectancy (years)")
plt.show()



# # Make a line plot
# sns.lineplot(data=oldest, x='year', y='age')
# plt.title('Life Expectancy at Birth')
# plt.ylabel('Years')
# plt.xlabel('Year')
# plt.show()
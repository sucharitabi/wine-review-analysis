import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/sucharita/Desktop/wine_eda_project/data/winemag-data-130k-v2.csv'

df = pd.read_csv(file_path)


def plot_point_category_distribution(df):
 

  total = len(df)
  plt.figure(figsize=(14, 6))
  g = sns.countplot(x='rating_cat', color='darkblue', data=df)
  g.set_title("Point Categories Counting Distribution", fontsize=20)
  g.set_xlabel("Categories", fontsize=15)
  g.set_ylabel("Total Count", fontsize=15)

  for bar in g.patches:
    height = bar.get_height()
    percentage = (height / total) * 100
    g.text(bar.get_x() + bar.get_width() / 2,
            height + 3,
            f'{percentage:.1f}%',
            ha='center', fontsize=12)

  plt.savefig('/Users/sucharita/Desktop/wine_eda_project/outputs/Point Categories Counting Distribution.png')
  plt.show()


def plot_correlation_between_price_and_points(df):
  

  correlation = df['price'].corr(df['points'])
  plt.figure(figsize=(10, 6))
  sns.scatterplot(data=df, x='price', y='points', alpha=0.6)
  sns.regplot(data=df, x='price', y='points', scatter=False, color='red')
  plt.title(f'Correlation between Price and Points: {correlation:.2f}', fontsize=14)
  plt.xlabel('Price ($)', fontsize=12)
  plt.ylabel('Points (Ratings)', fontsize=12)
  plt.grid(alpha=0.3)
  plt.savefig('/Users/sucharita/Desktop/wine_eda_project/outputs/Correlation between Price and Points.png')
  plt.show()


def plot_scatter_plot_of_points_vs_price(df):
  

  plt.figure(figsize=(10, 6))
  plt.scatter(df['points'], df['price'], alpha=0.5)
  plt.xlabel('Points')
  plt.ylabel('Price')
  plt.title('Scatter Plot of Points vs. Price')
  plt.savefig('/Users/sucharita/Desktop/wine_eda_project/outputs/Scatter Plot of Points vs. Price.png')
  plt.show()


def plot_price_and_point_distribution(df):
  

  plt.figure(figsize=(10,4))
  g = sns.regplot(x='points', y='price_log', data=df, line_kws={'color':'red'},
                  x_jitter=True, fit_reg=True, color='darkblue')
  g.set_title("Points x Price Distribuition", fontsize=20)
  g.set_xlabel("Points", fontsize= 15)
  g.set_ylabel("Price (log)", fontsize= 15)
  plt.savefig('/Users/sucharita/Desktop/wine_eda_project/outputs/Points x Price Distribuition.png')
  plt.show()

top_20_countries = df['country'].value_counts().head(20)


plt.figure(figsize=(10,12))

plt.subplot(2,1,1)
g = sns.boxplot(x='country', y='price_log',
                  data=df.loc[(df.country.isin(top_20_countries.index.values))],
                 color='darkblue')
g.set_title("Price by Country Of Wine Origin", fontsize=20)
g.set_xlabel("Country's ", fontsize=15)
g.set_ylabel("Price Dist(US)", fontsize=15)
g.set_xticklabels(g.get_xticklabels(),rotation=45)

plt.subplot(2,1,2)
g1 = sns.boxplot(x='country', y='points',
                   data=df[df.country.isin(top_20_countries.index.values)],
                 color='darkblue')
g1.set_title("Points by Country Of Wine Origin", fontsize=20)
g1.set_xlabel("Country's ", fontsize=15)
g1.set_ylabel("Points", fontsize=15)
g1.set_xticklabels(g1.get_xticklabels(),rotation=45)

plt.subplots_adjust(hspace = 0.6,top = 0.9)

plt.savefig('/Users/sucharita/Desktop/wine_eda_project/outputs/Price and Points by Country Of Wine Origin.png')

plt.show()
import pandas as pd


def clean_data(df):
 

  df.fillna({'region_1': 'Unknown', 'region_2': 'Unknown', 'designation': 'not found'}, inplace=True)
  df['price'].fillna(df['price'].median(), inplace=True)
  df["taster_twitter_handle"] = df["taster_twitter_handle"].fillna('not found')
  df["taster_name"] = df["taster_name"].fillna('Unknown')
  df["price"] = df["price"].fillna(df["price"].median())

  # Drop unnecessary column (assuming you don't need it)
  df = df.drop(columns=['Unnamed: 0'])

  # Save the cleaned data
  df.to_csv('/Users/sucharita/Desktop/wine_eda_project/data/cleaned_wine_data.csv', index=False)

  return df
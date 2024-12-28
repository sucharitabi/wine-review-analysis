
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/sucharita/Desktop/wine_eda_project/data/winemag-data-130k-v2.csv'

df = pd.read_csv(file_path)


def cat_points(points):

  if 80 <= points <= 82:
    return 0
  elif 83 <= points <= 86:
    return 1
  elif 87 <= points <= 89:
    return 2
  elif 90 <= points <= 93:
    return 3
  elif 94 <= points <= 97:
    return 4
  else:
    return 5

def analyze_outliers(data):
  
  Q1 = data.quantile(0.25)
  Q3 = data.quantile(0.75)
  IQR = Q3 - Q1

  lower_bound = Q1 - 1.5 * IQR
  upper_bound = Q3 + 1.5 * IQR

  lower_outliers = data[data < lower_bound]
  upper_outliers = data[data > upper_bound]
  total_outliers = pd.concat([lower_outliers, upper_outliers])

  total_observations = len(data)
  non_outliers = total_observations - len(total_outliers)
  outlier_percentage = (len(total_outliers) / total_observations) * 100

  print(f"Identified lowest outliers: {len(lower_outliers)}")
  print(f"Identified upper outliers: {len(upper_outliers)}")
  print(f"Identified outliers: {len(total_outliers)}")
  print(f"Non-outlier observations: {non_outliers}")
  print(f"Total percentual of Outliers: {outlier_percentage:.4f}")

  return total_outliers




# Print data statistics
print("Statistics of numerical data: ")
print(df.describe())

# Create point category DataFrame
df["rating_cat"] = df["points"].apply(cat_points)

# Point categories distribution plot
total = len(df)
plt.figure(figsize=(14, 6))
g = sns.countplot(x='rating_cat', color='darkblue', data=df)
g.set_title("Point Categories Counting Distribution", fontsize=20)
g.set_xlabel("Categories", fontsize=15)
g.set_ylabel("Total Count", fontsize=15)

for bar in g.patches:
  height = bar.get_height()
  percentage = (height / total) * 100
  g.text(bar.get_x)
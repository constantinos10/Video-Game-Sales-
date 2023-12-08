import pandas as pd
import os
import matplotlib.pyplot as plt  # Add this line to import the matplotlib module

# Provide the full path to the 'vgsales.csv' file
file_path = r'C:\Users\User\Desktop\constantinos\sports data analytics\2.Sports Analytics School - Programming Full Course Training 2023\9.Practical Examples on data analysis\datasets\videogames\vgsales.csv'

try:
    df = pd.read_csv(file_path)
    # Continue with your data processing or analysis here
    print(df.head())  # Example: Display the first 5 rows of the DataFrame
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except pd.errors.EmptyDataError:
    print(f"Error: The file '{file_path}' is empty.")
except pd.errors.ParserError:
    print(f"Error: There was an issue parsing the file '{file_path}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Group data by platform and sum global sales
platform_sales = df.groupby('Platform')['Global_Sales'].sum()
# Sort by global sales in descending order
platform_sales = platform_sales.sort_values(ascending=False)
# Display platform sales
print(platform_sales)

# Additional analysis and visualization
genre_sales = df.groupby('Genre')['Global_Sales'].sum()
genre_sales = genre_sales.sort_values(ascending=False)
print(genre_sales)

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(platform_sales.index, platform_sales.values, color='blue')
plt.xlabel('Platform')
plt.ylabel('Global Sales (in millions)')
plt.title('Video Game Sales by Platform')
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(genre_sales.index, genre_sales.values, color='green')
plt.xlabel('Genre')
plt.ylabel('Global Sales (in millions)')
plt.title('Video Game Sales by Genre')
plt.xticks(rotation=45)
plt.show()
# create a scatter plot showing the relationship between year of release and global sales
plt.scatter(df['Year'], df['Global_Sales'])
plt.title('Year of Release vs Global Sales')
plt.xlabel('Year')
plt.ylabel('Global Sales (millions)')
plt.show()
# group data by publisher and sum global sales
publisher_sales = df.groupby('Publisher')['Global_Sales'].sum()
# sort by global sales
publisher_sales = publisher_sales.sort_values(ascending=False)
# create a bar chart showing top publishers by global sales
publisher_sales.head(10).plot(kind='bar')
plt.title('Top Publishers by Global Sales')
plt.xlabel('Publisher')
plt.ylabel('Global Sales (millions)')
plt.show()
# calculate mean and variance of global sales data
mean_sales = df['Global_Sales'].mean()
var_sales = df['Global_Sales'].var()
# calculate expected mean and variance of Poisson distribution
exp_mean = var_sales
exp_var = var_sales
# compare mean and variance to expected values for Poisson distribution
print('Mean of global sales data:', mean_sales)
print('Variance of global sales data:', var_sales)
print('Expected mean of Poisson distribution:', exp_mean)
print('Expected variance of Poisson distribution:', exp_var)
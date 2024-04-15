import json
import pandas as pd

# Load JSON data from the file
with open('data/Takeout/Fitbit/Global Export Data/steps-2022-07-16.json') as file:
    data = json.load(file)
    
# Create a DataFrame from the JSON data
df = pd.DataFrame(data)

# Convert dateTime to datetime type and value to integer
df['dateTime'] = pd.to_datetime(df['dateTime'])
df['value'] = pd.to_numeric(df['value'])

# Group by date and sum the values
df_grouped = df.groupby(df['dateTime'].dt.date).agg({'value': 'sum'}).reset_index()

# Rename columns for clarity
df_grouped.columns = ['date', 'steps']

# Save the DataFrame to a CSV file
output_file = '/mnt/data/summarized_step_data.csv'
df_grouped.to_csv(output_file, index=False)
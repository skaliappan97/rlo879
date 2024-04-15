import pandas as pd
import sys

def filter_and_aggregate(datafile, entry_type, per_data='startDate'):
    # Read the CSV file
    df = pd.read_csv(datafile)

    # Filter rows based on the type
    df_filtered = df[df['type'] == entry_type]

    # Convert startDate to datetime and normalize to date only
    df_filtered[per_data] = pd.to_datetime(df_filtered[per_data]).dt.date

    # Ensure 'value' is treated as numeric for summing
    df_filtered['value'] = pd.to_numeric(df_filtered['value'], errors='coerce')

    # Aggregate sum of 'value' for each day
    result = df_filtered.groupby(per_data)['value'].sum().reset_index()

    # Rename columns for clarity
    result.columns = ['Date', 'Total Value']


    # Export to CSV
    result.to_csv('steps.csv', index=False)
    print(f'File {entry_type}_summary.csv has been created with the aggregated data.')

if __name__ == '__main__':
        datafile = 'apple_health_export_2024-04-15.csv'
        entry_type = 'StepCount'
        per_data = 'startDate'
        filter_and_aggregate(datafile, entry_type,per_data)


import pandas as pd
import sys

def calculate_sleep(datafile, entry_type):
    # Read the CSV file
    df = pd.read_csv(datafile)

    # Filter rows based on the type (e.g., Sleep or sleep)
    df_filtered = df[df['type'].str.lower() == entry_type.lower()]

    # Convert startDate and endDate to datetime
    df_filtered['startDate'] = pd.to_datetime(df_filtered['startDate'])
    df_filtered['endDate'] = pd.to_datetime(df_filtered['endDate'])

    # Calculate the sleep duration in hours
    df_filtered['value'] = (df_filtered['endDate'] - df_filtered['startDate']).dt.total_seconds() / 3600

    # Normalize startDate to date only for grouping
    df_filtered['startDate'] = df_filtered['startDate'].dt.date

    # Aggregate sum of 'value' for each day
    result = df_filtered.groupby('startDate')['value'].sum().reset_index()

    # Rename columns for clarity
    result.columns = ['Date', 'Total Value']

    # Export to CSV
    output_filename = 'sleep.csv'
    result.to_csv(output_filename, index=False)
    print(f'File {output_filename} has been created with the aggregated sleep data.')

if __name__ == '__main__':
        datafile = 'apple_health_export_2024-04-15.csv'
        entry_type = 'SleepAnalysis'
        calculate_sleep(datafile, entry_type)


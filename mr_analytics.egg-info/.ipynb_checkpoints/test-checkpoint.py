import pandas as pd
from mr_analytics.mr_analaytics import load_csv, clean_missing_values, summarize_data, filter_data, group_and_aggregate, save_to_csv

# Load data
df = load_csv('data.csv')

# Clean missing values
df_cleaned = clean_missing_values(df, strategy='fill', fill_value=0)

# Summarize data
summary = summarize_data(df_cleaned)
print(summary)

# Filter data
filtered_df = filter_data(df_cleaned, {'column_name': '>= 10'})

# Group and aggregate data
aggregated_df = group_and_aggregate(filtered_df, 'group_column', {'value_column': 'sum'})

# Save to CSV
save_to_csv(aggregated_df, 'output.csv')

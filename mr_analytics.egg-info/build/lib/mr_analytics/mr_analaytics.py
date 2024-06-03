import pandas as pd

def load_csv(file_path):
    """
    Load a CSV file into a DataFrame.
    
    Parameters:
    file_path (str): The path to the CSV file.
    
    Returns:
    pd.DataFrame: The loaded DataFrame.
    """
    return pd.read_csv(file_path)

def clean_missing_values(df, strategy='drop', fill_value=None):
    """
    Handle missing values in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to clean.
    strategy (str): The strategy to handle missing values. Options are 'drop' or 'fill'.
    fill_value: The value to fill in missing values if strategy is 'fill'.
    
    Returns:
    pd.DataFrame: The DataFrame with missing values handled.
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill':
        return df.fillna(fill_value)
    else:
        raise ValueError("Strategy must be either 'drop' or 'fill'.")

def summarize_data(df):
    """
    Provide a summary of the DataFrame.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to summarize.
    
    Returns:
    dict: A dictionary containing the summary of the DataFrame.
    """
    summary = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'info': df.info(),
        'describe': df.describe().to_dict()
    }
    return summary

def filter_data(df, filter_conditions):
    """
    Filter the DataFrame based on given conditions.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to filter.
    filter_conditions (dict): A dictionary containing column names as keys and conditions as values.
    
    Returns:
    pd.DataFrame: The filtered DataFrame.
    """
    for column, condition in filter_conditions.items():
        df = df.query(f"{column} {condition}")
    return df

def group_and_aggregate(df, group_by_column, agg_dict):
    """
    Group the DataFrame by a column and perform an aggregation.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to group and aggregate.
    group_by_column (str): The column to group by.
    agg_dict (dict): A dictionary specifying the aggregations to perform.
    
    Returns:
    pd.DataFrame: The grouped and aggregated DataFrame.
    """
    return df.groupby(group_by_column).agg(agg_dict)

def save_to_csv(df, file_path):
    """
    Save the DataFrame to a CSV file.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to save.
    file_path (str): The path to save the CSV file.
    """
    df.to_csv(file_path, index=False)

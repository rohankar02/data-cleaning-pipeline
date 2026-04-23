import pandas as pd

# Creating new columns for our analysis

def get_date_details(df, date_column_name):
    # Change the column to a date format
    df[date_column_name] = pd.to_datetime(df[date_column_name])
    
    # Extract year and month so we can see trends
    df['year_extracted'] = df[date_column_name].dt.year
    df['month_extracted'] = df[date_column_name].dt.month
    
    return df

def convert_text_to_numbers(df, columns_to_change):
    # This turns words into numbers so models can understand them
    # It creates new columns (One-Hot Encoding)
    return pd.get_dummies(df, columns=columns_to_change)

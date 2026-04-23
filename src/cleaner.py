import pandas as pd
import numpy as np

# Functions to clean our messy data for the project

def fill_missing_values(df, numerical_columns, categorical_columns):
    # This function looks for empty cells and fills them
    for col in numerical_columns:
        # We use the average (median) to fill empty numbers
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)
        
    for col in categorical_columns:
        # We use the most common word (mode) to fill empty text boxes
        most_common = df[col].mode()[0] if not df[col].mode().empty else "Unknown"
        df[col] = df[col].fillna(most_common)
    
    return df

def clean_outliers(df, columns_to_check):
    # This function removes weird data points (outliers) using the IQR method
    # It keeps only the data that is within a normal range
    for col in columns_to_check:
        first_quarter = df[col].quantile(0.25)
        third_quarter = df[col].quantile(0.75)
        iqr_value = third_quarter - first_quarter
        
        # Calculate the boundaries
        lower_limit = first_quarter - 1.5 * iqr_value
        upper_limit = third_quarter + 1.5 * iqr_value
        
        # Filter the data
        df = df[(df[col] >= lower_limit) & (df[col] <= upper_limit)]
        
    return df

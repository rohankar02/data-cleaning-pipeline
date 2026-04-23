import pandas as pd
import numpy as np
from scipy import stats

class DataCleaner:
    """
    A robust data cleaning module for handling missing values and outliers.
    """
    
    @staticmethod
    def handle_missing_values(df, strategy='mean', numerical_cols=None, categorical_cols=None):
        """
        Handles missing values using various strategies.
        """
        df_cleaned = df.copy()
        
        if numerical_cols:
            for col in numerical_cols:
                if strategy == 'mean':
                    df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].mean())
                elif strategy == 'median':
                    df_cleaned[col] = df_cleaned[col].fillna(df_cleaned[col].median())
                elif strategy == 'zero':
                    df_cleaned[col] = df_cleaned[col].fillna(0)
                    
        if categorical_cols:
            for col in categorical_cols:
                # Mode imputation for categorical
                mode_val = df_cleaned[col].mode()
                if not mode_val.empty:
                    df_cleaned[col] = df_cleaned[col].fillna(mode_val[0])
                else:
                    df_cleaned[col] = df_cleaned[col].fillna('Unknown')
                    
        return df_cleaned

    @staticmethod
    def remove_outliers_zscore(df, columns, threshold=3):
        """
        Removes outliers based on Z-score.
        """
        df_cleaned = df.copy()
        for col in columns:
            z_scores = np.abs(stats.zscore(df_cleaned[col].dropna()))
            # Map back to original indices
            non_null_indices = df_cleaned[col].dropna().index
            outlier_indices = non_null_indices[z_scores > threshold]
            df_cleaned = df_cleaned.drop(outlier_indices)
        return df_cleaned

    @staticmethod
    def remove_outliers_iqr(df, columns):
        """
        Removes outliers based on Interquartile Range (IQR).
        """
        df_cleaned = df.copy()
        for col in columns:
            Q1 = df_cleaned[col].quantile(0.25)
            Q3 = df_cleaned[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df_cleaned = df_cleaned[(df_cleaned[col] >= lower_bound) & (df_cleaned[col] <= upper_bound)]
        return df_cleaned

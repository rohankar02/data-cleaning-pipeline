import pandas as pd
import numpy as np

class FeatureEngineer:
    """
    Module for feature engineering and transformation.
    """
    
    @staticmethod
    def create_date_features(df, date_col):
        """
        Extracts features from datetime columns.
        """
        df[date_col] = pd.to_datetime(df[date_col])
        df['year'] = df[date_col].dt.year
        df['month'] = df[date_col].dt.month
        df['day'] = df[date_col].dt.day
        df['day_of_week'] = df[date_col].dt.dayofweek
        df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
        return df

    @staticmethod
    def encode_categorical(df, columns):
        """
        Performs one-hot encoding for categorical variables.
        """
        return pd.get_dummies(df, columns=columns, drop_first=True)

    @staticmethod
    def scaling_features(df, columns):
        """
        Basic min-max scaling for demonstration.
        """
        df_scaled = df.copy()
        for col in columns:
            df_scaled[col] = (df_scaled[col] - df_scaled[col].min()) / (df_scaled[col].max() - df_scaled[col].min())
        return df_scaled

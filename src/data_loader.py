import pandas as pd
import numpy as np
import io
import requests

class DataLoader:
    """
    Handles data acquisition from various sources.
    """
    
    @staticmethod
    def get_titanic_data():
        """
        Fetches the quintessential Kaggle Titanic dataset.
        """
        url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        try:
            response = requests.get(url)
            df = pd.read_csv(io.StringIO(response.text))
            return df
        except Exception as e:
            print(f"Error fetching Titanic data: {e}")
            return None

    @staticmethod
    def generate_messy_sales_data(rows=1000):
        """
        Generates a messy dataset for demonstration purposes.
        Includes missing values, outliers, and trend potential.
        """
        np.random.seed(42)
        dates = pd.date_range(start='2020-01-01', periods=rows, freq='D')
        
        data = {
            'Date': dates,
            'Product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'], rows),
            'Sales': np.random.normal(500, 150, rows),
            'Quantity': np.random.randint(1, 10, rows),
            'Discount': np.random.uniform(0, 0.3, rows),
            'Region': np.random.choice(['North', 'South', 'East', 'West', None], rows, p=[0.2, 0.2, 0.2, 0.2, 0.2])
        }
        
        df = pd.DataFrame(data)
        
        # Inject missing values
        df.loc[df.sample(frac=0.1).index, 'Sales'] = np.nan
        df.loc[df.sample(frac=0.05).index, 'Quantity'] = np.nan
        
        # Inject outliers
        df.loc[df.sample(n=10).index, 'Sales'] = df['Sales'].max() * 5
        df.loc[df.sample(n=10).index, 'Quantity'] = 500  # Extreme outlier
        
        # Add a trend
        df['Sales'] = df['Sales'] + (np.arange(rows) * 0.5)  # Upward trend
        
        return df

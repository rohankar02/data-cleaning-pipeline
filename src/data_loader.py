import pandas as pd
import numpy as np
import io
import requests

# Helper script to get data for my cleaning project

def get_titanic_dataset():
    # This downloads the Titanic data from a GitHub link
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    try:
        response = requests.get(url)
        df = pd.read_csv(io.StringIO(response.text))
        return df
    except:
        print("Could not download data.")
        return None

def generate_messy_sales_data(rows=1000):
    # This creates a dummy messy dataset so I can practice cleaning
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
    
    # Intentionally putting in empty boxes (NaN)
    df.loc[df.sample(frac=0.1).index, 'Sales'] = np.nan
    df.loc[df.sample(frac=0.05).index, 'Quantity'] = np.nan
    
    # Adding a trend for my graphs
    df['Sales'] = df['Sales'] + (np.arange(rows) * 0.5)
    
    return df

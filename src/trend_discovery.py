import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class TrendDiscoverer:
    """
    Module for identifying trends and patterns in data.
    """
    
    @staticmethod
    def analyze_time_trends(df, date_col, value_col):
        """
        Analyzes and plots trends over time.
        """
        df_sorted = df.sort_values(by=date_col)
        
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df_sorted, x=date_col, y=value_col)
        plt.title(f'Trend Analysis: {value_col} over {date_col}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('trend_analysis.png')
        plt.close()
        
        # Calculate moving average
        df_sorted['moving_avg'] = df_sorted[value_col].rolling(window=7).mean()
        return df_sorted

    @staticmethod
    def correlation_heat_map(df):
        """
        Generates a correlation matrix to find relationships.
        """
        plt.figure(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Feature Correlation Matrix')
        plt.tight_layout()
        plt.savefig('correlation_matrix.png')
        plt.close()

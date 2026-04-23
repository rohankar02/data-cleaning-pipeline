import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Basic visualization functions for the project

def show_sales_trend(df, date_col, value_col):
    # Sort by date so the graph looks correct
    df_plot = df.sort_values(by=date_col)
    
    plt.figure(figsize=(10, 5))
    plt.plot(df_plot[date_col], df_plot[value_col])
    plt.title('Sales Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.savefig('my_sales_trend_chart.png')
    print("Graph saved as 'my_sales_trend_chart.png'")

def show_correlations(df):
    # Create a heatmap to see how columns are related
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True)
    plt.title('My Feature Correlation Heatmap')
    plt.savefig('my_correlation_chart.png')
    print("Correlation chart saved.")

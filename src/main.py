from data_loader import DataLoader
from cleaner import DataCleaner
from feature_engineering import FeatureEngineer
from trend_discovery import TrendDiscoverer
import pandas as pd

def main():
    print("--- Starting Data Cleaning Pipeline ---")
    
    # 1. Load Data
    print("Step 1: Loading Messy Dataset...")
    loader = DataLoader()
    df = loader.generate_messy_sales_data(rows=500)
    print(f"Dataset Loaded. Shape: {df.shape}")
    print(df.isnull().sum())

    # 2. Handle Missing Values
    print("\nStep 2: Cleaning Missing Values...")
    cleaner = DataCleaner()
    df_cleaned = cleaner.handle_missing_values(
        df, 
        strategy='median', 
        numerical_cols=['Sales', 'Quantity'],
        categorical_cols=['Region']
    )
    print(f"Missing values after cleaning:\n{df_cleaned.isnull().sum()}")

    # 3. Remove Outliers
    print("\nStep 3: Removing Outliers...")
    df_no_outliers = cleaner.remove_outliers_iqr(df_cleaned, ['Sales', 'Quantity'])
    print(f"Shape after outlier removal: {df_no_outliers.shape}")

    # 4. Feature Engineering
    print("\nStep 4: Performing Feature Engineering...")
    engineer = FeatureEngineer()
    df_engineered = engineer.create_date_features(df_no_outliers, 'Date')
    df_engineered = engineer.encode_categorical(df_engineered, ['Product', 'Region'])
    print(f"New column list: {list(df_engineered.columns)}")

    # 5. Trend Discovery
    print("\nStep 5: Discovering Trends...")
    discoverer = TrendDiscoverer()
    df_trends = discoverer.analyze_time_trends(df_engineered, 'Date', 'Sales')
    discoverer.correlation_heat_map(df_engineered)
    
    print("\n--- Pipeline Execution Complete ---")
    print("Visualizations saved: 'trend_analysis.png', 'correlation_matrix.png'")
    df_engineered.to_csv('cleaned_data.csv', index=False)
    print("Cleaned data saved to 'cleaned_data.csv'")

if __name__ == "__main__":
    main()

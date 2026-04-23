import data_loader
import cleaner
import feature_engineering
import trend_discovery
import pandas as pd

# This is the main part of my Data Cleaning project

def run_my_pipeline():
    print("Step 1: Getting the messy data...")
    # Using my data loader script to get a messy sales file
    raw_df = data_loader.generate_messy_sales_data(rows=400)
    print(f"Data Loaded! Total rows: {len(raw_df)}")

    print("Step 2: Fixing missing values...")
    # Fill empty boxes in Sales, Quantity and Region
    df_no_nulls = cleaner.fill_missing_values(
        raw_df, 
        numerical_columns=['Sales', 'Quantity'], 
        categorical_columns=['Region']
    )

    print("Step 3: Removing outliers...")
    # Strip away the weird/extreme numbers
    df_clean = cleaner.clean_outliers(df_no_nulls, ['Sales', 'Quantity'])

    print("Step 4: Making new features...")
    # Extract dates and convert categories
    df_with_dates = feature_engineering.get_date_details(df_clean, 'Date')
    df_final = feature_engineering.convert_text_to_numbers(df_with_dates, ['Product', 'Region'])

    print("Step 5: Saving the output...")
    # Save to a clean CSV file
    df_final.to_csv('cleaned_output_data.csv', index=False)
    print("Project finished successfully! Output saved to 'cleaned_output_data.csv'")

if __name__ == "__main__":
    run_my_pipeline()

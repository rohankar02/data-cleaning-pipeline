# 🧹 Advanced Data Cleaning Pipeline

A professional Python-based data cleaning and feature engineering pipeline designed to handle messy datasets (inspired by Kaggle competitions). This project demonstrates robust techniques for preparing raw data for machine learning and deep analysis.

## 🚀 Features

- **Automated Data Acquisition**: Integration with common data sources and synthetic generators for testing.
- **Robust Cleaning**:
  - Missing value imputation (Mean, Median, Mode, Zero).
  - Outlier detection and removal using Z-score and Interquartile Range (IQR).
- **Feature Engineering**:
  - Datetime extraction (Year, Month, Day, Weekends).
  - Categorical encoding (One-Hot Encoding).
  - Feature scaling.
- **Trend Discovery & EDA**:
  - Time-series trend analysis.
  - Correlation heatmaps for relationship discovery.
- **Modular Design**: Separated concerns for maintainability and scalability.

## 📂 Project Structure

```text
├── src/
│   ├── data_loader.py         # Data fetching and generation
│   ├── cleaner.py             # Missing values & Outlier logic
│   ├── feature_engineering.py  # Transformations & Encoding
│   ├── trend_discovery.py     # Visualization & Analysis
│   └── main.py                # Pipeline orchestrator
├── requirements.txt           # Dependencies
└── README.md                  # Documentation
```

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/data-cleaning-pipeline.git
   cd data-cleaning-pipeline
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📈 Usage

Run the main pipeline to process example messy data:

```bash
python src/main.py
```

This will generate:
- `cleaned_data.csv`: The final processed dataset.
- `trend_analysis.png`: Visualization of sales trends.
- `correlation_matrix.png`: Statistical overview of feature relationships.

## 📊 Sample Visualizations

The pipeline automatically identifies patterns like:
- Upward/Downward trends in sales.
- Strong correlations between features.
- Anomalies that skew statistical models.



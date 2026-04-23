# 🧹 Production Data Cleaning & Integrity Pipeline
### Advanced Automated ETL for High-Volume Analytical Workflows

This repository implements a production-grade data cleaning and validation framework. It is designed to handle the complexity of real-world datasets—mitigating noise, enforcing data integrity, and engineering features for high-performance machine learning models.

---

## 🚀 Engine Capabilities

- **Automated Validation**: Integrated schema enforcement and data type consistency checks.
- **Advanced Cleaning**:
  - **Intelligent Imputation**: Strategic handling of missing values using distribution-aware logic.
  - **Statistical Outlier Detection**: Implementation of Z-score and IQR filters to eliminate noise.
- **Feature Engineering Engine**:
  - Temporal expansion (Seasonality, Lag features).
  - High-cardinality categorical encoding.
- **Data Governance**: Automated metadata generation and quality reporting.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rohankar02/data-cleaning-pipeline.git
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



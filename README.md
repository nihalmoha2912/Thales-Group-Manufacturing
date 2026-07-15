# Smart Manufacturing Efficiency Classification using Machine Learning

A machine learning project for predicting manufacturing efficiency (High, Medium, Low) using historical production, sensor, and network performance data. The project combines feature engineering, multiple classification models, explainable AI, and an interactive Streamlit dashboard for monitoring factory operations.

---

## Overview

Modern manufacturing plants generate large volumes of operational data from machines and sensors. This project uses that data to classify machine efficiency and provide insights into the factors affecting production performance.

The system helps engineers monitor efficiency, identify performance issues, and make informed operational decisions using explainable machine learning models.

---

## Features

- Manufacturing efficiency classification
- Historical data preprocessing
- Feature engineering
- Multiple machine learning models
- Model comparison
- Explainable AI (Feature Importance & SHAP)
- Prediction confidence scores
- Interactive Streamlit dashboard

---

## Dataset

The dataset contains manufacturing records with the following attributes:

- Date
- Timestamp
- Machine ID
- Operation Mode
- Temperature (°C)
- Vibration (Hz)
- Power Consumption (kW)
- Network Latency (ms)
- Packet Loss (%)
- Quality Control Defect Rate (%)
- Production Output (Units)
- Error Rate (%)
- Efficiency Status (Target)

---

## Project Workflow

```
Raw Manufacturing Data
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Explainability
        │
        ▼
Streamlit Dashboard
```

---

## Data Preprocessing

The preprocessing pipeline includes:

- Combining Date and Timestamp
- Chronological sorting
- Label Encoding categorical variables
- Feature Scaling using StandardScaler
- Class imbalance checking
- Train-Test Split

---

## Feature Engineering

Additional features were created to improve prediction accuracy:

- Sensor Stability Indicator
- Energy Efficiency Ratio
- Error-to-Output Ratio
- Network Reliability Score

---

## Machine Learning Models

### Baseline Model

- Logistic Regression

### Advanced Models

- Random Forest Classifier
- XGBoost Classifier

---

## Model Evaluation

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Feature Importance

---

## Explainable AI

The project includes explainability techniques to improve trust and transparency.

### Feature Importance

Identifies the variables that most influence manufacturing efficiency.

### SHAP

Provides explanations for individual predictions, showing why a machine is classified as:

- High Efficiency
- Medium Efficiency
- Low Efficiency

---

## Streamlit Dashboard

### Dashboard Modules

### Efficiency Prediction

- Efficiency Classification
- Prediction Confidence

### Machine Insights

- Machine-wise Trends
- Historical Performance

### Explainability

- Feature Importance
- SHAP Explanations

### Operational Monitoring

- Efficiency by Operation Mode
- Network Performance Analysis
- Sensor Performance Monitoring

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- SHAP
- Plotly
- Streamlit
- Matplotlib

---

## Project Structure

```
Smart-Manufacturing-Efficiency/
│
├── data/
│   └── Thales_Group_Manufacturing.csv
│
├── notebooks/
│   └── EDA.ipynb
│
├── models/
│   ├── random_forest.pkl
│   ├── xgboost.pkl
│   └── scaler.pkl
│
├── app.py
├── preprocessing.py
├── feature_engineering.py
├── train_model.py
├── explainability.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Smart-Manufacturing-Efficiency.git
```

Move into the project folder

```bash
cd Smart-Manufacturing-Efficiency
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

## Future Improvements

- Real-time IoT sensor integration
- Predictive Maintenance
- Deep Learning models
- Cloud deployment
- Manufacturing Execution System (MES) integration
- Edge AI deployment

---

## Author

**Nihal Mohammed**

M.Sc. Data Science

---

## License

This project is intended for educational and research purposes.

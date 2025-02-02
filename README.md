# House Price Prediction

This project predicts house prices based on features like location, size, number of rooms, and proximity to amenities.

## Dataset
The dataset is sourced from [Kaggle House Prices Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data). It includes features such as:
- `OverallQual`: Overall quality of the house.
- `GrLivArea`: Above-ground living area in square feet.
- `TotalBsmtSF`: Total basement area in square feet.
- `GarageCars`: Garage capacity (number of cars).
- `YearBuilt`: Year the house was built.
- `SalePrice`: Target variable (house price).

## Project Structure
```
house-price-prediction/
├── data/                      # Folder for raw and processed datasets
│   └── train.csv              # Raw dataset from Kaggle
├── notebooks/                 # Jupyter notebooks for EDA and model training
│   ├── eda.ipynb              # Exploratory Data Analysis (EDA)
│   └── model_training.ipynb   # Model training notebook
├── app.py                     # Streamlit app script for making predictions
├── model.pkl                  # Trained machine learning model
├── feature_names.txt          # Feature names used during training
├── requirements.txt           # List of Python dependencies
└── README.md                  # Project description and instructions
```

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/MArbeeGit/house-price-prediction.git
   cd house-price-prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Input house details in the app to get a price prediction.

## Techniques Used
- **Exploratory Data Analysis (EDA)**: Analyzed feature distributions and correlations.
- **Feature Engineering**: Handled missing values and scaled numeric features.
- **Model Training**: Trained a Gradient Boosting Regressor for price prediction.

## Deployment
The app can be deployed on platforms like [Streamlit Cloud](https://streamlit.io/cloud) or Heroku for public access.

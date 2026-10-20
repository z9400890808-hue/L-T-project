
# Mercari Marketplace Product Price Prediction

## Project Overview

This project develops a machine learning system to predict the selling price of products listed on an online marketplace. It uses product information such as the product name, description, category, brand, item condition, and shipping details to estimate the price.

The project covers data exploration, preprocessing, feature engineering, model training, evaluation, model comparison, and price prediction through a Streamlit web application.

## Objectives

- Explore and understand the product dataset.
- Handle missing values and prepare product features.
- Perform exploratory data analysis and visualize price distributions.
- Build a regression model to predict product prices.
- Evaluate model performance using regression metrics.
- Save the trained model and use it for new predictions.
- Provide a simple interface for users to enter product details and obtain an estimated price.

## Dataset

The project uses the Mercari marketplace `train.tsv` dataset.

The notebook loads the first 10,000 rows for the main analysis and model development.

The target variable is `price`. The input features include product text, category, brand, item condition, and shipping information.

Note: The dataset is not included in this repository. Place `train.tsv` in the project folder before running the notebook.

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- TF-IDF text vectorization
- One-Hot Encoding
- Ridge Regression
- Joblib
- MLflow
- Streamlit
- Jupyter Notebook

## Machine Learning Approach

The project uses Ridge Regression as the main price prediction model.

Text information is processed using TF-IDF vectorization, while categorical features are encoded using One-Hot Encoding. Missing values in applicable features are handled during preprocessing.

The model uses a log transformation of the target price to help manage its skewed distribution. Model performance is evaluated using metrics such as:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)
- Root Mean Squared Logarithmic Error (RMSLE)

The notebook also compares Ridge Regression with other regression approaches.

## Project Files

- `Mercari_Product_Price_Prediction_Final.ipynb` — Notebook containing data analysis, preprocessing, model training, evaluation, and experimentation.
- `app.py` — Streamlit application for product price prediction.
- `requirements.txt` — Python dependencies required by the project.
- `mercari_price_model.pkl` — Saved trained model.
- `final_metrics.json` — Saved model evaluation metrics.
- `model_comparison.csv` — Model performance comparison.
- `prediction_results.csv` — Prediction results, if generated.
- `batch_predictions.csv` — Batch prediction results, if generated.

Some output files may be generated when the notebook is executed.

## Installation and Setup

1. Install Python on your computer.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Install the required libraries:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Place the `train.tsv` dataset in the project folder if you want to rerun the notebook.
6. Open the notebook using Jupyter:

   ```bash
   jupyter notebook
   ```

7. Open `Mercari_Product_Price_Prediction_Final.ipynb` and run the cells in order.

## Running the Web Application

Make sure `app.py` and the saved model file `mercari_price_model.pkl` are in the same project folder.

Run:

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the application.

## Limitations

- The main notebook analysis uses a 10,000-row sample rather than the complete training dataset.
- Predicted prices are estimates and may differ from actual marketplace prices.
- Prediction quality depends on the available product information and the model's training data.
- Results from a sample dataset may not represent the entire marketplace.

## Future Improvements

- Train and evaluate the model using a larger dataset.
- Improve text feature engineering and model tuning.
- Explore additional regression algorithms.
- Improve the user interface and add batch prediction support.
- Evaluate model performance on unseen marketplace data.

## Conclusion

This project demonstrates an end-to-end machine learning workflow for marketplace product price prediction, from data analysis and feature preparation to model evaluation and deployment through a web application.

# Phishing Detection System

This program is a machine learning REST API that detects phishing websites using a Random Forest classifier trained on the UCI Phishing Websites dataset.


## Model Performance
- Accuracy: 98.2%
- Precision: 0.98
- Recall: 0.98
- F1-Score: 0.98

## Project Structure
- `explore.py` — explores and understands the dataset
- `preprocess.py` — cleans and splits the data
- `train.py` — trains and saves the model
- `app.py` — deploys the model as a REST API
- `test_api.py` — tests the API

## How to Run

Install dependencies:
pip install pandas scikit-learn flask joblib requests

Train the model:
python train.py

Start the API:
python app.py

Test the API:
python test_api.py

## Dataset
UCI Phishing Websites Dataset — 10,000 websites, 48 features, perfectly balanced classes.
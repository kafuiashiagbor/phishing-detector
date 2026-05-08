import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess():
    df = pd.read_csv("Phishing_Legitimate_full.csv")
    df = df.drop(columns=["id"])
    X = df.drop(columns=["CLASS_LABEL"])
    y = df["CLASS_LABEL"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test
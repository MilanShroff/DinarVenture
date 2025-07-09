import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay,
)


def load_data():
    
    iris = load_iris(as_frame=True)
    df = iris.frame
    X = df[iris.feature_names]
    y = df["target"]
    target_names = iris.target_names
    return X, y, target_names


def train_model(X_train, y_train):
    
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test, target_names):
    
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy: {accuracy:.4f}\n")

    print(" Classification Report:\n")
    print(classification_report(y_test, y_pred, target_names=target_names))

    
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
    disp.plot(cmap="Blues")
    plt.title("Confusion Matrix")
    plt.show()


def main():
   
    X, y, target_names = load_data()

    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    
    model = train_model(X_train, y_train)

  
    evaluate_model(model, X_test, y_test, target_names)


if __name__ == "__main__":
    main()

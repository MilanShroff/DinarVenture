
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = datasets.load_iris()

X = iris.data       
y = iris.target     

print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)
print("\nFirst 5 samples:\n", X[:5])
print("First 5 labels:\n", y[:5])


df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y
print("\nDataFrame head:\n", df.head())


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining samples:", X_train.shape)
print("Testing samples:", X_test.shape)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)


y_pred = model.predict(X_test_scaled)
print("\nPredictions:", y_pred)
print("True labels:", y_test)


accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", cm)

print("\nClassification Report:\n", classification_report(y_test, y_pred))

import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def connect_to_mysql():
    return mysql.connector.connect(
        host="",
        user="",
        password="",
        database="sneakers_db"
    )

def fetch_data():
    connection = connect_to_mysql()
    cursor = connection.cursor()
    query = "SELECT brand, location, `condition`, price FROM sneakers"
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=["brand", "location", "`condition`", "price"])
    cursor.close()
    connection.close()
    return df


df = fetch_data()

X = df[["brand", "location", "`condition`"]]
y = df["price"]

categorical_features = ["brand", "location", "`condition`"]


preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



X_train_transformed = preprocessor.fit_transform(X_train)
X_test_transformed = preprocessor.transform(X_test)

model = LinearRegression()
model.fit(X_train_transformed, y_train)

y_pred = model.predict(X_test_transformed)
mse_lr = mean_squared_error(y_test, y_pred)
r2_lr = r2_score(y_test, y_pred)

print(f"Coefficient (slope): {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")
print(f"Linear Regression — MSE: {mse_lr:.2f}, R²: {r2_lr:.2f}")

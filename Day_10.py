import pandas as pd
import pickle 
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score


df = pd.read_csv(r'C:\Users\milan\OneDrive\Desktop\PS_20174392719_1491204439457_log.csv')


print("DV06AI00020\n")
X = df[["type", "amount", "oldbalanceOrg", "newbalanceOrig", 
        "oldbalanceDest", "newbalanceDest"]]
y = df["isFraud"]


categorical_features = ["type"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ],
    remainder='passthrough'
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_train_transformed = preprocessor.fit_transform(X_train)
X_test_transformed = preprocessor.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_transformed, y_train)

y_pred = model.predict(X_test_transformed)

with open ('model.pkl','wb') as f:
    pickle.dump((preprocessor,model),f)
print("Model is saved as 'model.pkl'")

with open('model.pkl','rb') as f:
    loaded_preprocessor,loaded_model = pickle.load(f)

X_test_loaded = loaded_preprocessor.transform(X_test)
y_pred_loaded = loaded_model.predict(X_test_loaded)

print(f"Accuracy: {accuracy_score(y_test, y_pred_loaded):.2f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred_loaded))

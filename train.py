import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset 
df = pd.read_csv("alzheimers_disease_data.csv")

# Keep numeric columns
df = df.select_dtypes(include=['number'])

X = df.drop("Diagnosis", axis=1)
y = df["Diagnosis"]

X = df.drop("Diagnosis", axis=1)
y = df["Diagnosis"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "alz_model.pkl")
print("Model saved")




import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# 🔹 Get the absolute path of the dataset
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_behavior.csv")

# 🔹 Load dataset
data = pd.read_csv(file_path)

# 🔹 Display the first few rows to verify data
print("Dataset Loaded Successfully!")
print(data.head())

# 🔹 Prepare data for training
X = data.drop(columns=["threat_status"])
y = data["threat_status"].map({"Normal": 0, "Threat": 1})  # Fixed mapping

# 🔹 Train ML Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 🔹 Save the trained model
joblib.dump(model, os.path.join(os.path.dirname(__file__), "insider_threat_model.pkl"))

print("Model Training Completed & Saved as 'insider_threat_model.pkl'")

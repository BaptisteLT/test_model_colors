import os
import numpy as np
import pandas as pd
import joblib
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load color data from CSV
csv_filename = "colors.csv"
df = pd.read_csv(csv_filename, header=None, names=["id", "name", "hex", "r", "g", "b"])

# Extract features (RGB values) and labels (color names)
X = df[["r", "g", "b"]].values  # Features: RGB values
y = df["name"].values           # Labels: Color names

# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "color_model.pkl")

# Test model accuracy
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

print("Model trained and saved as 'color_model.pkl'.")

import pandas as pd
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras

#Convert model tensorflow to js using tensorflowjs_converter --input_format keras color_model_tensorflow.h5 color_model_tensorflow_js




# Load dataset
df = pd.read_csv("colors.csv", header=None, names=["id", "name", "hex", "r", "g", "b"])

# Features (RGB values) and labels (color names)
X = df[["r", "g", "b"]].values / 255.0  # Normalize RGB values
y = df["name"].astype("category").cat.codes  # Convert labels to numbers

# Save label mapping for later use in JS
label_mapping = dict(enumerate(df["name"].astype("category").cat.categories))
np.save("label_mapping.npy", label_mapping)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a simple neural network model
model = keras.Sequential([
    keras.layers.Dense(16, activation="relu", input_shape=(3,)),  # RGB input
    keras.layers.Dense(16, activation="relu"),
    keras.layers.Dense(len(label_mapping), activation="softmax")  # Output for color classification
])

# Compile the model
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=4, validation_data=(X_test, y_test))

# Save the model in TensorFlow.js format
model.save("color_model_tenserflow.h5")

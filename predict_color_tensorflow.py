import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model("color_model_tenserflow.h5")  # Make sure this path matches your saved model

# Load label mapping (color names)
label_mapping = np.load("label_mapping.npy", allow_pickle=True).item()

def get_dominant_color(image_path):
    """Extract the most dominant color from an image."""
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure it's in RGB mode
    img = img.resize((1, 1))  # Resize to 1x1 pixel
    r, g, b = img.getpixel((0, 0))
    return r / 255.0, g / 255.0, b / 255.0  # Normalize

def predict_color_from_image(image_path):
    """Predict the color name from an image using the TensorFlow model."""
    r, g, b = get_dominant_color(image_path)

    # Prepare input for the model
    input_data = np.array([[r, g, b]], dtype=np.float32)

    # Predict color
    prediction = model.predict(input_data)
    predicted_index = np.argmax(prediction)  # Get index of highest probability

    return label_mapping[predicted_index], (r * 255, g * 255, b * 255)  # Return color name and RGB

# Example usage
image_path = "./samples/sample1_blue.png"  # Change to your image path
predicted_color, rgb_values = predict_color_from_image(image_path)
print(f"Predicted Color: {predicted_color} (RGB: {rgb_values})")

# Example usage
image_path = "./samples/sample2_red.png"  # Change to your image path
predicted_color, rgb_values = predict_color_from_image(image_path)
print(f"Predicted Color: {predicted_color} (RGB: {rgb_values})")

# Example usage
image_path = "./samples/sample3_gold.png"  # Change to your image path
predicted_color, rgb_values = predict_color_from_image(image_path)
print(f"Predicted Color: {predicted_color} (RGB: {rgb_values})")

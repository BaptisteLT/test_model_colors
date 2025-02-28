import joblib
from PIL import Image


# Load trained model
model = joblib.load("color_model.pkl")

def get_dominant_color(image_path):
    """Extract the most dominant color from an image."""
    img = Image.open(image_path)
    img = img.convert("RGB")  # Ensure it's in RGB mode
    img = img.resize((1, 1))  # Resize to 1x1 pixel
    r, g, b = img.getpixel((0, 0))
    return r, g, b

def predict_color_from_image(image_path):
    """Predict the color name from an image."""
    r, g, b = get_dominant_color(image_path)
    predicted_color = model.predict([[r, g, b]])[0]
    return predicted_color, (r, g, b)

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

# Create API of ML model using flask

# Import libraries
import os
from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np

# Create upload file path

upload_folder = "static/upload"
temp = "model/"

# Create an app
app = Flask(__name__)
app.config['upload_folder'] = upload_folder

# Load the model
#model_path = os.path.abspath("model/microP.h5")
#model = load_model(model_path)
#model = load_model(model_path)
model = tf.keras.models.load_model("model/saved_model")




@app.route('/')
def home():
    return render_template("index.html")


def preprocess_image(image_path):
    # Read the image using OpenCV
    image = Image.open(image_path).convert("RGB")

    # print("Image Channels (PIL):", image.mode)
    # print("Image Shape (PIL):", np.array(image).shape)

    # Resize the image to (150, 150)
    image = tf.image.resize(image, (128, 128))

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Normalize the image
    image_array = image_array / 255.0  # Assuming pixel values are in the range [0, 255]

    image_array = np.transpose(image_array, (0, 1, 2))

    # Add batch dimension
    image_array = np.expand_dims(image_array, axis=0)

    image_tensor = tf.convert_to_tensor(image_array, dtype=tf.float32)

    return image_tensor

@app.route('/predict',methods=['POST','GET'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
        if 'exp' not in request.files:
            return 'No File!'
        file = request.files['exp']

        path = os.path.join(app.config['upload_folder'],file.filename)
        file.save(path)

        print("Path:",path)

        input_data = preprocess_image(path)
        predictions = model.predict(input_data)

        binary_predictions = (predictions > 0.5).astype(int)

        class_predict = "Clean" if binary_predictions == 0 else "Microplastics"

        return render_template("results.html", image_path=path, class_predict=class_predict)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=5001)

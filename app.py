# Create API of ML model using flask

# Import libraries
import os
from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from skimage.color import rgb2gray
from skimage.transform import resize
from PIL import Image
import numpy as np

# Create upload file path
upload_folder = "static/upload"
temp = "model/"

# Create an app
app = Flask(__name__,static_url_path='/static')
app.config['upload_folder'] = upload_folder
#app.config['UPLOAD_FOLDER'] = 'static/upload'


# Load the model
model = tf.keras.models.load_model("model/saved_model")




@app.route('/')
def home():
    return render_template("index.html")

def preprocess_input_for_prediction(image_path):
    image = load_img(image_path, target_size=(128, 128))
    image_array = img_to_array(image)
    image_array = preprocess_input(image_array)
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

#     return image_array
# def preprocess_image(image_path):
#     # Read the image using OpenCV
#     image = Image.open(image_path).convert("RGB")

#     # print("Image Channels (PIL):", image.mode)
#     # print("Image Shape (PIL):", np.array(image).shape)

#     # Resize the image to (150, 150)
#     image = tf.image.resize(image, (128, 128))

#     # Convert the image to a NumPy array
#     image_array = np.array(image)

#     # Normalize the image
#     image_array = image_array / 255.0  # Assuming pixel values are in the range [0, 255]

#     image_array = np.transpose(image_array, (0, 1, 2))

#     # Add batch dimension
#     image_array = np.expand_dims(image_array, axis=0)

#     image_tensor = tf.convert_to_tensor(image_array, dtype=tf.float32)

#     return image_tensor

@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
        if 'exp' not in request.files:
            return 'No File!'
        file = request.files['exp']

        path = os.path.join("static/upload", file.filename)
        #path = os.path.join(app.config['upload_folder'],file.filename)
        file.save(path)

        input_data = preprocess_input_for_prediction(path) 

        predictions = model.predict(input_data)
        print("Raw Predictions:", predictions)

        binary_predictions = (predictions > 0.5).astype(int)
   
        class_predict = "Clean" if binary_predictions == 0 else "Microplastics"

        result = {
            "class_predict": class_predict,
            "binary_predictions": binary_predictions.flatten().tolist(),
            "predictions": predictions.flatten().tolist(),
            "image_path": path
        }

        return render_template("results.html", image_path=path, class_predict=class_predict, binary_predictions=binary_predictions, predictions=predictions)
        return jsonify(result)
    
    #return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,port=5001)

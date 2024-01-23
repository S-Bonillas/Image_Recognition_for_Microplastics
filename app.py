# Create API of ML model using flask

# Import libraries
import os
from flask import Flask, render_template, request, url_for, redirect, flash, jsonify
import pickle

# Create upload file path

upload_folder = "static/upload"

# Create an app
app = Flask(__name__)
app.config['upload_folder'] = upload_folder

# Load the model
#model = pickle.load(open('./model.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")


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

        return render_template("results.html", image_path=path)

if __name__ == '__main__':
    app.run(debug=True,port=5001)

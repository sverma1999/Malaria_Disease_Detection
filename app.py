from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
# from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.applications.vgg19 import preprocess_input
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
#from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
# MODEL_PATH = 'saved_models/model_vgg19.h5'

# Get the absolute path to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

model_version = max([int(i) for i in os.listdir(
    "saved_models") if i != '.DS_Store'] + [0])

print("Using model version: ", model_version)
# Construct the path to the model file using the script's directory
# model_path = os.path.join(script_dir, "../saved_models/1")
# model_path = os.path.join(script_dir, "../idg_models/1/peppermodel.h5")
model_path = os.path.join(
    script_dir, f"saved_models/{model_version}/model_vgg19.h5")


# Load your trained model
model = load_model(model_path)

CLASS_NAMES = ["Parasitized", "Uninfected"]


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    # Scaling
    x = x/255
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x)

    predictions = model.predict(x)
    index = np.argmax(predictions[0])
    predicted_class = CLASS_NAMES[index]
    confidence = np.max(predictions[0])

    print("predictions index: ", index)
    print(predicted_class, confidence)

    # print("preds before argmax: ", preds)
    # preds = np.argmax(preds, axis=1)
    # print("preds after argmax and before condition: ", preds)

    preds = ""
    if index == 0:
        preds = "The Person is Infected With Malaria"
    else:
        preds = "The Person is not Infected With Malaria"

    return preds

# def model_predict(img_path, model):
#     img = image.load_img(img_path, target_size=(224, 224))

#     # Preprocessing the image
#     x = image.img_to_array(img)
#     x = x/255
#     x = np.expand_dims(x, axis=0)

#     # Be careful how your trained model deals with the input
#     # otherwise, it won't make correct prediction!
#     x = preprocess_input(x)

#     preds = model.predict(x)
#     #preds = np.argmax(preds, axis=1)
#     # preds = preds[0]  # extract the prediction value from the array
#     print(preds)
#     if preds[0] < 0.5:
#         preds = "The Person is Infected With Malaria"
#     else:
#         preds = "The Person is not Infected With Malaria"

#     return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    print("Request.method = ", request.method)
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        print("file_path:  ", file_path)
        print("model:  ", model)
        # Make prediction
        preds = model_predict(file_path, model)
        print("Done prediction..... ", preds)
        result = preds
        return result
    return None


if __name__ == '__main__':
    # app.run(debug=True)

    # Serving the app on local host: http://localhost:3000/
    app.run(host="0.0.0.0", port=3000)

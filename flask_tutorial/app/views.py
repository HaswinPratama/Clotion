import os
import cv2
#from app.face_recognition import faceRecognitionPipeline
from flask import render_template, request


UPLOAD_FOLDER = "static/upload"

def index():
    return render_template("index.html")

def app():
    return render_template("app.html")

def landing():
    return render_template("landing.html")

def page():
    return render_template("page.html")

def segmentation():
    return render_template("segmentation.html")

def clotion():
    if request.method == "POST":
        f = request.files["image_name"]
        filename = f.filename
        # save our image in upload folder
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path) # save image into upload folder
        # get predictions
        #pred_image, predictions = faceRecognitionPipeline(path)
        pred_filename = "prediction_image.jpg"
        #cv2.imwrite(f"./static/predict/{pred_filename}", pred_image)

        print("ML model predicted successfully")

    return render_template("clotion.html") #GET REQUEST
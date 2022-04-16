import os
from flask import Flask, render_template
from modes.Image.image import image
from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright


UPLOAD_IMAGE_FOLDER = 'modes\\Image\\static'
IMAGE_CACHE_FOLDER = 'modes\\Image\\__pycache__'


app = Flask(__name__)
app.secret_key = 'hello'
app.config['UPLOAD_IMAGE_FOLDER'] = UPLOAD_IMAGE_FOLDER
app.config['IMAGE_CACHE_FOLDER'] = IMAGE_CACHE_FOLDER


app.register_blueprint(image, url_prefix="/image")


@app.route("/")
def home():
    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
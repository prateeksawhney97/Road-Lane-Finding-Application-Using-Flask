from flask import *  

import pandas as pd
import numpy as np
import os

import pickle
import cv2
import glob

IMAGE_FOLDER = 'static/'
PROCESSED_FOLDER = 'processed/'
#IMAGE_FOLDER = os.path.join('upload', 'images')


app = Flask(__name__)  
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER


@app.route('/')  
def upload():
	return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])
def success():
	if request.method == 'POST':
		f = request.files['file']
		#hls = (np.float32(image), cv2.COLOR_RGB2HLS)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
		#print(f.filename)
		full_filename = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
		#filepath = os.path.join(app.config['imgdir'], filename);
		#file.save(filepath)
		image_ext = cv2.imread(full_filename)
		hls = cv2.cvtColor(image_ext, cv2.COLOR_RGB2HLS)
		hls_name = 'sample.jpg'
		cv2.imwrite('static/'+hls_name, hls)
		full_filename_processed = os.path.join(app.config['UPLOAD_FOLDER'], hls_name)		
		#full_filename_processed = os.path.join(app.config['PROCESSED_FOLDER'], hls_name)
		hls_final_name = 'Resultant Image after Detecting Lane Area'
		#return render_template("success.html", name = f.filename, img = full_filename)
		return render_template("success.html", name = hls_final_name, img = full_filename_processed)
		#return render_template("success.html", name=hls_final_name)

@app.route('/predict', methods = ['POST'])
def predict():
	if request.method == 'POST':
		return render_template("abc.html")

@app.route('/result', methods = ['POST'])
def result():
	if request.method == 'POST':
		return render_template("result.html")


if __name__ == '__main__':  
	app.run(host="127.0.0.1",port=8080,debug=True)  







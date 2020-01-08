from flask import *  

import pandas as pd
import numpy as np
import os

import pickle
import cv2
import glob

from random import randint

IMAGE_FOLDER = 'static/'
PROCESSED_FOLDER = 'static/processed/'
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
		i = randint(1, 1000000)
		char = str(i)
		hls_name = 'sample_'+char+'.jpg'
		cv2.imwrite('static/processed/'+hls_name, hls)
		full_filename_processed = os.path.join(app.config['PROCESSED_FOLDER'], hls_name)		
		final_text = 'Results after Detecting Lane Area over Input Image'
		return render_template("success.html", name = final_text, img_in = full_filename, img = full_filename_processed)
		

@app.route('/info', methods = ['POST'])
def info():
	if request.method == 'POST':
		return render_template("info.html")



if __name__ == '__main__':  
	app.run(host="127.0.0.1",port=8080,debug=True)  







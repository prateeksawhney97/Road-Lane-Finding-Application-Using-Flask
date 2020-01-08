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
		initial_image = np.copy(image_ext)

		objp = np.zeros((6*9,3), np.float32)
		objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

		# Arrays to store object points and image points from all the images.
		objpoints = [] # 3d points in real world space
		imgpoints = [] # 2d points in image plane.

		# Make a list of calibration images
		images_for_calibration = glob.glob('camera_cal/calibration*.jpg')

		# Step through the list and search for chessboard corners
		for f_name in images_for_calibration:
	    		img_read = cv2.imread(f_name)
    			gray = cv2.cvtColor(img_read,cv2.COLOR_BGR2GRAY)

    			# Find the chessboard corners
    			ret, corners = cv2.findChessboardCorners(gray, (9,6),None)

    			# If found, add object points, image points
    			if ret == True:
        			objpoints.append(objp)
        			imgpoints.append(corners)


		ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, initial_image.shape[1::-1], None, None)
		undistorted = cv2.undistort(initial_image, mtx, dist, None, mtx)
		hls = cv2.cvtColor(undistorted, cv2.COLOR_RGB2HLS)
		s_channel = hls[:,:,2]
		gray = cv2.cvtColor(undistorted, cv2.COLOR_RGB2GRAY)		
		
		hls = gray
		


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







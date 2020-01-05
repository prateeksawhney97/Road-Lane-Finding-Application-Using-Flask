from flask import *  
UPLOAD_FOLDER = '/home/prateeksawhney97/Documents/Advance-Lane-Flask-Application/upload/'

import pandas as pd
import numpy as np
import os


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


app = Flask(__name__)  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')  
def upload():
	return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])
def success():
	if request.method == 'POST':
		f = request.files['file']
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
		return render_template("success.html", name = f.filename)

@app.route("/predict", methods=['POST'])
def predict():
	return render_template("abc.html")


if __name__ == '__main__':  
	app.run(host="127.0.0.1",port=8080,debug=True)  







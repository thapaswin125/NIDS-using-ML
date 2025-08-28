from flask import Flask, render_template, redirect, url_for, request,session,Response
from werkzeug import secure_filename
import os
import cv2
import pickle
from sklearn.ensemble import RandomForestClassifier
from preprocessing import *

app = Flask(__name__)

app.secret_key = '1234'
app.config["CACHE_TYPE"] = "null"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/', methods=['GET', 'POST'])
def landing():
	return render_template('home.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template('home.html')


@app.route('/input', methods=['GET', 'POST'])
def input():	
	if request.method == 'POST':
		packet = 	Convert(request.form['packet'])
		test_df = [float(i) for i in packet]
		result = predict([test_df])
		print(result)
		return render_template('input.html',result1=result[0],result2=result[1],result3=result[2])


	return render_template('input.html')

@app.route('/train', methods=['GET', 'POST'])
def train():
	KNN_accuracy,KNN_accuracy1,BNB_accuracy,BNB_accuracy1,DTC_accuracy,DTC_accuracy1 = train_model()
	result1 = "Train Accuracy: "+ str(KNN_accuracy) + "%, " + "Test Accuracy: " + str(KNN_accuracy1) + "%"
	result2 = "Train Accuracy: "+ str(BNB_accuracy) + "%, " + "Test Accuracy: " + str(BNB_accuracy1) + "%"	
	result3 = "Train Accuracy: "+ str(DTC_accuracy) + "%, " + "Test Accuracy: " + str(DTC_accuracy1) + "%"

	return render_template('train.html',result1=result1,result2=result2,result3=result3)		





# No caching at all for API endpoints.
@app.after_request
def add_header(response):
	# response.cache_control.no_store = True
	response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
	response.headers['Pragma'] = 'no-cache'
	response.headers['Expires'] = '-1'
	return response


if __name__ == '__main__' and run:
	app.run(host='0.0.0.0', debug=True, threaded=True)

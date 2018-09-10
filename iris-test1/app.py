# import Flask class from the flask module
from flask import Flask, request, jsonify

import numpy as np
import pickle

# Create Flask object to run
app = Flask(__name__)

global svmIrisModel
svmIrisFile = open('model/SVMModel.pckl', 'rb')
svmIrisModel = pickle.load(svmIrisFile)
svmIrisFile.close()

@app.route("/")
def home():
    return "Hi, Welcome to Flask!!"


@app.route("/predict")
def predict():
	# Get values from browser
	sepLen = request.args['sepal_length']
	sepWid = request.args['sepal_width']
	petLen = request.args['petal_length']
	petWid = request.args['petal_width']
	
	testData = np.array([sepLen, sepWid, petLen, petWid]).reshape(1,4)
	try:
		class_prediced = int(svmIrisModel.predict(testData)[0])
		output = "Predicted Iris Class: " + str(class_prediced)
	except Exception as e:
		print(e)
	#return (output)
	print (jsonify(results=output))
	return jsonify(results=output)

	
# Load the pre-trained and persisted SVM model
# Note: The model will be loaded only once at the start of the server


if __name__ == "__main__":
	print("**Starting Server...")
	
	# Call function that loads Model
	#predict()
	
	# Run Server
	app.run()


# Create Flask object to run
#app = Flask(__name__)

#@app.route("/")
#def home():
#    return "Hi, Welcome to Flask!!"
#
#if (__name__ == "__main__"):
#    print("**Starting Server...")
    # Run Server
#    app.run(port = 5000)

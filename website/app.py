from flask import Flask, render_template, request
import pickle
import numpy as np

# Setup application
app = Flask(__name__)

# Load model once
model = None
def load_model():
    global model
    filename = 'model/predictor.pkl'
    try:
        with open(filename, 'rb') as file:
            model = pickle.load(file)
    except FileNotFoundError:
        print("Model file not found. Ensure 'predictor.pkl' exists.")

load_model()

# Prediction function
def prediction(lst):
    try:
        pred_value = model.predict([lst])
        return pred_value[0]
    except Exception as e:
        print(f"Prediction error: {e}")
        return "Error"

@app.route('/', methods=['POST', 'GET'])
def index():
    pred_value = None
    if request.method == 'POST':
        try:
            # Collect and process form data
            feature_list = [
                int(request.form['age']),
                float(request.form['bp']),
                float(request.form['sg']),
                int(request.form['al']),
                float(request.form['su']),
                1 if request.form['rbc'] == 'abnormal' else 0,
                1 if request.form['pc'] == 'abnormal' else 0,
                1 if request.form['pcc'] == '1' else 0,
                1 if request.form['ba'] == '1' else 0,
                float(request.form['bgr']),
                float(request.form['bu']),
                float(request.form['sc']),
                int(request.form['sod']),
                float(request.form['pot']),
                float(request.form['hemo']),
                int(request.form['pcv']),
                int(request.form['wbcc']),
                float(request.form['rbcc']),
                1 if request.form['htn'] == '1' else 0,
                1 if request.form['dm'] == '1' else 0,
                1 if request.form['cad'] == '1' else 0,
                1 if request.form['appet'] == '1' else 0,
                1 if request.form['pe'] == '1' else 0,
                1 if request.form['ane'] == '1' else 0
            ]
            pred_value = prediction(feature_list)
        except Exception as e:
            print(f"Form processing error: {e}")
            pred_value = "Error"
    
    return render_template('index.html', pred_value=pred_value)



    

if __name__ == '__main__':
    app.run(debug=True) 
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 12:38:13 2021

@author: Thomas M Thoppil
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import lightgbm as lgb
app = Flask(__name__)

model = lgb.Booster(model_file='mode.txt')

@app.route('/')
def welcome():
    return render_template("index.html")


@app.route('/predict', methods = ['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features).round(0)

    if int(prediction[0]) == 1:
        output = 'legitimate'
    else:
        output = 'illegitmate'

    return render_template('index.html', prediction_text=f'The predicted score is {prediction[0]} and hence the file is {output}')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))]).round(0)

    output = prediction[0]
    return jsonify(output)

    
    
if __name__ == '__main__':
    app.run()

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 03:07:03 2021

@author: Thomas M Thoppil
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import lightgbm as lgb

model = lgb.Booster(model_file='lightGBMModel.txt')
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    legitimacy = model.predict(final_features).round(0)
    if legitimacy[0] == 0:
        output = 'The file is illegitimate'
    else:
        output = 'The file is legitimate'
    return render_template('index.html', prediction_text = output)

if __name__ == '__main__':
    app.run()
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 03:07:03 2021

@author: Thomas M Thoppil
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    return render_template('index.html', prediction_text = 'lol')

if __name__ == '__main__':
    app.run()
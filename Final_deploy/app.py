# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:27:08 2022

@author: rohit
"""

import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model_M01AB = pickle.load(open('model_M01AB.pkl', 'rb'))
model_M01AE = pickle.load(open('model_M01AE.pkl', 'rb'))
model_MR06 = pickle.load(open('model_MR06.pkl', 'rb'))
model_N02BA = pickle.load(open('model_N02BA.pkl', 'rb'))
model_N02BE = pickle.load(open('model_N02BE.pkl', 'rb'))
model_N05B = pickle.load(open('model_N05B.pkl', 'rb'))
model_N05C = pickle.load(open('model_N05C.pkl', 'rb'))
model_R03 = pickle.load(open('model_R03.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''    
    start_date=request.form.get('start_date')
    period=request.form.get('period')
    period = int(period)
    
    pred_date_range = pd.date_range(start=str(start_date),periods= period)
    pred_df = pd.DataFrame({ 'ds' : pred_date_range})

    # Prediction for all drugs.
    # prediction = model.predict(pred_date_range)
    pred_M01AB   = model_M01AB.predict(pred_df)
    pred_M01AE   = model_M01AE.predict(pred_df)
    pred_R06     = model_MR06.predict(pred_df)
    pred_N02BA   = model_N02BA.predict(pred_df)
    pred_N02BE   = model_N02BE.predict(pred_df)
    pred_N05B    = model_N05B.predict(pred_df)
    pred_N05C    = model_N05C.predict(pred_df)
    pred_R03     = model_R03.predict(pred_df) 

    prediction = pd.DataFrame({'Sr_No': range(1, period+1),'Date' :pred_date_range, 'pred_M01AB':round(pred_M01AB.yhat, 2),'pred_M01AE':round(pred_M01AE.yhat, 2), 'pred_R06':round(pred_R06.yhat, 2), 'pred_N02BA':round(pred_N02BA.yhat, 2), 'pred_N02BE':round(pred_N02BE.yhat, 2), 'pred_N05B':round(pred_N05B.yhat, 2), 'pred_N05C':round(pred_N05C.yhat, 2), 'pred_R03':round(pred_R03.yhat, 2)})
    headings = prediction.columns
    data = []
    for index, rows in prediction.iterrows():
        my_list = [rows.Sr_No, rows.Date, rows.pred_M01AB, rows.pred_M01AE, rows.pred_R06, rows.pred_N02BA, rows.pred_N02BE, rows.pred_N05B, rows.pred_N05C, rows.pred_R03]
        data.append(my_list)
    
    


    return render_template('table.html',headings=headings, data=data)


if __name__ == "__main__":
    app.run(debug=True)
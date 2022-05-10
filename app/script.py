# libraries!
try:
    from flask import render_template, redirect, url_for, request, send_from_directory, flash
except:
    print("Not able to import all of the calls needed from the Flask library.")

import numpy as np      # numpy is Python's "array" library
import pandas as pd     # Pandas is Python's "data" library ("dataframe" == spreadsheet)
import pickle
from app import app

# Home page, renders the index.html template
@app.route('/index')
@app.route('/')
def index():
    return render_template('new_index.html', title='Home')

# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 13)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    print(f"result: {result}")
    return result[0]
 
@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        print(to_predict_list)
        result = ValuePredictor(to_predict_list)  
        result = int(result)     
        if result == 0:
            prediction ="You've matched with Full Cellar Farm"
        elif result == 1:
            prediction ="You've matched with Good Rain Farm"  
        elif result == 2:
            prediction ="You've matched with Lil Starts Farm"    
        elif result == 3:
            prediction ="You've matched with Three Goats Farm"
        elif result == 4:
            prediction ="You've matched with The Side Yard Farm" 
        elif result == 5:
            prediction ="You've matched with Sun Love Farm" 
        elif result == 6:
            prediction ="You've matched with Kasama Farm"
        elif result == 7:
            prediction ="You've matched with PK Pastures"
        elif result == 8:
            prediction ="You've matched with Totum Farm"
        elif result == 9:
            prediction ="You've matched with Stoneboat Farm"
        else:
            prediction = "I'm sorry we do not currently have a good match for you."                                  
        return render_template("result.html", prediction = prediction)
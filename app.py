import flask
from flask import Flask, request, render_template, jsonify
import numpy as np
from tensorflow.keras.models import load_model, save_model
import matplotlib.pyplot as plt
import numpy
import pandas as pd



# json_file = open("model.json", "r") 
# loaded_model = json_file.read() 
# json_file.close() 

# model = model_from_json(loaded_model)



# Flask 애플리케이션과 Keras 모델을 초기화합니다.
app = Flask(__name__)


@app.route('/') 
@app.route('/index')
def index():
    return "모델 불러오기 완료"
    # return flask.render_template(model)


@app.route('/predict', methods = ['POST'])  
def predict():
#     data = {"success": False}

#     return flask.jsonify(data)
    if request.method == 'POST':
        return render_template('hello.html')

    

@app.route('/environments/<language>')  
def environments(language):  
     return jsonify({"language":language}) #받아온 데이터 다시 전송 

if __name__== '__main__': # 모델로드
    
    model = load_model('model.h5')
    app.run(debug = True)



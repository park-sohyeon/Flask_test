# import flask
# from flask import Flask, request, render_template, jsonify
# import sklearn.externals
# import joblib
# import numpy as np
# from scipy import misc

# # Flask 애플리케이션과 Keras 모델을 초기화합니다.
# app = Flask(__name__)


# @app.route('/') 
# @app.route('/index')
# def index():
#     return flask.render_template("hello.html")



# @app.route('/predict', methods = ['POST'])  
# def predict():
#     data = {"success": False}

#     return flask.jsonify(data)
#     #if request.method == 'POST':
#         #return render_template('hello.html')

    

# @app.route('/environments/<language>')  
# def environments(language):  
#      return jsonify({"language":language}) #받아온 데이터 다시 전송 

# if __name__== '__main__': # 모델로드
   
#     model = joblib.load('model.h5')
#     app.run(debug = True)

from flask import Flask, render_template, jsonify
from flask.globals import request


app = Flask(__name__)


@app.route('/')  
def hello_world():
    print(__name__)
    return render_template("hello.html")

@app.route('/userLogin', methods = ['POST'])  
def userLogin():
    user = request.get_json() #json 데이터를 받아옴
    return jsonify(user) #받아온 데이터 다시 전송

@app.route('/environments/<language>') 
def environments(language):  
    return jsonify({"language":language}) #받아온 데이터 다시 전송 

if __name__== '__main__':
    app.run(debug = True)



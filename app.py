from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import flask
import io

# Flask 애플리케이션과 Keras 모델을 초기화합니다.
app = flask.Flask(__name__)
model = None


app = Flask(__name__)


@app.route('/') 
@app.route('/index')
def index():
    return flask.render_template("hello.html")

@app.route("/exam") # 접속 ip혹은 도메인 뒤 붙는 라우터 이름
def predict():
    #test_datagen = ImageDataGenerator(rescale=1./255)
    #test_generator = test_datagen.flow_from_directory("/이미지 경로/exam",target_size=(100,100), batch_size=100, class_mode='categorical')
    new_model = keras.models.load_model('model.h5')
    new_model.summary()
    loss, acc = new_model.evaluate_generator(test_generator, steps=5) 
    data = {"success": False} # dictionary 형태의 데이터를 만들어 놓고 (딕셔너리에 데이터 넣는 방법1 : dictionary_name = {key:value}) 
    
    data["loss_accuracy"] = acc # 호출한 모델의 정확도를 넣습니다. (딕셔너리에 데이터 넣는 방법2 : dictionary_name[key] = value)
 
    data["success"] = True # 같은 방식으로 가지고 있는 key의 value를 바꿀수 있습니다.
            
    return jsonify(str(acc))

# @app.route('/predict', methods = ['POST'])  
# def predict():
#     if request.method == 'POST':

#         return render_template('hello.html')

# @app.route('/environments/<language>')  
# def environments(language):  
#     return jsonify({"language":language}) #받아온 데이터 다시 전송 

if __name__== '__main__': # 모델로드
    def get_model():
        global model
    model = load_model('model.h5')
    app.run(debug = True)





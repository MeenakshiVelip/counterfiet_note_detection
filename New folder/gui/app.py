from flask import *
from model_methods import predict_image

app = Flask(__name__, static_url_path='/static')  
  

@app.route("/")
def home():
  return render_template("home.html",base_url=request.base_url)

@app.route("/upload",methods=['POST'])
def upload():
  f = request.files['file']
  #file_name = "uploaded." + f.filename.split(".")[-1]
  file_name="static/"+f.filename
  f.save(file_name)
  res = predict_image(file_name)

  return render_template('result.html',result=res,file_name=file_name)

    
app.run()

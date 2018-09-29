from flask import *
from datetime import datetime
from pymongo import MongoClient
import cloudinary
from cloudinary import uploader

#Config cloudinary
cloudinary.config(
  cloud_name = 'flask-image',  
  api_key = '133444264233997',  
  api_secret = 'SrlSO-4T4W2lQx72PEYGHSEnOwU'  
)

#Connect database
client = MongoClient("mongodb://admin:admin123@ds051933.mlab.com:51933/flaskimgur")
db = client.flaskimgur

app = Flask(__name__)

@app.route('/', methods= ['GET','POST'])
def index():
    if request.method == "GET":
        return render_template('upload.html')
    elif request.method == 'POST':
        files = request.files.getlist('image')
        for file in files:
            img = uploader.upload(file)
            link = img['url']
            db.Image.insert({"link":link, "created_date":datetime.now()})
        return redirect("collection")

@app.route("/collection/")
def detail():
    list_image = db.Image.find({})
    return render_template("detail.html", images = list_image)

if __name__ == '__main__':
  app.run(debug=True)
 
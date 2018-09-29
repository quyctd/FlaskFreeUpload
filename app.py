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


@app.template_filter()
def timesince(dt, default="just now"):
    """
    Returns string representing "time since" e.g.
    3 days ago, 5 hours ago etc.
    """

    now = datetime.now()
    diff = now - dt
    
    periods = (

        (diff.days // 365, "year", "years"),
        (diff.days // 30, "month", "months"),
        (diff.days // 7, "week", "weeks"),
        (diff.days, "day", "days"),
        (diff.seconds // 3600, "hour", "hours"),


        (diff.seconds // 60, "minute", "minutes"),


    )

    for period, singular, plural in periods:
        print(period)
        print(singular)
        if period:
            return "%d %s ago" % (period, singular if period == 1 else plural)

    return default

if __name__ == '__main__':
  app.run(debug=True)
 
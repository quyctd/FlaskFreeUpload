from flask import *
from datetime import datetime
from pymongo import MongoClient, DESCENDING
import cloudinary
from cloudinary import uploader
import os

#Config cloudinary
cloudinary.config(
  cloud_name = os.environ.get('CLOUD_NAME'),  
  api_key = os.environ.get('API_KEY'),  
  api_secret = os.environ.get('API_SECRET')
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
    list_image = db.Image.find({}).sort("created_date",DESCENDING)
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
        
        if period:
            return "%d %s ago" % (period, singular if period == 1 else plural)

    return default

if __name__ == '__main__':
  app.run(debug=True)
 
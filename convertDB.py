from pymongo import MongoClient, DESCENDING
import cloudinary
from cloudinary import uploader
import os

#Config cloudinary cloud
cloudinary.config(
  cloud_name = 'flask-image',  
  api_key = '133444264233997',  
  api_secret = 'SrlSO-4T4W2lQx72PEYGHSEnOwU'
)

#Path of current file
my_path = os.path.abspath(os.path.dirname(__file__))


def convert_local_to_url(uri, collection, url_field):
    client = MongoClient(uri)
    db_name = uri.split("/")[-1]
    db = client[db_name]
    docs = db[collection].find({})
    for doc in docs:
        #Upload file to free host
        path = os.path.join(my_path, doc[url_field])
        image_file = open(path, 'rb')
        imager = uploader.upload(image_file)
        link = imager['url']

        #return new url to db
        doc[url_field] = link
        print(doc)

convert_local_to_url("mongodb://admin:admin123@ds051933.mlab.com:51933/flaskimgur", "Image_local", "link")

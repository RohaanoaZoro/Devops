
from pymongo import MongoClient

def MongoDatabase():
    client = MongoClient('mongodb+srv://cluster0.66vps.gcp.mongodb.net/myFirstDatabase', 27017,  username='Roal5809', password='Zxcvbnm@2')
    db = client.studentdb
    colz = db.student_service
    return colz
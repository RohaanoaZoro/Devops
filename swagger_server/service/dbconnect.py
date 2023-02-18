
from pymongo import MongoClient

def MongoDatabase():
    client = MongoClient('localhost', 27017)
    db = client.studentdb
    colz = db.student_service
    return colz
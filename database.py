from pymongo import MongoClient


client = MongoClient("mongodb://localhost: ")
db = client.student_database

from pymongo import MongoClient
from models import Student


client = MongoClient("mongodb://localhost:27017")
db = client.student_database
collection = db.students

def create_student(student: Student):
    student_data = student.dict()
    collection.insert_one(student_data)
    return student_data

def get_student(student_id: int):
    return collection.find_one({"student_id": student_id})

def update_student(student_id: int, student: Student):
    student_data = student.dict()
    result = collection.update_one({"student_id": student_id}, {"$set": student_data})
    return result.matched_count

def delete_student(student_id: int):
    result = collection.delete_one({"student_id": student_id})
    return result.deleted_count

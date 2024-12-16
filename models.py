from pydantic import BaseModel

class Student(BaseModel):
    student_name: str
    student_id: int
    student_email: str
    student_contact: str
    student_address: str
    student_age: int
    student_gender: str

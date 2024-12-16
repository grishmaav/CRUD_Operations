from fastapi import APIRouter, HTTPException
from models import Student
import crud

router = APIRouter()

@router.post("/")
async def create_student(student: Student):
    student_data = crud.create_student(student)
    return student_data

@router.get("/{student_id}")
async def read_student(student_id: int):
    student = crud.get_student(student_id)
    if student:
        return student
    raise HTTPException(status_code=404, detail="Student not found")

@router.put("/{student_id}")
async def update_student(student_id: int, student: Student):
    result = crud.update_student(student_id, student)
    if result:
        return student.dict()
    raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/{student_id}")
async def delete_student(student_id: int):
    result = crud.delete_student(student_id)
    if result:
        return {"message": "Student deleted"}
    raise HTTPException(status_code=404, detail="Student not found")

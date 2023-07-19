from ast import List
from fastapi.param_functions import Depends
from http.client import ResponseNotReady, responses
from typing import Optional
from urllib import response
from fastapi import FastAPI,Response,status,HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from random import randrange
app = FastAPI()
students=[]
update_students=[]
class Student(BaseModel):
    name:str
    age:int
    year:Optional[str]=None
    subjects:Optional[str]=None
    
    
class Update_Student(BaseModel):
    name:Optional[str]=None
    age:Optional[int]=None
    year:Optional[str]=None
    subjects:Optional[str]=None
    
class Base1(Student):
    user:str
    pass
    
def find_Student(id):
    for p in students:
        if p['id']==id:
            return p
        
def find_Index(id):
    for i,p in enumerate(students):
        if p['id']==id: 
            return i


@app.post("/creates")
def create_base(student:list[Student]):
    return student
@app.post("/create", status_code=status.HTTP_201_CREATED)
def create_student( student:list[Student], update_student=Update_Student):
    print(student.dict())
    student_dict=student.dict()
    student_dict['id']=randrange(1,1000000)
    students.append(student_dict)
    print(students)
    update_students.append(student_dict)
    return {"data":student_dict}

@app.get("/students/{id}")
def get_student(id:int, response:Response):
    print(type(id))
    student_d=find_Student(id)
    print(students)
    if not student_d:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"message":f"{id} not found"}
    return {"student_detail":student_d}

@app.get("/students")
def get_Students():
    return {"data":students}

@app.get("/student/latest")
def get_Latest():
    student_latest=students[len(students)-1]
    return {"last_student":student_latest}

@app.put("/update/{id}")
def update_student(id:int, student:Student):
    index=find_Index(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"student with id:{id} does not exist")
    student_dict=student.dict()
    student_dict['id']=id
    students[index]=student_dict
    update_students[index]=student_dict
    return {"data":student_dict}

@app.patch("/patch/{id}")
def patch_student(id:int, update_student:Update_Student):
    index=find_Index(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"student with id:{id} does not exist")
    update_student_dict=update_student.dict()
    update_student_dict['id']=id
    update_students[index]=update_student_dict
    for i,j in update_student_dict.items():
        if j==None:
            continue
        else:
            students[index][i]=j
    print(students[index],update_students[index],update_student_dict,type(update_student_dict))
    return {"data":students[index]}

@app.delete("/student/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Student(id:int):
    index=find_Index(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"student with id:{id} does not exist")
    students.pop(index)
    update_students.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
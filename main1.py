from ctypes import Union
import datetime
from pathlib import Path
import time
from typing import Annotated
from uuid import UUID
from fastapi import FastAPI,Query,Body
from enum import Enum
from pydantic import BaseModel,HttpUrl

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

@app.get("/users/{user_id}")
async def read_user(user_id:str):
    return {"user_id":user_id}


@app.post("/form/data")
async def file_bytes_len(file:bytes=File()):
    return ({"file":len(file)})

s=-1
    for i,p in enumerate(update_students):
        if p['id']==id:
            s=i
            break
    
    for i,j in students[index].items():
        print(i,j)
        a=students[index].get(i)
        b=update_students[index].get(i)
        if b==None:
            continue
        else:
            students[index].update({i:b})
    print(s)
    
@app.patch("/patch/{id}")
def patch_student(id:int, student:Student, update_student:Update_Student):
    index=find_Index(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"student with id:{id} does not exist")
    s=-1
    student_dict=student.dict()
    student_dict['id']=id
    students[index]=student_dict
    update_student_dict=update_student.dict()
    update_student_dict['id']=id
    update_students[index]=update_student_dict
    for i,p in enumerate(update_students):
        if p['id']==id:
            s=i
            break
    
    for i,j in students[index].items():
        print(i,j)
        a=students[index].get(i)
        b=update_students[index].get(i)
        if b==None:
            continue
        else:
            students[index].update({i:b})
    print(students)
    return {"data":s}    
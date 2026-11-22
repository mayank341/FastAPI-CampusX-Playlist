from pydantic import BaseModel

class Student(BaseModel):
    name:str
    age:int

student=Student(name="Krishna",age=30)

print(student)
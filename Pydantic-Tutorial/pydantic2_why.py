from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int

def insert_patient(patient: Patient):
    print("Inserting patient into database")
    print("Patient name:", patient.name)
    print("Patient age:", patient.age)
    print("Patient inserted successfully!")



def update_patient(patient:Patient):
    print("Updating patient in database")
    print("Patient name:", patient.name)
    print("Patient age:", patient.age)
    print("Patient updated successfully!")

patient=Patient(name="RadhaKrishna",age=30)

insert_patient(patient)
update_patient(patient)





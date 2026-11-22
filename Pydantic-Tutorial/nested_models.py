from pydantic import BaseModel
from typing import List,Dict

class Address(BaseModel):
    city:str
    state:str
    pin_code:int

class Patient(BaseModel):
    name:str
    age:int
    weight:float
    address:Address

address_info={
    "city":"New York",
    "state":"NY",
    "pin_code":10001
}
address1=Address(**address_info)
patient_info={
    "name":"John Doe",
    "age":30,
    "weight":70.5,
    "address":address1
}


patient = Patient(**patient_info)
print(patient)
print("Patient name:", patient.name)
print("Patient city:",patient.address.city)


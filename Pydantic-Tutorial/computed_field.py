from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict

class Patient(BaseModel):
    name:str
    age:int
    email:EmailStr
    weight:float
    height:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]

# Computed Field to calculate BMI (Body Mass Index) based on weight and height
#  what is computed field?
#  Computed fields are used to define properties that are derived from other fields in the model.
# They allow you to create read-only attributes that are calculated based on the values of other fields, without storing them in the model's data.




    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi


def update_patient_data(patient:Patient):
    print("Updating patient in database")
    print("Patient name:",patient.name)
    print("Patient age:",patient.age)
    print("Patient email:",patient.email)
    print("Patient weight:",patient.weight)
    print("Patient height:",patient.height)
    print("Patient married:",patient.married)
    print("Patient allergies:",patient.allergies)
    print("Patient contact details:",patient.contact_details)
    print("Patient BMI:",patient.bmi)
    print("Patient updated successfully!")


patient_info={
        'name':'John Doe',
        'age':30,
        'email':'john.doe@example.com',
        'weight':70.5,
        'height':1.75,
        'married':True,
        'allergies':['Peanuts', 'Shellfish'],
        'contact_details':{'phone': '123-456-7890', 'address': '123 Main St'}}

patient = Patient(**patient_info)

update_patient_data(patient)
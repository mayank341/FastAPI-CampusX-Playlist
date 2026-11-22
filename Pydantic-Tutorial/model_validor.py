from pydantic import BaseModel, EmailStr, model_validator
from typing import Dict, List


class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

#  Model Validator to check if emergency contact is provided for patients above 60 years of age
#  what  is model validator?
#  Model validators are used to validate the entire model after all the fields have been validated. 
# They can be used to enforce constraints that depend on multiple fields or to perform complex validation logic that cannot be expressed using field validators alone.

    @model_validator(mode="after")
    def validate_emergency_contact(self):
        if self.age > 60 and "emergency_contact" not in self.contact_details:
            raise ValueError(
                "Emergency contact is required for patients above 60 years of age"
            )
        return self


def update_patient(patient: Patient):
    print("Updating patient in database")
    print("Patient name:", patient.name)
    print("Patient age:", patient.age)
    print("Patient weight:", patient.weight)
    print("Patient married:", patient.married)
    print("Patient allergies:", patient.allergies)
    print("Patient contact details:", patient.contact_details)
    print("Patient updated successfully!")


patient_info = {
    "name": "John Doe",
    "age": 65,
    "weight": 70.5,
    "married": True,
    "allergies": ["Peanuts", "Shellfish"],
    "contact_details": {
        "phone": "123-456-7890",
        "email": "johndoe@example.com",
        "emergency_contact": "555-0100",
    },
}

patient1 = Patient(**patient_info)
update_patient(patient1)


    




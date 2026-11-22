
from pydantic import BaseModel, EmailStr, field_validator
from typing import List, Dict


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    # 1. Email validation :::
    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Invalid email domain")

        return value

    # 2. Name transformation :::
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    # 3. Age validation
    @field_validator('age')  #we can mode here after the field name to validate the age field
    @classmethod
    def validate_age(cls, value):
        if value < 0:
            raise ValueError("Age cannot be negative")

        return value


def update_patient(patient: Patient):
    print("Updating patient in database")
    print("Patient name:", patient.name)
    print("Patient age:", patient.age)
    print("Patient email:", patient.email)
    print("Patient weight:", patient.weight)
    print("Patient married:", patient.married)
    print("Patient allergies:", patient.allergies)
    print("Patient contact details:", patient.contact_details)
    print("Patient updated successfully!")


patient_info = {
    'name': 'John Doe',
    'age': 30,
    'email': 'john.doe@hdfc.com',
    'weight': 70.5,
    'married': True,
    'allergies': ['peanuts'],
    'contact_details': {
        'phone': '123-456-7890',
        'address': '123 Main St'
    }
}

patient = Patient(**patient_info)

update_patient(patient)

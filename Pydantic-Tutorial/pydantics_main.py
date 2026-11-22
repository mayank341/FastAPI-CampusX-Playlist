
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict, Annotated


class Patient(BaseModel):

    name: Annotated[
        str,
        Field(
            max_length=50,
            title="Name of the Patient",
            description="Give the name of the patient in less than 50 chars"
        )
    ]

    age: Annotated[
        int,
        Field(
            gt=0,
            lt=150,
            title="Age of the Patient",
            description="Give the age of the patient in years"
        )
    ]

    email: EmailStr

    weight: Annotated[float, Field(gt=0, strict=True)]

    married: Optional[bool] = Field(
        default=None,
        description="Is the patient married or not"
    )

    allergies: Annotated[
        Optional[List[str]],
        Field(default=None, max_length=5)
    ]

    contact_details: Dict[str, str]


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
    'email': 'john.doe@example.com',
    'weight': 70.5,
    'married': True,
    'allergies': ['peanuts'],
    'contact_details': {
        'phone': '123-456-7890',
        'address': '123 Main St'
    }
}

patient1 = Patient(**patient_info)

update_patient(patient1)








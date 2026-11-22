from pydantic import BaseModel
from typing import List,Dict, Optional

class Address(BaseModel):
    city:str
    state:str
    pin_code:int

class Patient(BaseModel):
    name:str
    age: Optional[int] = None
    address:Address

address_dict={
    "city":"New York",
    "state":"NY",
    "pin_code":10001
}
address1=Address(**address_dict)

patient_dict={
    "name":"John Doe",
    # "age":30,
    "address":address1
}
patient1=Patient(**patient_dict)

# temp=patient1.model_dump(include=['name','address'])
# temp=patient1.model_dump(exclude={'name'})
temp=patient1.model_dump(exclude_unset=True)
print(temp)
print(type(temp))



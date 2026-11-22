from fastapi import FastAPI,Path,HTTPException,Query
import json

app = FastAPI()

def load_data():
    with open("patient.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/about")
def about():
    return {
        "message": "A fully functional API to manage Your Patient Records."
    }


@app.get("/view")
def view():
    return load_data()


@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):

    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )

@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description='Sort by height, weight or bmi'),
    order: str = Query('asc', description='asc or desc')
):

    valid_fields = ['height', 'weight', 'bmi']

    sort_by = sort_by.lower()
    order = order.lower()

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f'Invalid field. Choose from {valid_fields}'
        )

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400,
            detail='Select asc or desc'
        )

    data = load_data()

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=(order == 'desc')
    )

    return sorted_data